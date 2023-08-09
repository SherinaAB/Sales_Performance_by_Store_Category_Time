from sqlalchemy import (Column, String, Integer, Float, DateTime, ForeignKey)
from sqlalchemy.orm import declarative_base, relationship, backref


Base = declarative_base()

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    store_number = Column(Integer())
    state = Column(String())
    market = Column(String())
    region = Column(String())
    national = Column(String())
    product_id = Column(Integer(), ForeignKey('products.id'))

    Sale = relationship('Sale', backref=backref('store'))

    def __repr__(self):
        return f"Id: {self.id}," \
        +f"Name: {self.name}," \
        +f"Store Number: {self.store_number}," \
        +f"State: {self.state}," \
        +f"Market: {self.market}," \
        +f"Region: {self.region}," \
        +f"National: {self.national},"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    product_description = Column(String())
    sku = Column(Integer())
    wholesale = Column(Integer())
    retail = Column(Integer())    
    brand = Column(String())
    category = Column(String())
    department = Column(String())


    Sale = relationship('Sale', backref=backref('proudct'))

    # def __repr__(self):
    #     return f"Id: {self.id}," \
    #     +f"Name: {self.name}," \
    #     +f"Product Description: {self.product_description}," \
    #     +f"SKU: {self.sku}," \
    #     +f"Wholesale: {self.wholesale}," \
    #     +f"Retail: {self.retail}," \
    #     +f"Brand: {self.brand}," \
    #     +f"Category: {self.category}," \
    #     +f"Department: {self.department},"

# class Date(Base):
#     __tablename__ = "dates"

#     id = Column(Integer(), primary_key=True)
#     week_number = Column(Integer())
#     week = Column(String())
#     month = Column(String())
#     quarter = Column(String())
#     year = Column(Integer())
#     ly_week_number = Column(Integer())
#     ly_week = Column(String())
#     ly_month = Column(String())
#     ly_quarter = Column(String())
#     ly_year = Column(Integer())

#     def __repr__(self):
#         return f"Id: {self.id}," \
#         +f"Week Number: {self.week_number}," \
#         +f"Week: {self.week}," \
#         +f"Month: {self.month}," \
#         +f"Quarter: {self.quarter}," \
#         +f"Year: {self.year}," \
#         +f"Last Year Week Number: {self.week_number}," \
#         +f"Last Year Week: {self.week}," \
#         +f"Last Year Month: {self.month}," \
#         +f"Last Year Quarter: {self.quarter}," \
#         +f"Last Year: {self.year},"

class Sale(Base):
    __tablename__="sales"

    id = Column(Integer(), primary_key=True)
    store_id = Column(Integer(), ForeignKey('stores.id'))
    product_id = Column(Integer(), ForeignKey('products.id'))
    sales_quantity = Column(Integer())
    sales_dollar_amount = Column(Integer())
    cost_dollar_amount = Column(Integer())
    gross_profit_dollar_amount = Column(Integer())
    
    # date_id = Column(Integer(), ForeignKey('dates.id'))

    def __repr__(self):
        return f"Id: {self.id}," \
        +f"store_id: {self.store_id}," \
        +f"product_id: {self.product_id}," \
        +f"Sales Quantity: {self.sales_quantity}," \
        +f"Sales Dollar Amount: {self.sales_dollar_amount}," \
        +f"Cost Dollar Amount: {self.cost_dollar_amount}," \
        +f"Gross Profit Dollar Amount: {self.gross_profit_dollar_amount}"
    
    # +f"date_id: {self.date_id}," \

