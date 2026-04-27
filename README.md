# Local Restaurant Directory API
A CRUD (Create, Read, Update, Delete) API built with FastAPI and MongoDB to manage a local directory of restaurants.
---
## Prerequisites
- python 3.9 or above
- MongoDB (Running locally on localhost:27017)
The above listed are requested to be installed before implementing this project
---
## Installation & Setup
1. Clone the repository (or navigate to your project folder):
git clone https://github.com/Arrush5/Local-Restaurant-Directory-API.git
cd Local-Restaurant-Directory-API
2. Install dependencies:
pip install fastapi pymongo uvicorn
3. Run the application:
uvicorn main:app --reload
---
## API Documentation
|**Action**|**Method**|**Endpoint**|**Description**|
|---|---|---|---|
|Create|POST|/restaurants/|Adds a new restaurant to the directory.|
|Read All|Get|/restaurants/|Retrieves a list of all restaurants.|
|Update|Put|/restaurants/{id}|Updates details for an existing restaurant.|
|Delete|DELETE|/restaurants/{id}|Removes a restaurant from the database.|
---
## Sample Request Body (POST/PUT)
```json
{
  "id": "rest-001",
  "name": "Spice Symphony",
  "cuisine_type": "Indian",
  "rating": 4.8,
  "is_open": true,
  "location": "Downtown Salem"
}
```

---
## Folder Structure
Day 5/

├── main.py

└── README.md
