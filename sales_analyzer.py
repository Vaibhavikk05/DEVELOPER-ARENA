def analyze_sales(sales_data):
    total_sales = 0
    product_sales = {}
    
    for product, quantity, price in sales_data:
        sale_amount = quantity * price
        total_sales += sale_amount
        
        if product in product_sales:
            product_sales[product]['quantity'] += quantity
            product_sales[product]['revenue'] += sale_amount
        else:
            product_sales[product] = {
                'quantity': quantity,
                'revenue': sale_amount
            }
    
    best_selling_product = max(product_sales.items(), key=lambda x: x[1]['quantity'])
    highest_revenue_product = max(product_sales.items(), key=lambda x: x[1]['revenue'])
    
    return total_sales, product_sales, best_selling_product, highest_revenue_product

def print_report(total_sales, product_sales, best_selling_product, highest_revenue_product):
    print("\n" + "=" * 60)
    print("                    SALES ANALYSIS REPORT")
    print("=" * 60)
    
    print(f"\nTOTAL SALES REVENUE: ${total_sales:,.2f}")
    
    print("\n" + "-" * 60)
    print("PRODUCT-WISE BREAKDOWN:")
    print("-" * 60)
    print(f"{'Product':<20} {'Quantity':<15} {'Revenue':<15}")
    print("-" * 60)
    
    for product, data in sorted(product_sales.items()):
        print(f"{product:<20} {data['quantity']:<15} ${data['revenue']:,.2f}")
    
    print("\n" + "-" * 60)
    print("KEY INSIGHTS:")
    print("-" * 60)
    print(f"Best Selling Product (by quantity): {best_selling_product[0]}")
    print(f"  - Units Sold: {best_selling_product[1]['quantity']}")
    print(f"  - Revenue: ${best_selling_product[1]['revenue']:,.2f}")
    
    print(f"\nHighest Revenue Product: {highest_revenue_product[0]}")
    print(f"  - Units Sold: {highest_revenue_product[1]['quantity']}")
    print(f"  - Revenue: ${highest_revenue_product[1]['revenue']:,.2f}")
    
    print("\n" + "=" * 60)

def main():
    print("=" * 60)
    print("           SALES DATASET ANALYZER")
    print("=" * 60)
    
    sales_data = []
    
    try:
        num_entries = int(input("\nHow many sales entries do you want to add? "))
        
        if num_entries <= 0:
            print("Please enter a positive number of entries!")
            return
        
        for i in range(num_entries):
            print(f"\n--- Entry {i + 1} ---")
            product = input("Product name: ").strip()
            quantity = int(input("Quantity sold: "))
            price = float(input("Price per unit: $"))
            
            if quantity < 0 or price < 0:
                print("Error: Quantity and price must be positive!")
                return
            
            sales_data.append((product, quantity, price))
        
        total_sales, product_sales, best_selling_product, highest_revenue_product = analyze_sales(sales_data)
        
        print_report(total_sales, product_sales, best_selling_product, highest_revenue_product)
        
    except ValueError:
        print("\nError: Please enter valid numbers for quantity and price!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
