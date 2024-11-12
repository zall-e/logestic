from models.sql import SessionLocal
from models import sql

def retrieve_products():
    db = SessionLocal()
    try:
        objs = db.query(sql.Product).all()
        
        products = []
        
        for obj in objs:
            products.append({
                "id"  : obj.id,
                "title" : obj.title,
                "length" : obj.length,
                "width" : obj.width,
                "heigth" : obj.heigth,
                "weigth" : obj.weigth,
                "destination" : obj.destination,
                "price_truck" : obj.price_truck,
                "occupied_weight" : obj.occupied_weight,
                "occupied_volume" : obj.occupied_volume
            })
            
            return products
        return None

    finally:
        db.close()
        

def save_product(title, length, width, heigth, weigth, destination):
    db = SessionLocal()
    try:
        new_product = sql.Product(
            title = title,
            length = length,
            width = width,
            heigth = heigth,
            weigth = weigth,
            destination = destination,
            price_truck = 10,
            occupied_weight = 10,
            occupied_volume = 10
        )
        
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        
        response = {
            "id" : new_product.id,
            "title" : new_product.title,
            "length" : new_product.length,
            "width" : new_product.width,
            "heigth" : new_product.heigth,
            "weigth" : new_product.weigth,
            "destination" : new_product.destination,
            "price_truck" : new_product.price_truck,
            "occupied_weight" : new_product.occupied_weight,
            "occupied_volume" : new_product.occupied_volume
        }
        
        return response

    finally:
        db.close()
        
        
# def edit_product(id, title, length, width, heigth, weigth, destination):
#     db = SessionLocal()
#     try:
#         objs = db.query(sql.Product).all()
#         for products in objs:
#             if products.id == id:
                
#                 edited_product = sql.Product(
#                     title = title,
#                     length = length,
#                     width = width,
#                     heigth = heigth,
#                     weigth = weigth,
#                     destination = destination,
#                     price_truck = 10,
#                     occupied_weight = 10,
#                     occupied_volume = 10
#                 )
        
#                 db.add(edited_product)
#                 db.commit()
#                 db.refresh(edited_product)
        
#                 response = {
#                     "id" : edit_product.id,
#                     "title" :  edit_product.title,
#                     "length" : edit_product.length,
#                     "width" :  edit_product.width,
#                     "heigth" : edit_product.heigth,
#                     "weigth" : edit_product.weigth,
#                     "destination" : edit_product.destination,
#                     "price_truck" : edit_product.price_truck,
#                     "occupied_weight" : edit_product.occupied_weight,
#                     "occupied_volume" : edit_product.occupied_volume
#                 }
        
#         return response

#     finally:
#         db.close()
        

def edit_product(id: int, title: str, length: float, width: float, heigth: float, weigth: float, destination: str):
    db = SessionLocal()
    try:
        product = db.query(sql.Product).filter(sql.Product.id == id).first()
        if product:
            product.title = title
            product.length = length
            product.width = width
            product.heigth = heigth
            product.weigth = weigth
            product.destination = destination
            product.price_truck = 10
            product.occupied_weight = 10
            product.occupied_volume = 10

            db.commit()
            db.refresh(product)

            response = {
                "id": product.id,
                "title": product.title,
                "length": product.length,
                "width": product.width,
                "heigth": product.heigth,
                "weigth": product.weigth,
                "destination": product.destination,
                "price_truck": product.price_truck,
                "occupied_weight": product.occupied_weight,
                "occupied_volume": product.occupied_volume
            }
            return response

    finally:
        db.close()
        
        
def delete_product(id: str):
    db = SessionLocal()
    try:
        product = db.query(sql.Product).filter(sql.Product.id == id).first()
        if product:
            
            db.delete(product)
            db.commit()
            # db.refresh(product)

            response = {
                'message': 'deleted product!'
            }
            return response
        else:
            return None

    finally:
        db.close()