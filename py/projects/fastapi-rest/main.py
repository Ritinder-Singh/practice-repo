# =============================================================================
# FastAPI REST Service — main.py
# =============================================================================
# TODO: implement FastAPI app with Products CRUD.
# See README.md for full requirements.
# =============================================================================

# from fastapi import FastAPI, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from . import models, schemas
# from .database import engine, get_db
#
# models.Base.metadata.create_all(bind=engine)
# app = FastAPI(title="Products API", version="1.0.0")
#
# @app.get("/products", response_model=list[schemas.ProductResponse])
# def list_products(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
#     pass  # return db.query(models.Product).offset(skip).limit(limit).all()
#
# @app.post("/products", response_model=schemas.ProductResponse, status_code=201)
# def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
#     pass
#
# @app.get("/products/{product_id}", response_model=schemas.ProductResponse)
# def get_product(product_id: int, db: Session = Depends(get_db)):
#     pass  # raise HTTPException(status_code=404) if not found
