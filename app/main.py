from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class ShopInfo(BaseModel):
    name: str
    location: str


class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: float


class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: list[Item]


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.post("/")
async def index(data: Data):
    return {"data": data}


@app.get("/countries/{country_name}")
async def country(country_name: str, country_no: int, city_name: Optional[str] = None):
    return {"country_name": country_name, "country_no": country_no}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


@app.post("/item")
async def create_item(item: Item) -> dict[str, str]:
    return {"message": f"{item.name}は税込み価格{item.price * item.tax}円になります。"}
