from dotenv import load_dotenv
import os


POSTGRESQL=os.getenv("POSTGRESQL")


class Config:
    DEBUG= True
    SECRET_KEY='dev'

    SQLALCHEMY_DATABASE_URI=POSTGRESQL
 