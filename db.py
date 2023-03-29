"""In this module the database is created and
the connection to the sqlite database is established here"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL is created below to use sqlite database and database is named as address_book
SQLALCHEMY_DATABASE_URL = "sqlite:///./address_book.db"


# A database engine is created and the argument
# connect_args={"check_same_thread": False} is only needed for sqlite database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# sessionmaker returns a SessionLocal class,
# this class is used as Session which will be imported from sqlalchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# The declarative_base() return the Base class
# This class will be inherited later to create database models.
Base = declarative_base()

