const urlEndPoint = "https://c5j7g4oypbub6kqvkbdpmvhhra0njfgr.lambda-url.us-west-2.on.aws/"


function setLoginMessage(element, type, message) {
    const loginMessage = element.querySelector(".login__message");

    loginMessage.textContent = message;
    loginMessage.classList.remove("login__message--success", "login__message--error"); //get rid of current style
    loginMessage.classList.add(`login__message--${type}`); //type is success or error
}


function login() {
    const usernameInput = document.getElementById("username")
    const passwordInput = document.getElementById("password")

    let data = {
        operation: "get_cards",
        payload: {
            username: usernameInput.value,
            password: passwordInput.value,
            object: ''
        }
    };

    fetch(urlEndPoint, {
        method: "POST",
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            //"Access-Control-Allow-Origin": 'https://patpragman.github.io/swe_class_project'
        },
        body: JSON.stringify(data)
    }).then(res => {
        const data = res.json();
        return data
    }).then(data => {

        if (data['success']) {
            // if it was successful, run the function to launch the app
            store_and_load_app(data['return_payload'], usernameInput.value, passwordInput.value);
        }
    }
    );


}



function store_and_load_app(return_payload, username, password) {

    // store the login login info and the cards and open the html that contains the app

    window.sessionStorage.setItem("username", username);
    window.sessionStorage.setItem("password", password);
    window.sessionStorage.setItem("return_payload", JSON.stringify(return_payload));
    window.location.href = "user.html";

}

function createdNewUser() {
    const singupUsernameInput = document.getElementById("signupUsername")
    const signupPasswordInput = document.getElementById("signupPassword")
    const verifyPasswordInput = document.getElementById("verifyPassword")

    if (signupPasswordInput.value == verifyPasswordInput.value) {

        let user = {
            username: singupUsernameInput.value,
            password: signupPasswordInput.value
        }


        let data = {
            operation: "create_user",
            payload:
            {
                username: "no user",
                password: "na",
                object: user
            }


        };

        fetch(urlEndPoint, {
            method: "POST",
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                //"Access-Control-Allow-Origin": 'https://patpragman.github.io/swe_class_project'
            },
            body: JSON.stringify(data)
        }).then(res => {
            console.log("Request complete! response:", res);
        });

        return true;
    } else {
        signupPasswordInput.focus();
        return false;
    }

}

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#login");
    const createAccountForm = document.querySelector("#createAccount");

    document.querySelector("#linkCreateAccount").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.add("login--hidden");
        createAccountForm.classList.remove("login--hidden");
    });

    document.querySelector("#linkLogin").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.remove("login--hidden");
        createAccountForm.classList.add("login--hidden");
    });

    loginForm.addEventListener("submit", e => {
        e.preventDefault();


        if (login() == true) {
            console.log(usernameInput.value, passwordInput.value)
            setLoginMessage(createAccountForm, "success", "Account Created!")
        }
        else {
            setLoginMessage(loginForm, "error", "Invalid username/password combination");
        }
    });

    createAccountForm.addEventListener("submit", e => {
        e.preventDefault();
        if (createdNewUser() == false) {
            setLoginMessage(createAccountForm, "error", "Passwords do not match, Try again!")


        } else {
            setLoginMessage(createAccountForm, "success", "Account Created!")
        }

    })


});