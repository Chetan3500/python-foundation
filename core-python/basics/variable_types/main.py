"""Variable types"""

from typing import Any
from module.variable_types import load_inventory, summarize_by_category, apply_discount

def main() -> None:
    """Main entry point of the program"""

    input_file: str = "inventory.json"
    products: list[dict[str, Any]] = load_inventory(input_file)

    if not products:
        print("No valid products to process.")
        return

    # Summarize by category
    print("Inventory Summary by Category:")
    summary = summarize_by_category(products)
    for category, quantity in summary.items():
        print(f"{category}: {quantity} items")

    # Apply discount to low-stock items
    print("\nLow-Stock Products with Discount:")
    discounted_products = apply_discount(products)
    for product in discounted_products:
        if product["quantity"] < 5:
            print(f"{product['name']}: ${product['price']:.2f} ({product['quantity']} in stock)")


if __name__ == "__main__":
    main()
