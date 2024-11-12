from pydantic import BaseModel


class CreateProduct(BaseModel):
    title: str
    length: float
    width: float
    heigth: float
    weigth: float
    destination: int
    
class EditProduct(BaseModel):
    id: str
    title: str 
    length: float
    width: float
    heigth: float
    weigth: float
    destination: int

# class DeleteProdict(BaseModel):
#     id:str