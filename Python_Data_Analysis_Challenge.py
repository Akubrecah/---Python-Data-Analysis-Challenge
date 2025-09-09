import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_sample_data():
   np.random.seed(42)  # For reproducible results
   start_date = datetime(2023, 1, 1)
   products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']
   
   data = []
   for i in range(100):
       date = start_date + timedelta(days=np.random.randint(0, 365))
       product = np.random.choice(products)
       revenue = round(np.random.uniform(10, 500), 2)
       quantity = np.random.randint(1, 20)
       data.append([date.strftime('%Y-%m-%d'), product, round(revenue, 2), quantity])

   df = pd.DataFrame(data, columns=['Date', 'Product', 'Revenue ($)', 'Quantity Sold'])
   df.to_csv('sales_data.csv', index=False)
   print("Sample data created and saved to 'sales_data.csv'.")

def analyze_sales_data():
   df = pd.read_csv('sales_data.csv')
   df['Date'] = pd.to_datetime(df['Date'])
def analyze_sales_data():
    try:
        # Load the CSV file
        df = pd.read_csv('sales_data.csv')
        print("Data loaded successfully!")
        print(f"Dataset shape: {df.shape}")
        print("\nFirst few rows:")
        print(df.head())
    except FileNotFoundError:
        print("sales_data.csv not found. Creating sample data...")
        create_sample_data()
        df = pd.read_csv('sales_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    # calculate_total_revenue
    total_revenue = df['Revenue ($)'].sum()

    # Find the best-selling product by quantity
    product_sales = df.groupby('Product')['Quantity Sold'].sum()
    best_selling_product = product_sales.idxmax()
    best_selling_quantity = product_sales.max()

    # Identify the days with the highest revenue
    daily_sales = df.groupby('Date')['Revenue ($)'].sum()
    best_day = daily_sales.idxmax()
    best_day_revenue = daily_sales.max()

    # Prepare insights
    insights = f"""Sales Data Analysis Summary
================================
Total Revenue: ${total_revenue:,.2f}

Best-Selling Product: {best_selling_product}
Quantity Sold: {best_selling_quantity}

Day with Highest Sales: {best_day}
Revenue on that day: ${best_day_revenue:,.2f}

Additional Insights:
- Average daily revenue: ${daily_sales.mean():,.2f}
- Total units sold: {df['Quantity Sold'].sum():,}
- Number of transactions: {len(df):,}
- Top 3 products by revenue:
"""
# Add top 3 products by revenue
    product_revenue = df.groupby('Product')['Revenue ($)'].sum().sort_values(ascending=False)
    for i, (product, revenue) in enumerate(product_revenue.head(3).items(), 1):
        insights += f"  {i}. {product}: ${revenue:,.2f}\n"
    
    # Save results to file
    with open('sales_summary.txt', 'w') as file:
        file.write(insights)
    
    print("\n"+"*"*50)
    print("Sales Data Analysis Summary")
    print("*"*50)
    print(insights)
    print("Results have been saved to 'sales_summary.txt'")

    if __name__ == "__main__":
        create_sample_data()
        analyze_sales_data()