from flask import Flask, render_template, request
from controllers import loginController
from controllers import registerController

app = Flask(__name__)

@app.route('/')
def home_page():
   return render_template('/home.html')

@app.route('/login', methods=['GET', 'POST'])
def read():
   if request.method == 'GET':
      return render_template('/index.html')
   elif request.method == 'POST':
      return loginController.login(request.form['email'], request.form['password'])
      

@app.route('/register', methods=['GET', 'POST'])
def create():
   if request.method == 'GET':
      return render_template('/register.html')
   else:
      return registerController.register(request.form['username'], request.form['email'], request.form['password'])

@app.route('/update', methods= ['POST'])
def update():
   return registerController.update(request.form['username'], request.form['email'], request.form['password'])

@app.route('/delete', methods= ['POST'])
def delete():
   return registerController.delete(request.form['email'])

if __name__ == '__main__':
   app.run(host='localhost', port=3578)