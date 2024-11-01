from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text

class Customers(Base) :
    __tablename__ = 'customers'
    customer_id   = Column( Integer,primary_key=True, index=True )
    customer_name = Column(String,nullable=False)
    contact_name  = Column(String,nullable=False)