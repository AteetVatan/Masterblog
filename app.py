"""The Main Flask app Module"""
from flask import Flask
from views import AppView

app = Flask(__name__)

if __name__ == '__main__':
    app_view = AppView(app)
    app_view.app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
