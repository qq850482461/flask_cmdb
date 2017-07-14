from . import main
from flask import render_template,redirect

@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html',name="test")

