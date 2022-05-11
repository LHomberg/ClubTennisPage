from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from __init__ import create_app, db
import pandas as pd
from sqlalchemy import create_engine
import webemailserver
from models import User


main = Blueprint('main', __name__)


@main.route('/') 
def index():
    return render_template("home.html")

@main.route('/about')
def about():
    return render_template("about.html")

@main.route('/board')
def board():
    return render_template("board.html")

@main.route('/badgerclassic')
def badgerclassic():
    return render_template("badgerclassic.html")

@main.route('/faq')
def faq():
    return render_template("faq.html")

@main.route('/initial') 
@login_required
def initial():
    #connection = create_engine('sqlite:///db.sqlite').connect()
    #table_df = pd.read_sql_table("user", connection)
    #table_df = table_df.drop(columns=["password", "id", "officer"])
    #table = table_df.to_html()
    
    return render_template('initial.html', name=current_user.name)#, table=table)

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html")

@main.route('/email') 
@login_required
def email():
    return render_template("email.html")

@main.route('/roster')
@login_required
def roster():
    #connection = create_engine('sqlite:///db.sqlite').connect()
    #table_df = pd.read_sql_table("user", connection)
    #table_df = table_df.drop(columns=["password", "id", "officer"])
    #table = table_df.to_html()
    users = User.query
    return render_template("roster.html", users=users)

@main.route('/information')
@login_required
def information():
    return render_template("information.html")

@main.route("/email", methods=["GET", "POST"])
@login_required
def webemail():
    if request.method == "GET": 
        return render_template("email.html")
    else: 
        receiver = request.form.get("receiver")
        cc = request.form.get("cc")
        subject = request.form.get("subject")
        body = request.form.get("body")
        attachment = request.files['file']

        print(receiver)
        print(cc)
        print(subject)
        print(body)
        print(attachment)
        
        if receiver == "":
            connection = create_engine('sqlite:///db.sqlite').connect()
            table_df = pd.read_sql_table("user", connection)
            receiver = table_df["email"]
            print("LIST TIME")
            print(receiver)
            webemailserver.email(subject, body, receiver, cc, attachment, True)
        else:
            webemailserver.email(subject, body, receiver, cc, attachment)

        return render_template("email.html")

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run("0.0.0.0", debug=True) # run the flask app on debug mode
