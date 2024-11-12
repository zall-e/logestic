from models.sql import SessionLocal
from models import sql

def retrieve_products():
    db = SessionLocal()
    try:
        objs = db.query(sql.Cars).all()
        
        products = []
        
        for obj in objs:
            products.append({
                "id"  : obj.id,
                "truck_type" : obj.truck_type,
                "due_date" : obj.due_date,
                "total_income" : obj.total_income,
                "V_capacity" : obj.V_capacity,
                "W_capacity" : obj.W_capacity,
            })
            
            return products
        return None

    finally:
        db.close()