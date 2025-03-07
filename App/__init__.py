from flask import Flask
import json
import os

from .views import chatbot

def create_app():
    app = Flask(__name__)
    app.config.from_object('App.config')
    app.register_blueprint(chatbot.bp)
    return app

