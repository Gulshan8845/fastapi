from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    name: str
    price: float
    quantity: int

class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str

class OrderItem(BaseModel):
    product_id: int
    bought_quantity: int

class Order(BaseModel):
    timestamp: str
    items: List[OrderItem]
    total_amount: float
    address: UserAddress
