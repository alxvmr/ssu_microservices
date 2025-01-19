from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
db_name = os.getenv('DB_NAME')
db_passwd = os.getenv('DB_PASSWD')

Base = declarative_base()

class OutboxMessage(Base):
    __tablename__ = 'outbox_messages'
    
    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

DATABASE_URL = f"postgresql://{db_name}:{db_passwd}@localhost/microservices"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)