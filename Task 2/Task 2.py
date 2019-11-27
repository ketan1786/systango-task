import csv

class Product():
    def __init__(self, product_name, cost_price, sale_tax_percentage, final_price, country):
        self.product = product_name
        self.cost = cost_price
        self.tax = sale_tax_percentage
        self.final_cost = final_price
        self.country = country

    def