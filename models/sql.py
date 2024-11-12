from sqlalchemy import create_engine, Column, Integer, String, Float, Double, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

DATABASE_URL = "mysql+pymysql://root:1234@192.168.11.20:3306/logestic"

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=0,
    pool_recycle=3600
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(255))
    length = Column(Float)
    width = Column(Float)
    heigth = Column(Float)
    weigth = Column(Float)
    destination = Column(Integer)
    price_truck = Column(Double)
    occupied_weight = Column(Float)
    occupied_volume = Column(Float)

class Cars(Base):
    __tablename__ = "Cars"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    truck_type = Column(Integer)
    due_date = Column(Date)
    total_income = Column(Double)
    V_capacity = Column(Float)
    W_capacity = Column(Float)
