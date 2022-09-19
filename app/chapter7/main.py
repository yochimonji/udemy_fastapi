from fastapi import FastAPI

from .sql_app import schemas

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Success"}


@app.post("/users")
async def users(users: schemas.User):
    return {"users": users}


@app.post("/rooms")
async def rooms(rooms: schemas.Room):
    return {"rooms": rooms}


@app.post("/bookings")
async def bookings(bookings: schemas.Booking):
    return {"bookings": bookings}
