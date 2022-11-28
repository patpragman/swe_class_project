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


function displayApplication(){

    // retrieve the
    let username = window.localStorage.getItem("username");
    let password = window.localStorage.getItem("password");
    let return_payload = JSON.parse(window.localStorage.getItem("return_payload"));

    console.log('testing:');



    const app_window = document.getElementById("application_div");
    // app_window.className = "container";
    app_window.innerHTML = "";


    // need to build some of the UI elements

    // need a create flashcard button

    // need a remove flashcard button

    // need an update flashcard button



    // load the flashcards
    for (const o of return_payload.objects){
        console.log(o);
        login_window.appendChild(cardFromObject(o));

    }
}
