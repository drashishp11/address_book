"""
Here, we define reusable functions to interact
with database to perform CRUD operations on address book.
The Session allows to declare type of database (db)
"""
from sqlalchemy.orm import Session
import models, schemas


def get_user(db: Session, user_id: int):
    #This function returns the user details from ID
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    # This function returns the user details from email
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_address(db: Session, address_lattitude: float, address_longitude: float):
    # This function returns the user details from the coordinates of the address
    return db.query(models.User).filter(models.User.address_lattitude == address_lattitude and
                                        models.User.address_longitude == address_longitude).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    # This function returns all the users details available in database
   return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    # This function creates a new user
    db_user = models.User(email=user.email, address_lattitude = user.address_lattitude,
                          address_longitude = user.address_longitude)
    db.add(db_user)  # add db_user in database
    db.commit()   #Commit the changes in database
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, details: schemas.UserUpdate):
    #This function updates all the users
    db.query(models.User).filter(models.User.id == user_id).update(vars(details))
    db.commit()
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user_and_address(db: Session, user_id: int):
    # This function is used to delete the user and address
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return {"message": "User and address deleted successfully"}

