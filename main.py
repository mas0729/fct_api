import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    mail: Optional[str] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/user/")
def create_user(user: User):
    print(user)
    return {"status": "OK", "name": user.name, "age": user.age}


if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)

