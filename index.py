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
      jsonData = request.get_json()
      return loginController.login(jsonData['email'], jsonData['password'])      

@app.route('/register', methods=['GET', 'POST'])
def create():
   if request.method == 'GET':
      return render_template('/register.html')
   else:
      jsonData = request.get_json()
      return registerController.register(jsonData['username'], jsonData['email'], jsonData['password'])

@app.route('/update', methods= ['POST'])
def update():
   jsonData = request.get_json()
   return registerController.update(jsonData['username'], jsonData['email'], jsonData['password'])

@app.route('/delete', methods= ['POST'])
def delete():
   jsonData = request.get_json()
   return registerController.delete(jsonData['email'])
   
if __name__ == '__main__':
   app.run(host='localhost', port=3578)