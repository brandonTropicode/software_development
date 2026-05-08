from fastapi import FastAPI
from schemas import NumInput

# our server
bob_server = FastAPI()

# routes = endpoints of a website
# methods: GET, POST
# GET -> getting info and displaying to user
# POST -> creating data and storing it and display to user
@bob_server.get('/')
@bob_server.get('/home')
def home():
    return {
        'calculator':'basicly chatgpt'
    }

# add route
@bob_server.post('/add')
def add(data:NumInput):
    sum = data.num1 + data.num2
    return {
        "opperation":"add",
        "result":sum
    }

# subtract route
@bob_server.post('/subtract')
def subtract():
    pass
    
# multiply route
@bob_server.post('/multiply')
def multiply():
    pass

# divide route
@bob_server.post('/divide')
def divide():
    pass

# command to run your server
# uvicorn website:bob_server --reload