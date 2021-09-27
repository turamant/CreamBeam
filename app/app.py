from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Configuration)


