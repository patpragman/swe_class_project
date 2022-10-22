# Sequence Diagrams

## JSON Sequence Diagrams

```mermaid

sequenceDiagram
    participant A as  Client
    participant B as lambda_handler(event)
    participant C as authenticate(payload, operation)
    participant D as Execute Operation

    A->>+B: JSON to AWS Lambda
    B->>-A: Invalid JSON or Error
    B->>+C: Username, Password, Payload
    C->>A: Error 500
    C->>-A: Bad Username or Password

    D->>A:  Error 500 on server Error
    D->>A:  Error that didn't break everything, send a 200 Code, but an explanation of the error
    D->>A:  Success!  Send status code 200, and any data that comes back
```

##  Acceptable JSON Payloads

### Why

This document lays out what the JSON to and from the server should look like

### Create A Flashcard JSON Payload
````JSON

{
    "operation": "create_flashcard",
    "payload":
        {"username": "patrick",
         "password": "pass_test",
         "object": <-a dictionary describing a flashcard object->
         }
}

````
### Flow of JSON as class diagram

```mermaid
 classDiagram
    class FlashCard{
        owner
        folder
        front_text
        back_text
        streak
        create_date
        last_study_date
        front_image_path
        back_image_path
        dict()
    }

    class User{
        username
        password
        ...?
        dict()
    }

    class payload{
        username
        password
        object
    }

    class json_from_client{
        operation
        payload
    }

    class AWS{
        lambda_handler()
    }

    class operation_router{
        create(payload)
        read(payload)
        update(payload)
        delete(payload)
    }

    class ReturnPayload{
        message
        object
    }

    class ResponseBody{
        success
        return_payload
    }

    class Response{
        statusCode
        ResponseBody
    }


    FlashCard --> payload
    User --> payload
    payload --> json_from_client

    json_from_client --> AWS

    AWS --> operation_router

    operation_router --> ReturnPayload

    ReturnPayload --> ResponseBody

    ResponseBody --> Response

```

### How does this translate to JSON

#### Example JSON of a "object" in a JSON payload

##### Flashcard
```json
{
    "owner": "patrick", 
    "folder": "test / not import", 
    "front_text": "test_card_front", 
    "back_text": "test_card_back", 
    "streak": "0", 
    "create_date": "2022-10-16 17:03:15.074063", 
    "last_study_date": "2022-10-17 17:03:15.074074", 
    "next_study_due": "2022-10-21 17:03:15.074075", 
    "front_image_path": "None", 
    "back_image_path": "None"
}
```

##### User
Presumably we'd want to encrypt on the front end before we even sent this object
to the backend, but here's what one would look like
```json
{"username": "patrick", 
  "password": "pass_test"}
```

##### return_payload for a create flashcard
```json
{"message":"user saved!"}
```
##### return_payload for a create user
```json
{"message":"flashcard saved!"}
```

### Retrieve Operations

what you get when fetching all user cards
```json
{
  "message": "fetched the following cards for <username>",
  "objects": [list of cards]
}
```

