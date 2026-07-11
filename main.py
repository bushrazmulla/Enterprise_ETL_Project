from src.extract import DataExtractor
from src.transform import DataTransformer
from src.load import DataLoader

def main():

    extractor = DataExtractor("data/raw")
    transformer = DataTransformer()
    loader = DataLoader()

    sales = extractor.extract_sales()
    customers = extractor.extract_customers()
    print(customers.columns)
    products = extractor.extract_products()

    sales = transformer.remove_duplicates(sales)

    sales, customers, products = transformer.handle_missing_values(
        sales,
        customers,
        products
    )
    sales = transformer.standardize_dates(sales)
    final_df = transformer.merge_datasets(
    sales,
    customers,
    products )
    final_df = transformer.calculate_revenue(final_df)
    final_df = transformer.validate_data(final_df)
    loader.load_to_mysql(
    final_df,
    "sales_report"
    )
    print("\nFinal Dataset")
    print(final_df)

    print("\nTransformation Completed!")

    print("\nSales Data")
    print(sales)

    print("\nCustomers Data")
    print(customers)

    print("\nProducts Data")
    print(products)


if __name__ == "__main__":
    main()