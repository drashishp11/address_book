"""Here, we initiate our models or crete initial pydantic models.
The UserBase is created as a pydantic model and remaining models
are inherited from them, so that other models will also have have
same attributes as UserBase

These pydantic models are used for reading the data.
"""

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    address_lattitude : float
    address_longitude : float


class UserCreate(UserBase):
    email: str
    address_lattitude: float
    address_longitude: float
    is_active: bool
    # The behavior of pydantic can be controlled via config class
    # The orm_mode = True, will tell the pydantic model to
    # read the data even if it is not in the form of dictionary
    class Config:
        orm_mode = True   # This also enable compatibility for ORM


class User(UserCreate):
    id: int

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    email: str
    address_lattitude: float
    address_longitude: float

    class Config:
        orm_mode = True
