from flask import render_template, request, jsonify, Blueprint, session
import openai
from dotenv import dotenv_values
import os

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
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        ai_response = response["choices"][0]["message"]["content"]
    except Exception as e:
        ai_response = "エラーが発生しました。管理者へお伝えください。"

    return jsonify({"response": ai_response})
