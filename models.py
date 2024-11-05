from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
base = declarative_base()
# model for seasonal Flavors
class Flavor(base):
    __tablename__ = 'seasonal_flavors'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
#model for ingredient's inventory    
class Ingredient(base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    quantity = Column(Float)
#model for customer sugestion    
class Sugestion(base):
    __tablename__ = 'customer_sugestions'
    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    flavor_suggestion = Column(String)
    allergy_concern = Column(Boolean)
    allergy_details = Column(String, nullable=True)
