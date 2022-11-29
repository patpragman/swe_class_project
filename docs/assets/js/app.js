// retrieve thed global variables we'll work with while the app is running
let username = window.sessionStorage.getItem("username");
let password = window.sessionStorage.getItem("password");
let card_list = JSON.parse(window.sessionStorage.getItem("return_payload")).objects;
let card_id = window.sessionStorage.getItem("current_card");
let viewed = []
let current_card_object = ""

// stuff from the DOM we need
const app_window = document.getElementById("application_div");
const new_card_button = app_window.querySelector("#add_card")
const prev_button = app_window.querySelector("#previous_card")
const next_button = app_window.querySelector("#next_card")
const edit_button = document.getElementById("#edit_card")

display_specific_card(card_id)

//button behavior
//new_card_button.addEventListener("click", () => add_card)
prev_button.addEventListener("click", function () {
    i = viewed.indexOf(current_card_object["id"]) - 1
    display_specific_card(viewed.at(i))
})

next_button.addEventListener("click", function () {
    if (card_list.length > 0) {
        i = Math.floor(Math.random() * card_list.length)
        display_specific_card(card_list[i]["id"])
    } else {
        window.alert("Congrats. You've reviewed all your cards.")
        window.location.href = "user.html";

    }


})

edit_button.addEventListener("click", update_card)

//display
function display_specific_card(id) {
    //add to viewed cards
    current_card_object = card_list.filter((card_obj) => card_obj.id == id)[0]
    viewed.push(current_card_object["id"])

    //remove from unseen cards
    card_list = card_list.filter(card_obj => card_obj !== current_card_object)



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

function adjust_index_and_display(a) {
    // adjust the card index variable we're using to display cards
    card_id = card_id + a

    // logic so we don't try to access an item that's out of range
    if (card_id < 0) {
        card_id = card_list.length - 1
    } else if (card_id >= card_list.length) {
        card_id = 0;
    }

    display_specific_card()
}

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
    const question_input_box = document.createElement("input")
    question_input_box.id = "question"

    ans.after(answer_input_box)
    qst.after(question_input_box)

    // update the current object text
    current_card_object["front_text"] = question_input_box.value
    current_card_object["back_text"] = answer_input_box.value

    let data = {
        operation: "update_card",
        payload: {
            username: username,
            id: card_id,
            object: current_card_object
        }
    }

    console.log(data)

}
