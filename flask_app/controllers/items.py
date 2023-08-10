from flask_app import app     
from flask import render_template

@app.route("/items")
def dash():
    return render_template("dash.html")

@app.route("/items/create")
def create_item():
    return render_template("create.html")

@app.route("/items/<int:id>/edit")
def edit_item(id):
    return render_template("edit.html")

@app.route("/items/<int:id>/view")
def view_one_item(id):
    return render_template("view_one.html")