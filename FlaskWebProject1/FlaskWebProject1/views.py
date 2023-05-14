"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from FlaskWebProject1 import app
import pyshorteners

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/shorten', methods =["GET", "POST"])
def shorten():
    if request.method == "POST":
       input = request.form.get("userInput")
       s = pyshorteners.Shortener()
       shortenedUrl = s.tinyurl.short(input)
       result = '<a href="%s">%s!</a>'%(shortenedUrl, shortenedUrl)
       return result
    return render_template("form.html")


