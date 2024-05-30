from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
class Base(DeclarativeBase):pass

db = SQLAlchemy(model_class=Base)

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:6979@localhost/alchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer,primary_key =True,nullable =False,autoincrement =True)
    pid = db.Column(db.Integer,nullable =False)
    quantity = db.Column(db.Integer,nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow(),nullable=False)

class Inventory(db.Model):
    __tablename__ = 'inventories'
    id = db.Column(db.Integer,primary_key =True,nullable =False,autoincrement =True)
    pid = db.Column(db.Integer,nullable =False)
    quantity = db.Column(db.Integer,nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow(),nullable=False)