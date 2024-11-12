from pydantic import BaseModel
from datetime import date

class CreateCars(BaseModel):
    
    truck_type: int
    due_date : date
    total_income : float
    V_capacity : float
    W_capacity : float
    