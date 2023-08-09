# from faker import Faker  ...don't think i need this, but imported just in case I need it later
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


from models import Store, Product, Sale

if __name__ == '__main__':
    engine = create_engine('sqlite:///retail_app.db')

    # Base.metadata.create_all(engine)   
    # LECTURE SOLUTION DOES NOT INDICATE THAT I NEED THE BASE.METADATA.CREATE_ALL(ENGINE) .... DO I NEED THIS HERE, IF NOT HERE, THEN WHERE???
    # Session = sessionmaker(bind=engine)
    # session = Session() 
    # session.add_all()
    # session.commit()

    # WHERE DO THE SESSION.QUERY DELETE() COMMANDS GO WITHIN THE SEED FILE?????
    # session.query(Store).delete()
    # session.query(Product).delete()
    # session.query(Date).delete()
    # WHERE DO THE SESSION.QUERY DELETE() COMMANDS GO WITHIN THE SEED FILE?????  ...LECTURE SOLUTION CODE INDICATES TO ADD PRIOR TO LISTS TO CLEAR DB BEFORE EACH SEEDING, **BUT** IS THIS UTILIZED ****ONLY**** WHEN USING FAKER AND RANDOM DATA?????

    with Session(engine) as session:
        
        session.query(Store).delete()
        session.query(Product).delete()
        session.query(Sale).delete()
        # session.query(Date).delete()

        stores =[]
        
        atlanta = Store(name="Atlanta", store_number=100, state="GA", market="ATL", region="SOE",national="national")
        buckhead = Store(name="Buckhead", store_number=101, state="GA", market="ATL", region="SOE",national="national")
        los_angeles = Store(name="Los Angeles", store_number=200, state="CA", market="LA", region="PAC",national="national")    
        anaheim = Store(name="Anaheim", store_number=201, state="CA", market="LA", region="PAC",national="national")    
        bronx = Store(name="Bronx", store_number=300, state="NY", market="NYC", region="NOE",national="national")    
        manhattan = Store(name="Manhattan", store_number=301, state="NY", market="NYC", region="NOE",national="national")    
        chicago = Store(name="Chicago", store_number=400, state="IL", market="CHI", region="MDW",national="national")    
        lincoln = Store(name="Lincoln", store_number=401, state="IL", market="CHI", region="MDW",national="national")    
        dallas = Store(name="Dallas", store_number=500, state="TX", market="TEX", region="SWE",national="national")    
        houston = Store(name="Houston", store_number=501, state="TX", market="TEX", region="SWE",national="national")    
        seattle = Store(name="Seattle", store_number=600, state="WA", market="WAS", region="PNW",national="national")    
        bellevue = Store(name="Bellevue", store_number=601, state="WA", market="WAS", region="PNW",national="national")  

        session.add_all([atlanta,buckhead,los_angeles,anaheim,bronx,manhattan,chicago,lincoln,dallas,houston,seattle,bellevue])
        session.commit()
        stores = [atlanta,buckhead,los_angeles,anaheim,bronx,manhattan,chicago,lincoln,dallas,houston,seattle,bellevue]

        # print(stores)
        products = []

        anker_powercore = Product(name="Anker PowerCore",product_description="Anker PowerCore Slim 10000 PD",sku=321-432,wholesale=10,retail=24,brand="Anker",category="Portable Chargers",department="Tech Accessories")
        jackery_bolt_10050= Product(name="Jackery Bolt 10050",product_description="Bolt 10050mAh Power Bank",sku=432-543,wholesale=12,retail=40,brand="Jackery",category="Portable Chargers",department="Tech Accessories")
        lifeproof_lifeactive_powerpack= Product(name="Lifeproof Lifeactive Power Pack",product_description="Lifeproof Lifeactive Power Pack 10",sku=543-654,wholesale=23,retail=80,brand="Lifeproof",category="Portable Chargers",department="Tech Accessories")
        peak_design_tech_pouch = Product(name="Peak Design Tech Poutch", product_description="Tech Pouch",sku=654-765,wholesale=15,retail=60,brand="Peak Design",category="Electronic Organizers",department="Organization")
        fyy_cable_case= Product(name="FYY Travel Cable Organizer Pouch", product_description="Electronic Accessories Carry Case",sku=765-876,wholesale=3,retail=10,brand="FYY",category="Electronic Organizers",department="Organization")
        bellroy_tech_kit= Product(name="Bellroy Tech Kit", product_description="Tech Accessories Organizer Pouch",sku=876-987,wholesale=18,retail=60,brand="Bellroy",category="Electronic Organizers",department="Organization")
        troubadour_apex_backpack= Product(name="Troubadour Apex Backpack", product_description="Handsome styling, ergonomic design, and thoughtful details make this pricey backpack worth the money. The slim, structured shape looks best when packed just so—not too empty, but not overstuffed.",sku=987-109,wholesale=25,retail=245,brand="Troubadour",category="Back Packs",department="Travel Bags")
        july_carry_all_backpack= Product(name="July Carry All Backpack Series 2", product_description="This backpack is loaded with traveler-friendly features, including a sturdy luggage sleeve and passport pocket. Leather accents and gunmetal hardware elevate its simple silhouette, but the thick material can feel a little warm in hot climates.",sku=109-111,wholesale=30,retail=175,brand="",category="Back Packs",department="Travel Bags")
        everlane_renew_transit_backpack= Product(name="Everlane Renew Backpack", product_description="A streamlined design and welcome features—including a magnetic top closure and a plethora of pockets—make this budget-friendly, wear-anywhere bag look and feel pricier than it is. But unlike our other picks, it isn’t backed by a warranty.",sku=111-121,wholesale=25,retail=95,brand="Everlane",category="Back Packs",department="Travel Bags")

        session.add_all([anker_powercore,jackery_bolt_10050,lifeproof_lifeactive_powerpack,peak_design_tech_pouch,fyy_cable_case,bellroy_tech_kit,troubadour_apex_backpack,july_carry_all_backpack,everlane_renew_transit_backpack])
        session.commit()
        products = [anker_powercore,jackery_bolt_10050,lifeproof_lifeactive_powerpack,peak_design_tech_pouch,fyy_cable_case,bellroy_tech_kit,troubadour_apex_backpack,july_carry_all_backpack,everlane_renew_transit_backpack]

        print(products)
        # BELOW ARE ATTRIBUTE ARRAYS FOR THE DATE CLASS/METHOD
        # week_number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
        # week = ["June 3, 2023","June 10, 2023","June 17, 2023","June 24, 2023","July 1, 2023","August 5, 2023","August 12, 2023","August 19,2023","August 26,2023"]
        # month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        # quarter = ["Q1","Q2","Q3","Q4"]
        # year = [2021,2022,2023]
        # ly_week_number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
        # ly_week = []
        # ly_month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        # ly_quarter = ["Q1","Q2","Q3","Q4"]
        # ly_year = [2020,2021,2022]

        # session.add_all([month,quarter,year,ly_month,ly_quarter,ly_year])
        # session.commit()



        # sales = [] 
        
        for store in stores:
            # print(store.name)
            for _ in range(random.randint(1,10)):
                new_product = random.choice(products) 
                # print(new_product.retail)
                quantity = random.randint(10,9999)

                new_sale = Sale(store_id = store.id,
                product_id = new_product.id,
                sales_quantity = quantity,
                sales_dollar_amount = new_product.retail * quantity,
                cost_dollar_amount = new_product.wholesale * quantity,
                gross_profit_dollar_amount = (new_product.retail * quantity)-(new_product.wholesale * quantity)
                ) 
                session.add(new_sale)
        session.commit()



        # s1 = Sale(store_id = atlanta.id, product_id = anker_powercore.id)