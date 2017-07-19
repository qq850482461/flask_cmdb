from . import main
from flask import render_template,redirect
from flask_login import login_required



@main.route('/',methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html',name="test")

