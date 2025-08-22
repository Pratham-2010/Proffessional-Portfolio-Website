from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact',methods=['GET','POST'])
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
