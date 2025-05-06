from flask import render_template, request, jsonify, Blueprint, session
import openai
from dotenv import dotenv_values
import os
import base64

bp = Blueprint("chatbot", __name__, url_prefix="/chatbot")

@bp.route('/chatbot/')
def chat_bot():
    return render_template("chatbot/chatbot.html")

@bp.route("/chat", methods=["POST"])
def chat():
    API_KEY = os.getenv("OPENAI_API_KEY")
    openai.api_key = API_KEY
    data = request.get_json()
    user_message = data.get("message", "")
    image_data = data.get("image", None)
    
    try:
        messages = [{"role": "user", "content": user_message}]
        
        if image_data:
            # Base64エンコードされた画像データを追加
            messages[0]["content"] = [
                {"type": "text", "text": user_message},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_data}"
                    }
                }
            ]
            
            response = openai.ChatCompletion.create(
                model="gpt-4-vision-preview",
                messages=messages,
                max_tokens=300
            )
        else:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            
        ai_response = response["choices"][0]["message"]["content"]
    except Exception as e:
        ai_response = f"エラーが発生しました。管理者へお伝えください。エラー内容: {str(e)}"

    return jsonify({"response": ai_response})
