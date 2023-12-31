from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, session
# import click
# import matplotlib.pyplot as plt
from models import (Base, Store, Product, Sale)

engine = create_engine('sqlite:///sales.db')

products = []
stores = []

Session = sessionmaker(bind=engine)
session = Session() 

def hide():
    # products = [            
    #     {"id": 1, "name" : "Anker PowerCore", "wholesale" : 10,"retail" : 24,"category" : "Portable Chargers", "department" : "Tech Accessories"},
    #     {"id": 2, "name" : "Jackery Bolt 10050","wholesale" : 12,"retail" : 40,"category" : "Portable Chargers", "department" : "Tech Accessories"},
    #     {"id": 3, "name" : "Lifeproof Lifeactive Power Pack","wholesale" : 23,"retail" : 80,"category" : "Portable Chargers", "department" : "Tech Accessories"},
    #     {"id": 4, "name" : "Peak Design Tech Poutch","wholesale" : 15,"retail" : 60,"category" : "Electronic Organizers", "department" : "Organization"},
    #     {"id": 5, "name" : "FYY Travel Cable Organizer Pouch","wholesale" : 3,"retail" : 10,"category" : "Electronic Organizers", "department" : "Organization"},
    #     {"id": 6, "name" : "Bellroy Tech Kit","wholesale" : 18,"retail" : 60,"category" : "Electronic Organizers", "department" : "Organization"},
    #     {"id": 7, "name" : "Troubadour Apex Backpack","wholesale" : 25,"retail" : 245,"category" : "Back Packs", "department" : "Travel Bags"},
    #     {"id": 8, "name" : "July Carry All Backpack Series 2","wholesale" : 30,"retail" : 175, "category" : "Back Packs","department" : "Travel Bags"},
    #     {"id": 9, "name" : "Everlane Renew Backpack","wholesale" : 25,"retail" : 95,"category" : "Back Packs","department" : "Travel Bags"},
    # ]

    # stores = [
    #     {"id": 1, "name" : "Atlanta", "store_number" : 100, "state" : "GA", "market" : "ATL", "region" : "SOE"},
    #     {"id": 2, "name" : "Buckhead", "store_number" : 101, "state" : "GA", "market" : "ATL", "region" : "SOE"},
    #     {"id": 3, "name" : "Los Angeles", "store_number" : 200, "state" : "CA", "market" : "LA", "region" : "PAC"},   
    #     {"id": 4, "name" : "Anaheim", "store_number" : 201, "state" : "CA", "market" : "LA", "region" : "PAC"},
    #     {"id": 5, "name" : "Bronx", "store_number" : 300, "state" : "NY", "market" : "NYC", "region" : "NOE"},   
    #     {"id": 6, "name" : "Manhattan", "store_number" : 301, "state" : "NY", "market" : "NYC", "region" : "NOE"},  
    #     {"id": 7, "name" : "Chicago", "store_number" : 400, "state" : "IL", "market" : "CHI", "region" : "MDW"}, 
    #     {"id": 8, "name" : "Lincoln", "store_number" : 401, "state" : "IL", "market" : "CHI", "region" : "MDW"},  
    #     {"id": 9, "name" : "Dallas", "store_number" : 500, "state" : "TX", "market" : "TEX", "region" : "SWE"},   
    #     {"id": 10, "name" : "Houston", "store_number" : 501, "state" : "TX", "market" : "TEX", "region" : "SWE"},    
    #     {"id": 11, "name" : "Seattle", "store_number" : 600, "state" : "WA", "market" : "WAS", "region" : "PNW"},   
    #     {"id": 12, "name" : "Bellevue", "store_number" : 601, "state" : "WA", "market" : "WAS", "region" : "PNW"},
    # ]

    # sales = [
    #     {"product_id" : 1, "store_id" : 9, "quantity" : 6858},
    #     {"product_id" : 2, "store_id" : 7, "quantity" : 5339},
    #     {"product_id" : 3, "store_id" : 5, "quantity" : 1814},
    #     {"product_id" : 4, "store_id" : 12, "quantity" : 5097},
    #     {"product_id" : 5, "store_id" : 2, "quantity" : 3450},
    #     {"product_id" : 6, "store_id" : 10, "quantity" : 2886},
    #     {"product_id" : 7, "store_id" : 6, "quantity" : 4317},
    #     {"product_id" : 8, "store_id" : 1, "quantity" : 1527},
    #     {"product_id" : 9, "store_id" : 8, "quantity" : 3909},
    #     {"product_id" : 1, "store_id" : 11, "quantity" :7466},
    #     {"product_id" : 2, "store_id" : 4, "quantity" : 8985},
    # ]

    # store_session.query()

            # store = session.query(Store).first()
            # # print(store.id)
            # store_products = session.query(Product).filter_by(store_id=store.id)
            # print([product for product in store_products])
    # userinput_dict = {"Sales" : "Total Sales", "Cost" : "Total Cost","Profit" : "Total Gross Profit",}
        # products_dict = {product["id"]: product for product in products}
        # stores_dict = {store["id"]: store for store in stores}
        pass
    
dict = {"userinput": "All Options"}

def main():
    product_id = input("Selcect Item by Typing a Number: 109 - 117: ")
    product = session.query(Product).filter_by(id = product_id).first()
    userinput = input("Type: \n Total Sales:        (view total sales for selected item) \n Total Cost:         (view total cost for selected item) \n Total Gross Profit: (view Gross Profit for selected item) \n All Options:       (view Total Sales, Total Cost, & Total Gross Profit for selected item)\n\n ENTER SELECTION HERE:  ")
    if userinput == "Total Sales":
        dollars = 0
        for sale in product.Sale:
            dollars = dollars + sale.sales_dollar_amount
        print("Total Sales:  $ ",dollars)
    elif userinput == "Total Cost":
        total = 0
        for sale in product.Sale: 
            total = total + sale.cost_dollar_amount
        print("Total Cost $ ",total)
    elif userinput == "Total Gross Profit":
        profit = 0
        for sale in product.Sale: 
            profit  = profit + sale.gross_profit_dollar_amount
        print("Total Gross Profit $ ",profit)
    elif dict["userinput"] == "All Options":
        dollars = 0
        total = 0
        profit = 0
        for sale in product.Sale:
            dollars = dollars + sale.sales_dollar_amount
            total = total + sale.cost_dollar_amount 
            profit = profit + sale.gross_profit_dollar_amount
        print(" Program Sales     Program Cost     Program Gross Profit "'\n',"$   ",dollars,"     $   ", total,"     $          ", profit)
    
if __name__ == "__main__":
    main()













# @cli.command()
# @click.argument('products', nargs=-1)  # Allow passing multiple product names
# @click.argument('stores', nargs=-1)    # Allow passing multiple store names
# @click.argument('sales', nargs=-1)     # Allow passing multiple sales data

# def show_sales_chart(products, stores, sales):
#     # Create a bar chart using Matplotlib
#     plt.bar(products, sales)
#     plt.xlabel('Products')
#     plt.ylabel('Sales')
#     plt.title('Sales Performance by Product')
#     plt.xticks(rotation=45)
#     plt.tight_layout()

#     # Display the chart
#     plt.show()