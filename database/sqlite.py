from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import datetime
import os

# db_url = f"sqlite:////{os.environ.get('DB_PATH','user_management')}.db"
db_url = "postgresql://postgres:password@localhost:5432/postgres"
sqlite_engine = create_engine(db_url)
session_obj = sessionmaker(bind=sqlite_engine)

# Define the Base class
Base = declarative_base()


# User model
class User(Base):
    __tablename__ = 'user_record'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(String, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# table creation
Base.metadata.create_all(sqlite_engine)


