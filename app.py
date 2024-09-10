from flask import Flask, url_for, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
from datetime import datetime
import json
import subprocess
import os
import sys

app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/index", methods=["POST"])
def upload():

    target = os.path.join(APP_ROOT, 'uploads')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("upload"):
        print(file)

        filename = file.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print(destination)
        file.save(destination)

    return render_template('index.html')




