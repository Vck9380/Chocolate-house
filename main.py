from sqlalchemy.orm import Session
from models import Flavor, Ingredient, Sugestion
def add_seasonal_flavor(db: Session, name: str, description: str):
    existing_flavor = db.query(Flavor).filter(Flavor.name == name).first()
    if existing_flavor:
        return "Flavor already exists" 
    new_flavor = Flavor(name=name, description=description)
    db.add(new_flavor)  
    db.commit() 
    return ("Flavor added successfully")

def view_seasonal_flavors(db: Session):
    flavors = db.query(Flavor).all()
    if not flavors:
        return "No seasonal flavors found"
    flavor_list = []
    for flavor in flavors:
        flavor_list.append(f"Flavor: {flavor.name}, Description: {flavor.description}")

    return ("\n".join(flavor_list))

def add_or_update_ingredient(db: Session, name: str, quantity: float):
    ingredient = db.query(Ingredient).filter(Ingredient.name == name).first()
    if ingredient:
        ingredient.quantity += quantity
    else:
        new_ingredient = Ingredient(name=name, quantity=quantity)
        db.add(new_ingredient)
    db.commit()
    return ("Ingredient added or updated successfully")

def add_customer_sugestion(db: Session, customer_name: str, flavor: str, allergy: bool, details: str = None):
    sugestion = Sugestion(
        customer_name=customer_name, 
        flavor_suggestion=flavor, 
        allergy_concern=allergy, 
        allergy_details=details
    )
    db.add(sugestion) 
    db.commit()  
    return ("Customer sugestion added")
