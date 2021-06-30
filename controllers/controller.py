from app import app
from flask import render_template
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template("orders.html", title="Orders", orders=orders)

@app.route("/orders/<index>")
def order(index):
    return render_template("order.html", title="Order", order=orders[int(index)])
