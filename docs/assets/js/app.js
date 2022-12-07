const urlEndPoint = "https://c5j7g4oypbub6kqvkbdpmvhhra0njfgr.lambda-url.us-west-2.on.aws/"

// retrieve thed global variables we'll work with while the app is running
let username = window.sessionStorage.getItem("username");
let password = window.sessionStorage.getItem("password");
let card_list = JSON.parse(window.sessionStorage.getItem("return_payload")).objects;
let card_id = window.sessionStorage.getItem("current_card");
let viewed = 0 //num of seen cards
let current_card_object = ""

// stuff from the DOM we need
const app_window = document.getElementById("application_div");
const app_buttons = document.getElementById("app_buttons")
const add_card_button = app_buttons.querySelector("#add_card")
const prev_button = app_window.querySelector("#previous_card")
const next_button = app_window.querySelector("#next_card")
const edit_button = app_buttons.querySelector("#edit_card")

card_list = shuffleCards(card_list)
display_specific_card()

//shuffle the cards
function shuffleCards(arr) {
    // set the current object to be card with given id
    current_card_object = card_list.filter((card_obj) => card_obj.id == card_id)[0]

    // remove that card from the deck and shuffle deck
    const i = arr.indexOf(current_card_object)
    const x = arr.splice(i, 1)
    arr.sort(() => Math.random() - 0.5)

    // add the current card back in at the top of the deck
    arr.push(current_card_object)

    return arr
}

//display
function display_specific_card() {
    // display the card at the top of the deck
    current_card_object = card_list[card_list.length - 1]

    // create the html for a new card
    let old_object = prev_button.nextElementSibling
    current_elem = create_card_element(current_card_object)
    if (old_object != next_button) {
        app_window.replaceChild(current_elem, old_object)
    } else {
        app_window.insertBefore(current_elem, next_button)
    }
}

//create the flashcard
function create_card_element(obj) {
    const card_box = document.createElement("div");
    const question = document.createElement('h2')
    const answer = document.createElement("h2")


    //const id = obj['id'];
    card_box.classList.add("current_card")

    question.setAttribute("style", "display:block")
    question.id = "q"
    question.textContent = obj['front_text']

    answer.setAttribute("style", "display:none")
    answer.id = "a"
    answer.textContent = obj["back_text"]


    card_box.appendChild(question)
    card_box.appendChild(answer)

    card_box.onclick = function () {
        [question.style.display, answer.style.display] = [answer.style.display, question.style.display]
    }


    return card_box
}

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

// NOT FINISHED, STILL  NEED TO GET THE INPUT FROM TEXT BOXES
function update_card() {
    // get the q/a text
    const ans = document.getElementById("a")
    const qst = document.getElementById("q")

    //make sure they're viewable
    qst.setAttribute("style", "display:block")
    ans.setAttribute("style", "display:block")

    //add input boxes under q/a text
    const answer_input_box = document.createElement("input")
    answer_input_box.id = "answer"
    answer_input_box.placeholder = "New Answer"
    const question_input_box = document.createElement("input")
    question_input_box.id = "question"
    question_input_box.placeholder = "New Question"
    const confirmation_button = document.createElement("button")
    confirmation_button.textContent = "Ok"


    ans.after(answer_input_box)
    qst.after(question_input_box)
    answer_input_box.after(confirmation_button)

    confirmation_button.addEventListener("click", () => {
        // update the current object text
        current_card_object["front_text"] = question_input_box.value
        current_card_object["back_text"] = answer_input_box.value
        console.log(current_card_object["front_text"], current_card_object["back_text"])


        let data = {
            operation: "update_card",
            payload: {
                username: username,
                password: password,
                id: current_card_object["id"],
                object: JSON.stringify(current_card_object)
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
            window.sessionStorage.setItem('return_payload', JSON.stringify(card_list));
        });


        display_specific_card()


    })
}

function send_out(data) {



}


function  add_card(){

    let new_card = {
    "owner": username,
    "folder": "test / not import",
    "front_text" : "new card front!",
    "back_text": "new card back",
    "streak": 0,
    "create_date": "not implemented",
    "last_study_date": "not implemented",
    "next_study_due": "not implemented"
    };


    let data = {
            operation: "create_flashcard",
            payload: {
                username: username,
                password: password,
                object: JSON.stringify(new_card)
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
            let id = data['id'];
            new_card['id'] = id;

            card_list.push(new_card);
            display_specific_card();
            update_card();
        });

}



document.addEventListener("DOMContentLoaded", () => {
    //button behavior
    //new_card_button.addEventListener("click", () => add_card)
    prev_button.addEventListener("click", function () {
        if (viewed == 0) {
            window.alert("This is the first viewed card today")
        } else {
            // remove the card on bottom of deck and move to the top
            let p_card = card_list.shift()
            card_list.push(p_card)
            display_specific_card()
            viewed = viewed - 1
        }

    })

    //displays a random unseen card or sends alert
    next_button.addEventListener("click", function () {
        if (viewed == card_list.length) {
            window.alert("Congrats. You've reviewed all of your cards.")
        } else {
            // move the current card to the bottom of the deck
            card_list.pop()
            card_list.unshift(current_card_object)
            display_specific_card()
            viewed = viewed + 1
        }


    })

    edit_button.addEventListener("click", update_card)

    add_card_button.addEventListener("click", add_card)


})
