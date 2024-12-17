from typing import Union

from fastapi import FastAPI
# BaseModel from Pydantic is used to define data objects.
from pydantic import BaseModel


# Declare the data object with its components and their type.
class TaggedItem(BaseModel):
    name: str
    tags: Union[str, list]
    item_id: int


# Instantiate the app.
app = FastAPI()

# Define a GET on the specified endpoint.
@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}


@app.post("/items/")
async def create_item(item: TaggedItem):
    return item


# A GET that in this case just returns the item_id we pass,
# but a future iteration may link the item_id here to the one we defined in our TaggedItem.
@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}

@app.post("/elements/{path}/")
async def exercise_function(path: int, query: int, body: TaggedItem):
    return {"path": path, "query": query, "body": body}