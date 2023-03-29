"""This is the main address_book app which is created using fastapi"""

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from db import SessionLocal, engine

# A metadata is created using database engine
models.Base.metadata.create_all(bind=engine)

# The app is initiated
app = FastAPI()


def get_db():
    # database dependency is created using the SessionLocal
    # created in db.py.
    # Throughout all the requests same session is used
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Returns all the users present in databse
   users = crud.get_users(db, skip=skip, limit=limit)
   return users


@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    # Returns the user details for the particular user_id
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Creates new user
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)



@app.put("/update/{user_id}", response_model=schemas.User)
def update_user(user_id: int, update_param: schemas.UserUpdate,db: Session = Depends(get_db)):
    # Updates the user
    db_user = crud.get_user(db, user_id=user_id)
    #db_user = json.loads(str(db_user))
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.commit()
    db.refresh(db_user)
    return crud.update_user(db=db, details=update_param, user_id=user_id)


@app.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    # deletes the user
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    try:
        crud.delete_user_and_address(db, user_id=user_id)
    except Exception as e:
        raise   HTTPException(status_code=400, detail=f"Unable to delete : {e}")

    return {"message": "User and address deleted successfully"}
