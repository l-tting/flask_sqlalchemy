from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:6979@localhost/alchemy'
db = SQLAlchemy(app)

class Products(db.Model):
    id = db.Column(db.Integer,primary_key = True,nullable=False)
    name = db.Column(db.String(50),nullable = False)
    buying_price = db.Column(db.Integer,nullable = False)
    selling_price = db.Column(db.Integer,nullable = False)
    stock_quantity = db.Column(db.Integer,nullable = False)
    def __repr__(self):
        return f' (id ={self.id},name= {self.name},buying_price={self.buying_price},selling_price={self.selling_price},stock={self.stock_quantity})'
product = Products(name='chicken',buying_price=17,selling_price=20,stock_quantity=100)
db.session.add(product)
db.session.commit()

with app.app_context():
    db.create_all()
app.run(debug=True)

 


