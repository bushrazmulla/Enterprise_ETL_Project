import pandas as pd
import os

class DataExtractor:

    def __init__(self, data_path):
        self.data_path = data_path

    def extract_sales(self):
        file_path = os.path.join(self.data_path, "sales.csv")
        sales_df = pd.read_csv(file_path)
        print(f"✅ Sales data extracted: {len(sales_df)} records")
        return sales_df

    def extract_customers(self):
        file_path = os.path.join(self.data_path, "customers.csv")
        customers_df = pd.read_csv(file_path)
        print(f"✅ Customer data extracted: {len(customers_df)} records")
        return customers_df

    def extract_products(self):
        file_path = os.path.join(self.data_path, "products.csv")
        products_df = pd.read_csv(file_path)

        # If you're using Excel instead of CSV,
        # replace the previous two lines with:
        # file_path = os.path.join(self.data_path, "products.xlsx")
        # products_df = pd.read_excel(file_path)

        print(f"✅ Product data extracted: {len(products_df)} records")
        return products_df