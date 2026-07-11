import pandas as pd


class DataTransformer:

    def remove_duplicates(self, sales_df):
        """
        Remove duplicate sales records.
        """

        original_rows = len(sales_df)

        sales_df = sales_df.drop_duplicates()

        removed = original_rows - len(sales_df)

        print(f"✅ Removed {removed} duplicate rows")

        return sales_df


    def handle_missing_values(self, sales_df, customers_df, products_df):
        """
        Handle missing values using simple business rules.
        """

        # Missing Quantity → Assume 1
        sales_df["Quantity"] = sales_df["Quantity"].fillna(1)

        # Missing Customer Name → Unknown
        customers_df["CustomerName"] = customers_df["CustomerName"].fillna("Unknown")

        # Missing Product Price → 0
        products_df["Price"] = products_df["Price"].fillna(0)

        print("✅ Missing values handled")

        return sales_df, customers_df, products_df
    
    def standardize_dates(self, sales_df):
        """
        Convert all dates to YYYY-MM-DD format.
        """
        sales_df["OrderDate"] = pd.to_datetime( 
            sales_df["OrderDate"], 
            errors="coerce",
            format="mixed"
        )
        sales_df["OrderDate"] = sales_df["OrderDate"].dt.strftime("%Y-%m-%d")
        print("✅ Dates standardized")
        return sales_df
    def merge_datasets(self, sales_df, customers_df, products_df):
        """
        Merge sales, customer and product data.
        """
        # Merge Sales + Customers
        merged_df = pd.merge(
            sales_df,
            customers_df,
            on="CustomerID",
            how="left"
        )
        # Merge with Products
        merged_df = pd.merge(
            merged_df,
            products_df,
            on="ProductID",
            how="left"
        )
        print("✅ Datasets merged successfully")
        return merged_df

    def calculate_revenue(self, merged_df):
        """
        Calculate revenue for each order.
        """

        merged_df["Revenue"] = (
            merged_df["Quantity"] *
            merged_df["Price"]
        )

        print("✅ Revenue calculated")

        return merged_df
    def validate_data(self, merged_df):
        """
        Validate final dataset.
        """

        if merged_df["OrderID"].isnull().any():
            print("❌ Missing Order IDs")

        if merged_df["CustomerID"].isnull().any():
            print("❌ Missing Customer IDs")

        if merged_df["Price"].isnull().any():
            print("⚠ Missing Product Prices")

        if (merged_df["Revenue"] < 0).any():
            print("❌ Negative Revenue Found")

        print("✅ Data validation completed")

        return merged_df