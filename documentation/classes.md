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

### What a card object looks like

```
{
   
}
```
