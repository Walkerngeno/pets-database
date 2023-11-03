import os
import dotenv
import sqlalchemy
class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:Walker@localhost:5432/pets"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
