from model import app,db,Products
from flask import render_template

@app.route('/')
def sales():
    sl = Products.query.all()
    for i in sl:
        print(i)
    
    print(sl)
    return render_template("index.html",sl=sl)



with app.app_context():
    db.create_all()
app.run(debug=True)