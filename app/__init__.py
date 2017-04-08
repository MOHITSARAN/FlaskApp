from flask import Flask

app = Flask(__name__)

app.config["DATABASE"] = 'database.db'
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "Mohit$aran"
app.config["USERNAME"] = "Mohit"
app.config["PASSWORD"] = "admin"

from app import views, models
