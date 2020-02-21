from sqlalchemy.orm import sessionmaker, backref, relationship
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from .set_secrets import _set_secret

Base = declarative_base()
db_string = _set_secret("db_con_string")
engine = db.create_engine(db_string)

Base.metadata.bind = engine

# DB Session instance to access decalartives (created tables, classes etc)
# DB Session establishes a connection with the database
DBSession = sessionmaker(bind=engine)
session = DBSession()
