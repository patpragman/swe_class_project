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

//save a note to the local storage -> need to somehow send to lambda
function save_cards(notes) {
    localStorage.setItem("payload_return", JSON.stringify(cards));
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

function add_card() {

    const cards = get_cards();
    const card_object = {
        id: Math.floor(Math.random() * 100000),
        content: ""
    };

    const card_element = create_card_element(card_object.id, card_object.front_text);
    all_cards_container.insertBefore(card_element, add_card_button);

    cards.push(card_object);
    save_cards(cards);
}

function updateNote(id, newContent) {
    const notes = getNotes();
    const targetNote = notes.filter((note) => note.id == id)[0];

    targetNote.content = newContent;
    saveNotes(notes);
}

function deleteNote(id, element) {
    const notes = getNotes().filter((note) => note.id != id);

    saveNotes(notes);
    notesContainer.removeChild(element);
}
