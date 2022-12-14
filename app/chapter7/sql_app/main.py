# poetry run uvicorn app.chapter7.sql_app.main:app --host 0.0.0.0 --port 9000 --reload

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/")
# async def index():
#     return {"message": "Success"}

# Read
@app.get("/users", response_model=list[schemas.User])
async def reade_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/rooms", response_model=list[schemas.Room])
async def reade_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return rooms


@app.get("/bookings", response_model=list[schemas.Booking])
async def reade_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return bookings


# Create
@app.post("/users", response_model=schemas.User)
async def create_users(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user)


@app.post("/rooms", response_model=schemas.Room)
async def create_rooms(room: schemas.Room, db: Session = Depends(get_db)):
    return crud.create_room(db, room=room)


@app.post("/bookings", response_model=schemas.Booking)
async def create_bookings(booking: schemas.Booking, db: Session = Depends(get_db)):
    return crud.create_booking(db, booking=booking)
