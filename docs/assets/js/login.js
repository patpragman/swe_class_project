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
    }).then( data => {

        console.log("Request complete! response:");
        console.log(data);
        console.log(data['return_payload']);
        if (data['success']){
            displayApplication(data['return_payload']);
        }
        }
    );


}

function cardFromObject(o){

    /*
    Example flashcard object!

    {
	"0": {
		"owner": "patrick",
		"back_image_path": "None",
		"back_text": "test_card_back",
		"folder": "test / not import",
		"front_image_path": "None",
		"streak": "0",
		"id": 1,
		"front_text": "test_card_front",
		"create_date": "2022-11-21 01:12:11.247960",
		"last_study_date": "2022-11-22 01:12:11.247970",
		"next_study_due": "2022-11-26 01:12:11.247972"
	}
    }
    */

    // let's create a card
    let card_div = document.createElement("div");
    const id = o['id'];
    card_div.className = "flashcard";

    let title = document.createElement("h3");
    title.innerText = "Flashcard!";

    let front_text_tag = document.createElement('p');
    front_text_tag.className = "front_text";
    front_text_tag.innerText = o['front_text'];

    let back_text_tag = document.createElement('p');

    card_div.appendChild(title);
    card_div.appendChild(front_text_tag);
    card_div.appendChild(back_text_tag);

    return card_div
}


function displayApplication(res){
    const login_window = document.getElementById("login_container");
    login_window.innerHTML = "";

    for (o in res.return_payload){
        console.log(o);
        login_window.appendChild(cardFromObject(o));

    }
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