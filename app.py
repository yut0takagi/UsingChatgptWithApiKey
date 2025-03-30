from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

# 設定
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

# 初期化
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")


def read_file_text(filepath):
    ext = filepath.rsplit(".", 1)[1].lower()
    if ext == "txt":
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == "pdf":
        try:
            import PyPDF2
            with open(filepath, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        except Exception as e:
            return f"[PDF読み取りエラー: {str(e)}]"
    else:
        return "[サポートされていないファイル形式です]"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message")
    model = data.get("model", "gpt-3.5-turbo")
    filename = data.get("filename")

    # ファイルがある場合はその中身を message として使う
    if filename:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(filename))
        if os.path.exists(filepath):
            file_content = read_file_text(filepath)
            message = f"以下のファイル内容を読んでください:\n\n{file_content}"

    if not message:
        return jsonify({"error": "メッセージもファイルも指定されていません"}), 400

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "あなたはファイルや文章を読み取り、質問に答えるアシスタントです。"},
            {"role": "user", "content": message}
        ]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "ファイルが見つかりません"}), 400

    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({"error": "許可されていないファイル形式です"}), 400

    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    return jsonify({"message": f"{filename} をアップロードしました。", "filename": filename})

if __name__ == "__main__":
    app.run(debug=True)