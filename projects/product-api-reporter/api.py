from fastapi import FastAPI
from summary import summarize_products
from main import fetch_products

app = FastAPI()

@app.get("/summary")
def summary():
    products = fetch_products()
    summary = summarize_products(products)
    return summary
