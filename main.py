from flask_login import LoginManager
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
"""
def create_app():
    app = Flask(__name__)
    from handler.user_handler import user_bp
    app.register_blueprint(user_bp, url_prefix='/')
    return app
app = create_app()
"""
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':

    app.run(debug=True)

