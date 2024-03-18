from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmarker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = 'sqlite:///./finance.db'

engine = create_engine(URL_DATABASE,  connect_args={"check_same_thread": False})

SessionLocal =  sessionmarker(autocommit=False, autoflush=False, bind=engine)

Base =  declarative_base()
