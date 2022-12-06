const all_cards_container = document.getElementById("user_cards");
const addQuestion = all_cards_container.querySelector(".add-card");
const container = document.querySelector(".container");
const addQuestionCard = document.getElementById("add-question-card");
const cardButton = document.getElementById("save-btn");
const question = document.getElementById("question");
const answer = document.getElementById("answer");
const errorMessage = document.getElementById("error");
const closeBtn = document.getElementById("close-btn");
let editBool = false;

get_cards().forEach((card) => {
    const card_element = create_card_element(card.id, card.front_text);
    all_cards_container.insertBefore(card_element, addQuestion);
    card_element.addEventListener("click", () => {
        window.sessionStorage.setItem("current_card", card.id)
        window.location.href = "app.html";
    })
});

addQuestion.addEventListener("click", () => addCard());


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

////////// Add Flashcard pop up window /////////////

//Add question when user clicks 'Add Flashcard' button
addQuestion.addEventListener("click", () => {
    container.classList.add("hide");
    question.value = "";
    answer.value = "";
    addQuestionCard.classList.remove("hide");
});

//Hide Create flashcard Card
closeBtn.addEventListener(
    "click",
    (hideQuestion = () => {
        container.classList.remove("hide");
        addQuestionCard.classList.add("hide");
        if (editBool) {
            editBool = false;
            submitQuestion();
        }
    })
);

//Submit Question
cardButton.addEventListener(
    "click",
    (submitQuestion = () => {
        editBool = false;
        // tempQuestion = question.value.trim();
        // tempAnswer = answer.value.trim();
        if (!tempQuestion || !tempAnswer) {
            errorMessage.classList.remove("hide");
        } else {
            // viewlist();

        }
    })
);

