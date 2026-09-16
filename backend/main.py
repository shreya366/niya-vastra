from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class Product(BaseModel):
    name: str
    category: str
    color: str
    fabric: str
    price: float
    available: bool = True

@app.get("/")
def home():
    return {
        "brand": "Niya Vastra",
        "tagline": "As pure as a mother's love."
    }



products = [
    {
        "id": 1,
        "name": "Amethyst Bloom",
        "category": "Lehenga",
        "color": "Purple",
        "fabric": "Net Chikankari",
        "price": 3000,
        "available": True
    },
    {
        "id": 2,
        "name": "Lavender Dream",
        "category": "Lehenga",
        "color": "Lavender",
        "fabric": "Net",
        "work": "Sequence Work",
        "price": 3500,
        "available": True
    }
]

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
@app.post("/products", status_code=201)
def create_product(product: Product):

    new_product = product.model_dump()

    new_product["id"] = len(products) + 1

    products.append(new_product)

    return new_product