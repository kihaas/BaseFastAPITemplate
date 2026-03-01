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

from fastapi import FastAPI, Depends, HTTPException, Body, Path
from pydantic import BaseModel, EmailStr

import uvicorn
app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr
@app.get("/")
def hello():
    return {
        "message": "Hello World!"
    }


@app.get("/hello")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"hello,{name}"}


@app.post("/users")
def create_user(email: EmailStr = Body):
    return{
        "message": "success",
        "email": email,
    }

@app.get("/calc")
def calculator(a: float, b:float):
    return{
        "a": a,
        "b": b,
        "result": a+b,
    }


@app.get("/items")
def list_items():
    return [
        "item1",
        "item2",
    ]


@app.get("/items/{item_id}")
def get_item_by_id(item_id: int = Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item":{
            "id":item_id,
        },
    }


@app.get("/item/latest")
def get_latest_item():
    return {"item": {"id": "0", "name": "Latest"}}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)





















