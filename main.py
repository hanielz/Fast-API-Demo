from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
# from typing import List

app = FastAPI()

# Model for Item
class Item(BaseModel):
	name: str
	description: str = None
	price: float = Field(gt=0, description="The price must be greater than zero")
	tax: float = None


# Fake database to store items
fake_items_db = []

# GET
# POST
# PUT
# DELETE



@app.get("/")
def read_root():
    return f"helloo wleowleo community !"

# Create operation
@app.post("/items/", response_model=Item)
def create_item(item: Item):
	fake_items_db.append(item)
	return item

# Read operation
@app.get("/items/", )
def read_items():
	return fake_items_db

@app.get("/items/{item_id}",response_model=Item )
def read_each_items(item_id :int):    
    if item_id < 0 or item_id >= len(fake_items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]

# Update operation
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
	if item_id < 0 or item_id >= len(fake_items_db):
		raise HTTPException(status_code=404, detail="Item not found")
	
	fake_items_db[item_id] = updated_item
	return updated_item

# Delete operation
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
	if item_id < 0 or item_id >= len(fake_items_db):
		raise HTTPException(status_code=404, detail="Item not found")
	
	deleted_item = fake_items_db.pop(item_id)
	return deleted_item


