from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///data/database.db')

Session = sessionmaker(bind=engine)
session = Session()
