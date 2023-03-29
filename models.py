"""Here, we will create tables and objects of required models.
 This project is for developing an address book, an user object
 is created with different parameters under the user class
 """


from sqlalchemy import Boolean, Column, Integer, String, Float
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    address_lattitude = Column(Float, index=True, nullable=False)
    address_longitude = Column(Float, index=True, nullable=False)





