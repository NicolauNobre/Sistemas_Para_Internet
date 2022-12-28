const username = document.getElementById('name')
const email = document.getElementById('email')
const password = document.getElementById('senha')

async function signIn(){

    const response = await fetch("http://localhost:3578/register", {
    method: 'POST',
    headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        "username": username.value,
        "email": email.value,
        "password": password.value,
    }),
    });

    response.json().then(data => {
    console.log(data);
    });
}