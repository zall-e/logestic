from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from utils.cars import *
from schemas import cars

router = APIRouter()

@router.get("/get_cars")
def get_cars():
    
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
    