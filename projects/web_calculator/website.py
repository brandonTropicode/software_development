from fastapi import FastAPI, HTTPException
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
        "operation":"add",
        "result":sum
    }

# subtract route
@bob_server.post('/subtract')
def subtract(data:NumInput):
    difference = data.num1 - data.num2
    return {
        "operation":"subtract",
        "result":difference
    }
    
# multiply route
@bob_server.post('/multiply')
def multiply(data:NumInput):
    product = data.num1 * data.num2
    return {
        "operation":"multiply",
        "result":product
    }

# divide route
@bob_server.post('/divide')
def divide(data:NumInput):
    if data.num2 == 0:
        #when user error code 400/when system error 500
        raise HTTPException(status_code = 400,detail = "Stop dividing by 0 por favor")
    quotiont = data.num1/data.num2
    return {
        "operation":"divide",
        "result":quotiont
    }

# command to run your server
# uvicorn website:bob_server --reload