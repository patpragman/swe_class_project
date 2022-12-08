const urlEndPoint = "https://c5j7g4oypbub6kqvkbdpmvhhra0njfgr.lambda-url.us-west-2.on.aws/"
let username = window.sessionStorage.getItem("username");
let password = window.sessionStorage.getItem("password");

const all_cards_container = document.getElementById("user_cards");
const add_card_button = all_cards_container.querySelector(".add-card");


get_cards()

add_card_button.addEventListener("click", () => {
    add_card();
});


//get array of cards stored in local storage
function get_cards() {
    cards = JSON.parse(sessionStorage.getItem("return_payload")).objects
    if (cards == undefined) {
        cards = JSON.parse(sessionStorage.getItem("return_payload"))
    }

    cards.forEach((card) => {
        const card_element = create_card_element(card.id, card.front_text);
        all_cards_container.insertBefore(card_element, add_card_button);
        card_element.addEventListener("click", () => {
            window.sessionStorage.setItem("current_card", card.id)
            window.location.href = "app.html";
        })
    })

}

//create new card html --> moving to another page?
function create_card_element(id, front_text) {


    const element = document.createElement("textarea");
    element.readOnly = true

    // add styling
    element.classList.add("card");
    element.value = front_text;
    element.placeholder = "Empty Flashcard";

    return element;
}

// still needs some work
function add_card() {

    let new_card = {
        "owner": username,
        "folder": "test / not import",
        "front_text": "Here is your new card, click to edit",
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
            object: new_card
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

        let id = data['return_payload']["id"];
        new_card['id'] = id;

        new_payload = {
            object: new_card
        }
        window.sessionStorage.setItem("return_payload", JSON.stringify(new_payload));
        console.log(JSON.parse(sessionStorage.getItem("return_payload")))
        get_cards()

    });
} 