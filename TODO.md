# Things TODO

Things todo or ideas to implement
my thoughts on how to implement the project

## client

React app

- [x] Chat to ui mange with useChat store
- [x] Supabase Auth
  - [x] Login
  - [x] getAccessToken
- [x] Api layer to all outgoing requests
  - [x] JWT authorization headers
  - [x] send file to server | POST
  - [x] send message | POST params=[message, user_id,context]
  - [x] get All files | GET
- [ ] husky pre-commit hooks
- [x] UI components
  - [x] ChatMessage
  - [x] ChatInput
  - [x] uploading file type=[pdf]
  - [ ] file list
  - [ ] get file urls
  - [ ] download file
  - [ ] add a react-markdown for chat
- [x] Error handling / Error boundary
- [ ] Tests
  - [ ] Unit tests
  - [ ] Integration tests
- [x] Dockerfile
- [ ] Deployment

## server

Flask app

- [x] Project structure For flask
- [x] Requirement.txt
- [x] JWT validation
- [x] DB { supabase }
  - [x] profiles table
    - [x] user_id
    - [x] files [file_id]
    - [x] File block storage
- [ ] Message table | Not sure to implement this or not | it can be done in client local storage

- [x] Api layer
  - [x] send message | POST params=[message, file, user_id,context?] call Ollama | gpt model | any llm
  - [x] upload file | POST
  - [x] get All files | GET
  - [x] download file | GET
  - [x] delete file | DELETE
- [ ] logging
- [x] Dockerfile
- [ ] Tests
  - [ ] Unit tests
- [ ] Deployment

## LLM

llm's to implement

- [ ] OpenAI GPT | expensive not feasible.
- [ ] Ollama | llaVa vision model | difficult to deploy on any free service.
- [ ] llama | Most likely to implement provides $5 free credit.
- [ ] turn out llama can't keep the context by itself, need to implement that.
  - [x] works with context now
- [ ] see if llama can return the response as markdown | html

## overall

- [x] Documentation
- [x] README
- [x] docker-compose
- [ ] startup scripts
  - [ ] one for that requires to clone and .env file | ignore that
  - [ ] one for that requires to run docker-compose up in end run a startup script to create user and load data
- [x] Deployment
  - [ ] as a single flask that returns react build dist
  - or
  - [x] separate app for client and server
  - Note sure for now

## Auth Test

Email : <zafeer746@gmail.com>
Password : 123456
