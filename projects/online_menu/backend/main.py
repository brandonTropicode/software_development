from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

menu_items = [
    # {    
    #     'id': 1,
    #     'name': 'Burger',
    #     'description': 'Tasty burger',
    #     'price': 67.00, -> float
    #     'category': 'main', 'soups', 'sides'
    # },
]

# user order is in memory
order = []

class UserOrder(BaseModel):
    item_id: int

class MenuItem(BaseModel):
    name:str
    description:str
    price:float
    category:str

# home route
@app.get("/")
def home():
    return {
        "message":"Welcome to crystal caverns, have a look through our menu!"
    }

@app.get("/menu")
def get_menu():
    return menu_items

@app.post("/order/add")
def add_to_order(user_item:UserOrder):
    item_id = user_item.item_id
    for item in menu_items:
        # check if current item's id == item_id
        if item["id"] == item_id:
            order.append(item)
            return {
                "message":"Your item has been added to your order",
                "item":item
            }
    return {
        "message":"Item not found"
    }

@app.delete("/order/delete")
def reset_order():
    order.clear()
    return {
        "message":"Order clear"
    }

@app.get("/order/total")
def get_total():
    total = 0
    # order = [{'price':x}, {'price':y}, {'price':z}]
    for item in order:
        total += item["price"]
    return {
        "items":order,
        "total":round(total,2)
    }

@app.post("/menu/add")
def add_to_menu(item:MenuItem):
    new_item = {
        "id":len(menu_items)+1,
        "name":item.name,
        "description":item.description,
        "price":item.price,
        "catagory":item.category
        }
    menu_items.append(new_item)
    return {
        "message":"New item added to menu",
        "item":new_item
    }
@app.delete("/menu/item/delete/{item_id}")
def delete_from_menu(item_id:int):
    for item in menu_items:
        # check if current item's id == item_id
        if item["id"] == item_id:
            menu_items.remove(item)
            return {
                "message":"Your item has been deleted from the menu",
                "item":item
            }
    return {
        "message":"Item not found"
    }


# uvicorn main:app --reload