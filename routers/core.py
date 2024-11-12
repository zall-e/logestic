from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from utils.logics import *
from schemas import core

router = APIRouter()

@router.get("/get_product")
def get_product():
    
    products = retrieve_products()
    
    if products:
    
        response = {
            "status" : "200",
            "is_success" : True,
            "data" : products
        }
        
        return JSONResponse(response, status_code = status.HTTP_200_OK)


    response = {
        "status" : "404",
        "is_success" : False
    }
        
    return JSONResponse(response, status_code = status.HTTP_404_NOT_FOUND)

@router.post("/create_product")
def create_product(input: core.CreateProduct):
    
    title = input.title
    length = input.length
    width = input.width
    heigth = input.heigth
    weigth = input.weigth
    destination = input.destination
    
    is_saved = save_product(title, length, width, heigth, weigth, destination)
    
    if is_saved:
        
        response = {
            "status" : "200",
            "is_success" : True,
            "data" : is_saved
        }
        
        return JSONResponse(response, status_code = status.HTTP_200_OK)


    response = {
        "status" : "400",
        "is_success" : False
    }
        
    return JSONResponse(response, status_code = status.HTTP_400_BAD_REQUEST)
    
    
@router.put("/update_product")
def update_product(input: core.EditProduct):
    
    id = input.id
    title = input.title
    length = input.length
    width = input.width
    heigth = input.heigth
    weigth = input.weigth
    destination = input.destination
    
    is_saved = edit_product(id, title, length, width, heigth, weigth, destination)
    
    if is_saved:
    
        response = {
            "status" : "200",
            "is_success" : True,
            "data" : is_saved
        }
        
        return JSONResponse(response, status_code = status.HTTP_200_OK)


    response = {
        "status" : "400",
        "is_success" : False
    }
        
    return JSONResponse(response, status_code = status.HTTP_400_BAD_REQUEST)


@router.delete("/delete_product")
def remove_product(id: str):
    
    
    
    is_saved = delete_product(id)
    
    if is_saved:
    
        response = {
            "status" : "200",
            "is_success" : True,
            "data" : is_saved
        }
        
        return JSONResponse(response, status_code = status.HTTP_200_OK)


    response = {
        "status" : "400",
        "is_success" : False,
        "message": "products not found!"
    }
        
    return JSONResponse(response, status_code = status.HTTP_400_BAD_REQUEST)