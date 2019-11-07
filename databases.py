from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, picture_link, description):

    product_object = Product(
        name=name,
        price=price,
        picture_link=picture_link,
        description=description)
    session.add(product_object)
    session.commit()


add_product("iphone", 3000 , "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlJD8T1EZgy4-_qD2o4uXbQlm81K9SxyY0NvJEoPrKqHN3wqIU&s" , "iphone x")