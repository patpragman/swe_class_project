const all_cards_container = document.getElementById("user_cards");
const add_card_button = all_cards_container.querySelector(".add-card");

get_cards().forEach((card) => {
    const card_element = create_card_element(card.id, card.front_text);
    all_cards_container.insertBefore(card_element, add_card_button);
    card_element.addEventListener("click", () => {
        window.sessionStorage.setItem("current_card", card.id)
        window.location.href = "app.html";
    })
});

add_card_button.addEventListener("click", () => addCard());


//get array of cards stored in local storage
function get_cards() {
    return JSON.parse(sessionStorage.getItem("return_payload")).objects;
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
