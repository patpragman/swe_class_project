const urlEndPoint = "https://c5j7g4oypbub6kqvkbdpmvhhra0njfgr.lambda-url.us-west-2.on.aws/"


function setLoginMessage(element, type, message) {
    const loginMessage = element.querySelector(".login__message");

    loginMessage.textContent = message;
    loginMessage.classList.remove("login__message--success", "login__message--error"); //get rid of current style
    loginMessage.classList.add(`login__message--${type}`); //type is success or error
}

function setInputError(inputElement, message) {
    inputElement.classList.add("login__input--error");
    inputElement.parentElement.querySelector(".login__input-errorMsg").textContent = message;
}

function clearInputError(inputElement) {
    inputElement.classList.remove("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = "";
}

function login() {
    const usernameInput = document.getElementById("username")
    const passwordInput = document.getElementById("password")

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

        /*  fetch(urlEndPoint, {
              method: "POST",
                mode: 'cors',
              headers: {'Content-Type': 'application/json',
                  "Access-Control-Allow-Origin": "*"
              },
              body: JSON.stringify(data)
            }).then(res => {
              console.log("Request complete! response:", res);
            }); */

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

        // Perform your AJAX/Fetch login
        console.log(usernameInput.value, passwordInput.value)

        setLoginMessage(loginForm, "error", "Invalid username/password combination");
    });

    createAccountForm.addEventListener("submit", e => {
        e.preventDefault();
        if (createdNewUser() == false) {
            setLoginMessage(createAccountForm, "error", "Passwords do not match, Try again!")

        } else {
            setLoginMessage(createAccountForm, "success", "Account Created!")
        }

    })

    document.querySelectorAll(".form__input").forEach(inputElement => {
        inputElement.addEventListener("blur", e => {
            if (e.target.id === "signupUsername" && e.target.value.length > 0 && e.target.value.length < 10) {
                setInputError(inputElement, "Username must be at least 10 characters in length");
            }
        });

        inputElement.addEventListener("input", e => {
            clearInputError(inputElement);
        });
    });
});