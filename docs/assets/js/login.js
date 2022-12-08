const urlEndPoint = "https://c5j7g4oypbub6kqvkbdpmvhhra0njfgr.lambda-url.us-west-2.on.aws/"

const loginForm = document.querySelector("#login");
const createAccountForm = document.querySelector("#createAccount");

function setLoginMessage(element, type, message) {
    const loginMessage = element.querySelector(".login__message");

    loginMessage.textContent = message;
    loginMessage.classList.remove("login__message--success", "login__message--error"); //get rid of current style
    loginMessage.classList.add(`login__message--${type}`); //type is success or error
}

async function fetch_login_json(data) {
    const response = await fetch(urlEndPoint, {
        method: "POST",
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            //"Access-Control-Allow-Origin": 'https://patpragman.github.io/swe_class_project'
        },
        body: JSON.stringify(data)
    })

    const res_promise = await response.json()
    return res_promise
}

async function login() {
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

    const res = await fetch_login_json(data)

    if (res["success"]) {
        console.log("passed")
        store_info(res["return_payload"], usernameInput.value, passwordInput.value)
        setLoginMessage(loginForm, "success", "Account Created!")
        window.location.href = "user.html";

    } else {
        console.log("failed")
        setLoginMessage(loginForm, "error", "Invalid username/password combination")
    }

}



function store_info(return_payload, username, password) {

    // store the login login info and the cards and open the html that contains the app

    window.sessionStorage.setItem("username", username);
    window.sessionStorage.setItem("password", password);
    window.sessionStorage.setItem("return_payload", JSON.stringify(return_payload));

}

async function createdNewUser() {
    const singupUsernameInput = document.getElementById("signupUsername")
    const signupPasswordInput = document.getElementById("signupPassword")
    const verifyPasswordInput = document.getElementById("verifyPassword")

    if (signupPasswordInput.value == verifyPasswordInput.value) {

        let user = {
            username: singupUsernameInput.value,
            password: signupPasswordInput.value
        }


        let data = {
            operation: "user",
            payload:
            {
                username: "no user",
                password: "na",
                object: user
            }
        };

        const res = await fetch_login_json(data)

        if (res["return_payload"]["success"]) {
            window.alert("account created!")
            store_info({}, singupUsernameInput.value, signupPasswordInput.value)
            setLoginMessage(createAccountForm, "success", "Account Created!")
            window.location.href = "user.html";

        } else {
            window.alert("There was an error somehow.")
        }
    } else {
        setLoginMessage(createAccountForm, "error", "Passwords do not match, Try again!")
        signupPasswordInput.focus();
        return false;
    }

}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#linkCreateAccount").addEventListener("click", e => {
        e.preventDefault(); // prevents redirect
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

        login()
    });

    createAccountForm.addEventListener("submit", e => {
        e.preventDefault();
        createdNewUser()
    })
});