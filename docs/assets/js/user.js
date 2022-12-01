// const all_cards_container = document.getElementById("user_cards");
// const add_card_button = all_cards_container.querySelector(".add-card");

// get_cards().forEach((card) => {
//     const card_element = create_card_element(card.id, card.front_text);
//     all_cards_container.insertBefore(card_element, add_card_button);
//     card_element.addEventListener("click", () => {
//         window.sessionStorage.setItem("current_card", card.id)
//         window.location.href = "app.html";
//     })
// });

// add_card_button.addEventListener("click", () => addCard());


// //get array of cards stored in local storage
// function get_cards() {
//     return JSON.parse(sessionStorage.getItem("return_payload")).objects;
// }

// //create new card html --> moving to another page?
// function create_card_element(id, front_text) {


//     const element = document.createElement("textarea");
//     element.readOnly = true

//     // add styling
//     element.classList.add("card");
//     element.value = front_text;
//     element.placeholder = "Empty Flashcard";

//     return element;
// }

////////// Add Flashcard pop up window /////////////
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
        tempQuestion = question.value.trim();
        tempAnswer = answer.value.trim();
        if (!tempQuestion || !tempAnswer) {
            errorMessage.classList.remove("hide");
        } else {
            container.classList.remove("hide");
            errorMessage.classList.add("hide");
            viewlist();
            question.value = "";
            answer.value = "";
        }
    })
);

//Card Generate
function viewlist() {
    var listCard = document.getElementsByClassName("card-list-container");
    var div = document.createElement("div");
    div.classList.add("card");
    //Question
    div.innerHTML += `
    <p class="question-div">${question.value}</p>`;
    //Answer
    var displayAnswer = document.createElement("p");
    displayAnswer.classList.add("answer-div", "hide");
    displayAnswer.innerText = answer.value;

    //Link to show/hide answer
    var link = document.createElement("a");
    link.setAttribute("href", "#");
    link.setAttribute("class", "show-hide-btn");
    link.innerHTML = "Show/Hide";
    link.addEventListener("click", () => {
        displayAnswer.classList.toggle("hide");
    });

    div.appendChild(link);
    div.appendChild(displayAnswer);

    //Edit button
    let buttonsCon = document.createElement("div");
    buttonsCon.classList.add("buttons-con");
    var editButton = document.createElement("button");
    editButton.setAttribute("class", "edit");
    editButton.innerHTML = `<i class="fa-solid fa-pen-to-square"></i>`;
    editButton.addEventListener("click", () => {
        editBool = true;
        modifyElement(editButton, true);
        addQuestionCard.classList.remove("hide");
    });
    buttonsCon.appendChild(editButton);
    disableButtons(false);

    //Delete Button
    var deleteButton = document.createElement("button");
    deleteButton.setAttribute("class", "delete");
    deleteButton.innerHTML = `<i class="fa-solid fa-trash-can"></i>`;
    deleteButton.addEventListener("click", () => {
        modifyElement(deleteButton);
    });
    buttonsCon.appendChild(deleteButton);

    div.appendChild(buttonsCon);
    listCard[0].appendChild(div);
    hideQuestion();
}

//Modify Elements
const modifyElement = (element, edit = false) => {
    let parentDiv = element.parentElement.parentElement;
    let parentQuestion = parentDiv.querySelector(".question-div").innerText;
    if (edit) {
        let parentAns = parentDiv.querySelector(".answer-div").innerText;
        answer.value = parentAns;
        question.value = parentQuestion;
        disableButtons(true);
    }
    parentDiv.remove();
};

//Disable edit and delete buttons
const disableButtons = (value) => {
    let editButtons = document.getElementsByClassName("edit");
    Array.from(editButtons).forEach((element) => {
        element.disabled = value;
    });
};
