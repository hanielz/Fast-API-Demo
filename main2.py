from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from starlette import status


from database import get_db
import models
import schemas


app = FastAPI()


@app.get("/customers/", response_model=List[schemas.CreateCustomer])
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db) ):
    
    customers=  db.query(models.Customers).offset(skip).limit(limit).all()
    return customers

## EACH CUSTOMER ##
@app.get("/customers/{id}", response_model=schemas.CreateCustomer,status_code=status.HTTP_200_OK )
def read_each_customers(id : int, db: Session = Depends(get_db)) :
    
    idCust =  db.query(models.Customers).filter(models.Customers.customer_id == id).first()
    if idCust is None :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The id: {id} you requested for does not exist")
    return idCust


@app.post("/customer/",status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreateCustomer] )
def post_customer(post_customer : schemas.CreateCustomer,  db: Session = Depends(get_db) ) :

    existing_custId = db.query(models.Customers).filter(models.Customers.customer_id == post_customer.customer_id).first()
    
    if existing_custId :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Customer ID={post_customer.customer_id} already exist !" )
     
     
    new_customer = models.Customers(**post_customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    
    return [new_customer]


## UPDATE CUSTOMER ##    
@app.put("/customer/{id}",response_model=schemas.CreateCustomer )
def update_customer(update_cust : schemas.CreateCustomer , id : int, db: Session = Depends(get_db)) :
    
    updated_cust =  db.query(models.Customers).filter(models.Customers.customer_id == id).first()
    if updated_cust is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    
    for key, value in update_cust.dict().items():
        setattr(updated_cust, key, value)
        
    db.commit()
    db.refresh(updated_cust)
    
    return updated_cust

## DELETED CUSTOMER ##
@app.delete("/customer/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(id : int,db:Session = Depends(get_db) ):
    deleted_cust =  db.query(models.Customers).filter(models.Customers.customer_id == id).delete(synchronize_session=False)
                    
    if deleted_cust is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=f"The id:{id} does not exist") 
        
    db.commit()
    return {"detail": "Customer deleted successfully"}
