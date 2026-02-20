from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Starter API")


class Item(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None


_items: List[Item] = []


@app.get("/items", response_model=List[Item])
def list_items():
    return _items


@app.post("/items", response_model=Item)
def create_item(item: Item):
    # Simple in-memory append; in real apps use a DB
    _items.append(item)
    return item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in _items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


# To run the app locally:
# 1. python -m venv venv
# 2. source venv/bin/activate
# 3. pip install -r requirements.txt
# 4. uvicorn starter-code:app --reload
