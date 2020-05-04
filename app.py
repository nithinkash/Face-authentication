from flask import Flask, render_template, redirect, request, url_for
import os, subprocess
from werkzeug import secure_filename
import time

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('index.html')


@app.route('/upload', methods=['GET','POST'])
def upload():
    clicked = None
    if request.method=='POST':
        f = request.form['data']
        f.save(secure_filename(f.filename))
    return "Success"

if __name__ == '__main__':
    app.run(threaded=True)
