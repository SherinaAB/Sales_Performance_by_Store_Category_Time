from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models import (Base, Store, Product, Sale)

if __name__ == "__main__":

    engine = create_engine('sqlite:///sales.db')

    # Session = sessionmaker(bind=engine)
    # session = Session() 


    with Session(engine) as session: 
        # product  = session.query(Product).first()
        # product_stores = session.query(Store).filter_by(product_id=product.id)
        # print([store for store in product_stores])


        store = session.query(Store).first()
        # print(store.id)
        store_products = session.query(Product).filter_by(store_id=store.id)
        print([product for product in store_products])

        # ======================================================================================

        # product = session.query(Product).first()
        # product_sales = session.query(Sale).filter_by(product_id=product.id)
        # # print([sale for sale in store_products])

        # # ======================================================================================

        # store = session.query(Store).first()
        # store_sales = session.query(Sale).filter_by(store_id=store.id)
        # print([sale for sale in store_sales])

        # store_products = [session.query(Product).get(sale.product_id) for sale in store_sales]

        # ======================================================================================

        # sale = session.query(Sale).first()
        # sale_stores = session.query(Store).filter_by(sale_id=sale.id)
        # print([store for store in sale_stores])

        # ======================================================================================

        # sale = session.query(Sale).first()
        # sale_products = session.query(Product).filter_by(sale_id=sale.id)
        # print([product for product in sale_products])

        tech_store_products = [
            {
                "name" : "Anker PowerCore",
                "category" : "Portable Chargers",
                "department" : "Tech Accessories",
            },
            {
                "name" : "Jackery Bolt 10050",
                "category" : "Portable Chargers",
                "department" : "Tech Accessories",
            },
            {
                "name" : "Lifeproof Lifeactive Power Pack",
                "category" : "Portable Chargers",
                "department" : "Tech Accessories",
            },
            {
                "name" : "Peak Design Tech Poutch", 
                "category" : "Electronic Organizers",
                "department" : "Organization",
            },
            {
                "name" : "FYY Travel Cable Organizer Pouch",
                "category" : "Electronic Organizers",
                "department" : "Organization",
            },
            {
                "name" : "Bellroy Tech Kit", 
                "category" : "Electronic Organizers",
                "department" : "Organization",
            },
            {
                "name" : "Troubadour Apex Backpack", 
                "category" : "Back Packs",
                "department" : "Travel Bags",
            },
            {
                "name" : "July Carry All Backpack Series 2", 
                "category" : "Back Packs",
                "department" : "Travel Bags",
            },
            {
                "name" : "Everlane Renew Backpack", 
                "category" : "Back Packs",
                "department" : "Travel Bags",
            },
        ]

        get_tech_store_products_by_category(tech_store_products,"Electronic Organizers")

    