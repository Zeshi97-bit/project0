import os
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import request

app=Flask(__name__)
engine = create_engine("postgres://postgres:zeshan123@localhost:5432/mydb")

db=scoped_session(sessionmaker(bind=engine))



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
@app.route ("/signIn")
def signin():
    return render_template("signIn.html")
@app.route("/signup")
def signup():
    return render_template("signUp.html")

@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    email = request.form.get("email")
    comment = request.form.get("message")
    db.execute("INSERT INTO friend.comment (name, email, comment) VALUES(:name, :email, :comment)",
                {"name": name, "email": email, "comment": comment})
    db.commit()
    return render_template("success.html", username=name)

if __name__=="__main__":
    main()
