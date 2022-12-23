// Script destinado as funções de login e cadastro de usuário (páginas de login e cadastro)

// Elementos html do inputs da página de cadastro
const nome = document.getElementById("name")
const email = document.getElementById("email")
const senha = document.getElementById("senha")
const sobre = document.getElementById("sobre")
const name_label = document.querySelector('#name');
// Elementos html do inputs da página de login
const usr_label = document.querySelector('#email');
const psw_label = document.querySelector('#senha');

// Função que realiza login de usuário
function logIn(){
    let user_list = []
    // Verifica se todos os campos foram preenchidos (usuario e senha)
    if(email.value != '' && senha.value != '') {
        user_list = JSON.parse(localStorage.getItem('user_list'))
        if (user_list == null){
            setTimeout(() => {alert('Nenhum usuário cadastrado. Cadastre-se e tente fazer o login novamente');}, 100)   
        } else {
            // Percorre a lista de usuários cadastrados para encontrar dupla equivalência (usuario e senha)
            let user_valid = user_list.find((user) => {
                return user.user_mail === email.value && user.user_psw === senha.value
            })
            // Caso não for encontrado
            if(user_valid == undefined){
                setTimeout(() => {alert('Usuário ou senha inválidos');}, 100)
                usr_label.className = 'form-control is-invalid'
                psw_label.className = 'form-control is-invalid'
            }
            // Caso encontrado
            else if (email.value == user_valid.user_mail && senha.value == user_valid.user_psw){
                localStorage.setItem('logged_user', JSON.stringify(user_valid))
                alert('Login realizado com sucesso!\nBem vindo ao Flask Example!');
                window.location.href = 'home.html'  
            }
        }
    } else {
        setTimeout(() => {alert('Preencha todos os campos para realizar o login');}, 100)
        usr_label.className = 'form-control is-invalid'
        psw_label.className = 'form-control is-invalid'  
    }

}

// Valida o email verificando se contém '@', letras e numeros (opcionais)
function validateEmail(input) {
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (input.value.match(validRegex)) {
        return true;
    } else {
        return false;
    }
}

// Verifica na lista de usuários se já existe o email a ser cadastrado
function isEmailRepeated (){
    let user_list = JSON.parse(localStorage.getItem("user_list"))
    if (user_list != null) {
        for (let i = 0; i < user_list.length; i++) {
            if (email.value == user_list[i].user_mail){
                return true;
            } 
        }    
        return false;   
    }
    else {
        return false;
    }
}

// Função que cadastra o usuário
function signIn(){
    // Carrega a lista de usuários cadastrados, se não existir a cria
    let user_list = JSON.parse(localStorage.getItem("user_list") || '[]')
    // Verifica se todos os campos foram preenchidos
    if (nome.value != '' && email.value != '' && senha.value!= '' && sobre.value != ''){
        // Verifica se o email é repetido
        if (!isEmailRepeated()){
            // Realiza aa validação de email
            if (validateEmail(email)){
                // realiza a criação do objeto de usuário com suas credenciais
                user_list.push(
                    {
                        id: user_list.length + 1,
                        user_name: nome.value,
                        user_mail: email.value,
                        user_psw: senha.value,
                        fav_games: [],
                        user_desc: sobre.value
                    }
                )
                // Insere o objeto de usuário cadastrado na lsita de usuários
                localStorage.setItem('user_list', JSON.stringify(user_list))
                alert('Usuário cadastrado com sucesso!\nRedirecionando para a página de login...')
                window.location.href = 'index.html'
            } else {
                setTimeout(() => {alert('Endereço de email inválido. Use "@" para cadastrar um email válido');}, 100)
                usr_label.className = 'form-control is-invalid'
            }
        } else {
            alert("Usuário já cadastrado. Por favor, insira outro e-mail")     
        } 
    }
    else {
        name_label.className = 'form-control is-invalid'
        usr_label.className = 'form-control is-invalid'
        psw_label.className = 'form-control is-invalid'
        setTimeout(() => {alert('Preencha todos os campos para cadastrar-se');}, 100)
    }
    
        
}
// Função que seta as cores normais no formulário ao focar no mesmo (cadastro)
function setNormalColor(){
    name_label.className = 'form-control'
    usr_label.className = 'form-control'
    psw_label.className = 'form-control'    
}

// Função que seta as cores normais no formulário ao focar no mesmo (login)
function setNormalColorLogin(){
    usr_label.className = 'form-control'
    psw_label.className = 'form-control'    
}
// Função do menu dropdown
function dropMenu(){
    document.getElementById("dropdown-content").classList.toggle("show");
}

// Fecha o menu dropdown se o usuário clica fora dele
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
}

// Função que realiza o logout (seta o objeto de usuário logado para '' {vazio})
function logOut(){
    let empty_user = {
        id: '',
        user_name: '',
        user_mail: '',
        user_psw: '',
        fav_games: [] 
    } 
    localStorage.setItem('logged_user', JSON.stringify(empty_user)) 
    window.location.href = 'index.html' 
}

// Carrega o nome do usuário logado (do localStorage) para colocar na barra superior do site
if (document.title == "Games Library"){
    document.addEventListener('DOMContentLoaded', function() {
        logged_user = JSON.parse(localStorage.getItem('logged_user'))
        document.getElementById("p1").innerHTML = logged_user.user_name.split(' ')[0].charAt(0).toUpperCase() + logged_user.user_name.split(' ')[0].slice(1);
    }, false);
}
