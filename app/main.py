from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: float


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/countries/{country_name}")
async def country(country_name: str, country_no: int, city_name: Optional[str] = None):
    return {"country_name": country_name, "country_no": country_no}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


@app.post("/item/")
async def create_item(item: Item):

    return {"message": f"{item.name}は税込み価格{item.price * item.tax}円になります。"}
