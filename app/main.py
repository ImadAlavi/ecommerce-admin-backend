from fastapi import FastAPI
from app.api.v1.endpoints import customers, inventory, products, sales, users

app = FastAPI(title="E-commerce Admin API")

app.include_router(customers.router, prefix="/api/v1/customers", tags=["Customers"])
app.include_router(inventory.router, prefix="/api/v1/inventory", tags=["Inventory"])
app.include_router(products.router, prefix="/api/v1/products", tags=["Products"])
app.include_router(sales.router, prefix="/api/v1/sales", tags=["Sales"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
