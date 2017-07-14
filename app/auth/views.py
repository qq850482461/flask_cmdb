from . import auth
from flask import redirect,render_template,request

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username,password)
    return render_template('login.html')
