from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from fastapi import Depends

from database import SessionLocal
from models import Product as ProductModel

app = FastAPI()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

class Product(BaseModel):
    name: str
    category: str
    color: str
    fabric: str
    work: str | None = None
    price: float | None = None
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
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductModel).all()
    return products

@app.get("/products/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(ProductModel).filter(
        ProductModel.id == product_id
    ).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product

@app.post("/products", status_code=201)
def create_product(
    product: Product,
    db: Session = Depends(get_db)
):
    new_product = ProductModel(**product.model_dump())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product