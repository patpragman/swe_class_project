// retrieve thed global variables we'll work with while the app is running
let username = window.localStorage.getItem("username");
let password = window.localStorage.getItem("password");
let card_list = JSON.parse(window.localStorage.getItem("return_payload")).objects;
let card_index = 0;

// stuff from the DOM we need
const app_window = document.getElementById("application_div");
const current_card_div = document.getElementById("current_card");


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
    card_div.className = "content section_data";

    let title = document.createElement("h3");
    title.innerText = "Front!";

    let front_text_tag = document.createElement('h1');
    front_text_tag.className = "front_text";
    front_text_tag.innerText = o['front_text'];
    front_text_tag.style.display = "block";


    let back_text_tag = document.createElement('h1');
    back_text_tag.className = "back_text";
    back_text_tag.innerText = o['back_text'];
    back_text_tag.style.display = "none";

    card_div.appendChild(title);
    card_div.appendChild(front_text_tag);
    card_div.appendChild(back_text_tag);

    // handle the clicking

    card_div.onclick = function () {
        // swap the variables like this [a, b] = [b, a];
        [front_text_tag.style.display, back_text_tag.style.display] = [back_text_tag.style.display, front_text_tag.style.display];

        // swap the card title text
        if (title.innerText == "Front!") {
            title.innerText = "Back!";
        } else {
            title.innerText = "Front!";
        }

    };

    return card_div
}

function adjust_index_and_display(by){
    // adjust the card index variable we're using to display cards
    card_index = card_index + by;

    // logic so we don't try to access an item that's out of range
    if (card_index < 0) {
        card_index = card_list.length - 1
    } else if (card_index >= card_list.length){
        card_index = 0;
    }

    displayApplication();
}

function displayApplication(){
    let current_card_object = card_list[card_index];
    current_card_div.innerHTML = "";
    current_card_div.appendChild(cardFromObject(current_card_object))
}
