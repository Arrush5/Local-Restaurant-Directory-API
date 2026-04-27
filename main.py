from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

client = MongoClient("mongodb://localhost:27017")
db = client.restaurants_db
restaurants_collection = db.restaurants

class Restaurant(BaseModel):
    id: str
    name: str
    cuisine_type: str
    rating: float
    is_open: bool
    location: str

@app.post("/restaurants/")
def create_restaurant(restaurant: Restaurant):
    # Convert the Pydantic model to a dictionary for MongoDB
    restaurant_dict = restaurant.model_dump()
    
    # Insert the document into our collection
    restaurants_collection.insert_one(restaurant_dict)
    
    # Return the newly created restaurant to the user
    return restaurant

@app.get("/restaurants/")
def get_all_restaurants():
    # .find({}) gets all documents. 
    # {"_id": 0} tells MongoDB to hide its internal ID so it matches our Pydantic model perfectly.
    restaurants = list(restaurants_collection.find({}, {"_id": 0}))
    return restaurants

@app.put("/restaurants/{restaurant_id}")
def update_restaurant(restaurant_id: str, updated_data: Restaurant):
    # Convert the new Pydantic data into a dictionary
    data_dict = updated_data.model_dump()
    
    # Update the document where the "id" matches the restaurant_id
    # $set tells MongoDB to update the specific fields we provide
    result = restaurants_collection.update_one(
        {"id": restaurant_id}, 
        {"$set": data_dict}
    )
    
    # Check if we actually modified anything
    if result.modified_count == 1:
        return {"message": "Restaurant updated successfully!"}
    return {"message": "Restaurant not found or no changes made."}

@app.delete("/restaurants/{restaurant_id}")
def delete_restaurant(restaurant_id: str):
    # Delete the document where the "id" matches
    result = restaurants_collection.delete_one({"id": restaurant_id})
    
    if result.deleted_count == 1:
        return {"message": "Restaurant deleted successfully!"}
    return {"message": "Restaurant not found."}