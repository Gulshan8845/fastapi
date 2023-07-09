from fastapi import FastAPI, HTTPException
from typing import List
from models import Product, Order, UserAddress, OrderItem
app = FastAPI()
products = []
orders = []
@app.get("/")
def root():
    return {"message": "Welcome to the eCommerce API"}

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product created successfully"}

@app.post("/orders")
def create_order(order: Order):
    orders.append(order)
    return {"message": "Order created successfully"}

@app.get("/orders")
def get_orders(skip: int = 0, limit: int = 10):
    return orders[skip : skip + limit]

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["order_id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.put("/products/{product_id}")
def update_product(product_id: int, quantity: int):
    for product in products:
        if product["product_id"] == product_id:
            product["quantity"] = quantity
            return {"message": "Product updated successfully"}
    raise HTTPException(status_code=404, detail="Product not found")
