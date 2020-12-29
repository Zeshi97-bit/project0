from flask import Flask, render_template

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/contact")
def cont():
    return render_template("contact.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route ("/about")
def about():
    return render_template("about.html")
