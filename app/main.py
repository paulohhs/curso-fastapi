from fastapi import FastAPI
from app.routes.category_routes import router as category_router
from app.routes.product_routes import router as product_router

app = FastAPI()

@app.get('/health-check')
def health_check():
    return True

app.include_router(category_router)
app.include_router(product_router)
