import json

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_post_item():
    body = {"name": "shirt", "description": "g", "price": 1000, "tax": 1.1}
    res = client.post("/item", json.dumps(body))
    assert res.status_code == 200
    assert res.json() == {"message": f"{body['name']}は税込み価格{body['price'] * body['tax']}円になります。"}


if __name__ == "__main__":
    test_post_item()
