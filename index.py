# Descrição: Arquivo principal do projeto
# Importando biblioteca do Flask
from flask import Flask, render_template, request

# Importando controladores
from controllers import loginController
from controllers import registerController

# Iniciando o Flask
app = Flask(__name__)

# Definindo rotas
# Definindo rota para a página inicial
@app.route('/')
def home_page():
   # Renderizando a página inicial
   return render_template('/home.html')

# Definindo rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
# Definindo função para a rota
def read():
   # Verificando o método da requisição
   if request.method == 'GET':
      # Renderizando a página de login
      return render_template('/login.html')
   elif request.method == 'POST':
      # Obtendo os dados do formulário
      jsonData = request.get_json()
      # Retornando o resultado da função de login
      return loginController.login(jsonData['email'], jsonData['password'])      

# Definindo rota para a página de cadastro
@app.route('/register', methods=['GET', 'POST'])
# Definindo função para a rota
def create():
   # Verificando o método da requisição
   if request.method == 'GET':
      # Renderizando a página de cadastro
      return render_template('/register.html')
   elif (request.method == 'POST'):
      # Obtendo os dados do formulário
      jsonData = request.get_json()
      # Retornando o resultado da função de cadastro
      return registerController.register(jsonData['username'], jsonData['email'], jsonData['password'])

# Definindo rota para a página de edição
@app.route('/update', methods= ['GET','UPDATE'])
# Definindo função para a rota
def update():
   # Verificando o método da requisição
   if request.method == 'GET':
      return render_template('/edit.html')
   elif request.method == 'UPDATE':
      # Obtendo os dados do formulário
      jsonData = request.get_json()
      # Retornando o resultado da função de edição
      return registerController.update(jsonData['username'], jsonData['email'], jsonData['password'])

# Definindo rota para a página de exclusão
@app.route('/delete', methods= ['DELETE'])
# Definindo função para a rota
def delete():
   # Obtendo os dados do formulário
   jsonData = request.get_json()
   # Retornando o resultado da função de exclusão
   return registerController.delete(jsonData['email'] , jsonData['password'])

# Executando o Flask 
if __name__ == '__main__':
   app.run(host='localhost', port=3578)