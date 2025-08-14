"""Variable types"""

import json
from typing import Any


def load_inventory(file_path: str) -> list[dict[str, Any]]:
    """Reads JSON and returns a list of product dictionaries."""

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("JSON file must contain a list of products")
            return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}.")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []


def summarize_by_category(products: list[dict[str, Any]]) -> dict[str, int]:
    """Groups products by category and sums quantities."""

    summary: dict[str, int] = {}
    for product in products:
        try:
            category = product["category"]
            quantity = product["quantity"]

            if not isinstance(quantity, int):
                raise ValueError(
                    f"Invalid quantity for {product.get('name','unknown')}"
                )
            summary[category] = summary.get(category, 0) + quantity
        except (KeyError, TypeError, ValueError) as e:
            print(f"Error processing product: {e}")
            continue
    return summary


def apply_discount(
    products: list[dict[str, Any]], threshold: int = 5, discount: float = 0.1
) -> list[dict[str, Any]]:
    """Reduces price for products with quantity below threshold"""

    updated_products: list[dict[str, Any]] = []
    for product in products:
        if not product:
            continue
        try:
            update_product = product.copy()
            if update_product["quantity"] < threshold:
                update_product["price"] *= 1 - discount
            updated_products.append(update_product)
        except (KeyError, TypeError) as e:
            print(f"Error applying discount: {e}")
            continue
    return updated_products


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
