const username = document.getElementById('name')
const email = document.getElementById('email')
const password = document.getElementById('senha')

async function signIn(){

    const response = await fetch("http://localhost:3578/register", {
    method: 'POST',
    headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        "username": username.value,
        "email": email.value,
        "password": password.value,
    }),
    });

    console.log(response.body.username);

    response.json().then(data => {
    console.log(data);
    
    if (data.confirm == true){
        alert("Usuário cadastrado com sucesso!");
        window.location.href = "/login";
    };
    });
}

async function logIn(){

    const response = await fetch("http://localhost:3578/login", {
    method: 'POST',
    headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        "email": email.value,
        "password": password.value,
    }),
    });

    console.log(response.body.username);

    response.json().then(data => {
    console.log(data);
    
    if (data.confirm == true){
        alert("Usuário logado com sucesso!");
        window.location.href = "/";
    };
    });
}