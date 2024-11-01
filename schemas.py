from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel) :
    customer_name : str
    contact_name  : str    
    
    class Config:
        orm_mode = True    
 
    
class CreateCustomer(CustomerBase):
    customer_id : int = 0
    class Config:
        orm_mode = True    

