from typing import Optional

from fastapi import FastAPI
from random import Random
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

class AreaOfCircle(BaseModel):
    r: float

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/index")
def index():
    html_content = """
    <DOCTYPE! html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>こんにちは！</title>
            p#ehehe{
                background-color: #ffffff;
                color: #000000;
                font-size: 1.5rem;
            }
        </head>
        <body>
        <p>
            <h1>うおおおお！WEBAPI!WEBAPI!</h1>
        </p>
        <p id="ehehe">
            みってるぅ～？（笑）
        </p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

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
    return {"result":omikron_list[random_number.randint(0,7)]}

@app.post("/areaOfCircle/")
async def calcAreaOfCircle(circle: AreaOfCircle):
    area = circle.r ** 2 * 3.1415
    return {"radius": circle.r, "area": area}