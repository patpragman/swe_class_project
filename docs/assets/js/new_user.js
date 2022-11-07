function create_new_user() {
    // get the following stuff from the dom
    // username, password, and the verify password input

    const user_name_block = document.getElementById("username");
    const password_block = document.getElementById("password")
    const verify_block = document.getElementById("verify_password")

    // post to this URL to trigger the api
    const url_endpoint = "https://c5j7g4oypbub6kqvkbdpmvhhra0njfgr.lambda-url.us-west-2.on.aws/"

    // validate that the username and password match
    if (password_block.value == verify_block.value){
        // if they match, try to make a new user!

        let user = {username: user_name_block.value,
                    passsword: password_block.value}

        let data = {operation: "create_user",
                    payload:
                        {username: "no user",
                        password: "na",
                        object: user
                        }
                  };

        // make a post request with the fetch method
        fetch(url_endpoint, {
          method: "POST",
            mode: 'cors',
          headers: {'Content-Type': 'application/json',
              "Access-Control-Allow-Origin": "*"
          },
          body: JSON.stringify(data)
        }).then(res => {
          console.log("Request complete! response:", res);
        });



    } else {
        alert("passwords don't match")
        password_block.focus()
    }
}