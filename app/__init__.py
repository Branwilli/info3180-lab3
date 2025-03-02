from flask import Flask
from flask_mail import Mail 
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'g09lh749js012m'

mail = Mail(app)
from app import views

if __name__ == '__main__':
    app.run(debug=True)