from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import base
database_url = "sqlite:///chocolate_house.db"
engine = create_engine(database_url)
localsession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base.metadata.create_all(bind=engine)
def get_db():
    db = localsession()
    try:
        yield db
    finally:
        db.close()
