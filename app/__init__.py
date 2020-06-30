# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db variable initialization

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from .models import RequestItems
db.create_all()
db.session.commit()

try:
    sample = RequestItems("test", 9, "vm", False, "Adam Hicks", 3.50)
    db.session.add(sample)
    db.session.commit()
except:
    pass

from app import views, models