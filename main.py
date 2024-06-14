from typing import Optional

from fastapi import FastAPI
from random import Random
from pydantic import BaseModel

class AreaOfCircle(BaseModel):
    r: float

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    random_number = Random()
    omikron_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "末吉",
        "凶",
        "小凶",
        "大凶",
    ]
    return omikron_list[random_number.randint(0,7)]

@app.post("/areaOfCircle/")
async def calcAreaOfCircle(circle: AreaOfCircle):
    area = circle.r ** 2 * 3.1415
    return {"radius": circle.r, "area": area}