from typing import Union

from fastapi import FastAPI

from db import clientPS

from db import productDB
from model import product


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/product/")
def getproduct():
    data=productDB.consulta()
    return (data) 


@app.get("/product/{id}")
def getproductById(id:int):
    dataId=productDB.consultaId(id)
    return (dataId)


@app.post("/product/")
def createProduct(prod: product.Product):
    return productDB.insert(prod)


""" @app.put("/product/{id}")
def getproductById(id:int):
    dataActualitza=productDB. """