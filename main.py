# import uvicorn
# from fastapi import FastAPI
# from pydantic import EmailStr, BaseModel
# app = FastAPI()
#
#
# class CreateUser(BaseModel):
#     email: EmailStr
# @app.get("/")
#
# def say_hello():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/")
# def hello(name: str = "World"):
#     name = name.strip().title()
#     return {"message": f"Hello {name} !"}
#
#
# @app.post("/users/")
# def create_user(user: CreateUser):
#     return {
#         "message" : "success",
#         "email": user.email,
#     }
#
# @app.post("/calc/add/")
# def add(a: int, b: int):
#     return{
#         "a": a,
#         "b": b,
#         "result": a + b
#     }
#
#
# @app.get("/items/")
# def list_items():
#     return [
#         "item1",
#         "item2"
#     ]
#
#
# @app.get("/items/latest/")
# def get_latest_item():
#     return{"item":{"id": "0", "name": "latest"}}
#
#
# @app.get("/items/{item_id}/")
# def get_item_by_id(item_id: int):
#     return {
#         "item_id": {
#             "id": item_id,
#         },
#     }
#
#
# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)

from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel, EmailStr

import uvicorn

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello():
    return {"message": "Hello World!"}


@app.get("/hello")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"hello,{name}"}


@app.get("/calc")
def calculator(a: float, b: float):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
