"""
Created on Tue Nov 17 09:09:01 2020

@author: alierbey
"""
import os
from linear import toplama
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    article = dict()
    article["title"] = "sd"
    article["body"] = "icerik"
    return render_template("index.html",article= article)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/people")
def people():
    return render_template("people.html")

@app.route("/linear")
def linear():
    x = toplama(5,6)
    return render_template("linear.html", ekran =  x)


@app.route("/analiz")
def analiz():
    return render_template("analiz.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)



