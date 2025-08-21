import pytest
import json
import os
from typing import Any
from main import load_inventory, summarize_by_category, apply_discount

@pytest.fixture
def temp_json_file(tmp_path):
    """Create a temporary JSON file for testing."""
    file_path = tmp_path / "test_inventory.json"
    data = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10, "price": 999.99},
        {"name": "Mouse", "category": "Electronics", "quantity": 3, "price": 29.99}
    ]
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return str(file_path)

@pytest.fixture
def invalid_json_file(tmp_path):
    """Create a temporary invalid JSON file."""
    file_path = tmp_path / "invalid_inventory.json"
    with open(file_path, 'w') as f:
        f.write("not json")
    return str(file_path)

def test_load_inventory(temp_json_file: str) -> None:
    """Test loading valid JSON inventory."""
    products = load_inventory(temp_json_file)
    expected = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10, "price": 999.99},
        {"name": "Mouse", "category": "Electronics", "quantity": 3, "price": 29.99}
    ]
    assert products == expected, "Should load valid JSON correctly"

def test_load_inventory_edge_cases(invalid_json_file: str) -> None:
    """Test edge cases for load_inventory."""
    # Invalid JSON
    assert load_inventory(invalid_json_file) == [], "Invalid JSON should return empty list"
    
    # Non-existent file
    assert load_inventory("non_existent.json") == [], "Missing file should return empty list"
    
    # Non-list JSON
    temp_file = invalid_json_file.replace("invalid", "non_list")
    with open(temp_file, 'w') as f:
        json.dump({"invalid": "data"}, f)
    assert load_inventory(temp_file) == [], "Non-list JSON should return empty list"

def test_summarize_by_category() -> None:
    """Test summarizing products by category."""
    products: list[dict[str, Any]] = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10, "price": 999.99},
        {"name": "Mouse", "category": "Electronics", "quantity": 3, "price": 29.99},
        {"name": "Desk", "category": "Furniture", "quantity": 2, "price": 149.99}
    ]
    expected: dict[str, int] = {"Electronics": 13, "Furniture": 2}
    assert summarize_by_category(products) == expected, "Should summarize quantities by category"

def test_summarize_by_category_edge_cases() -> None:
    """Test edge cases for summarize_by_category."""
    # Empty list
    assert summarize_by_category([]) == {}, "Empty list should return empty dict"
    
    # Invalid products
    products: list[dict[str, Any]] = [
        {"name": "Invalid", "category": "Electronics", "quantity": "5"},
        {"name": "Missing"},
        None
    ]
    assert summarize_by_category(products) == {}, "Invalid products should return empty dict"

def test_apply_discount() -> None:
    """Test applying discounts to low-stock products."""
    products: list[dict[str, Any]] = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10, "price": 1000.0},
        {"name": "Mouse", "category": "Electronics", "quantity": 3, "price": 30.0}
    ]
    result = apply_discount(products, threshold=5, discount=0.1)
    expected = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10, "price": 1000.0},
        {"name": "Mouse", "category": "Electronics", "quantity": 3, "price": 27.0}
    ]
    assert result == expected, "Should apply discount to low-stock items"

def test_apply_discount_edge_cases() -> None:
    """Test edge cases for apply_discount."""
    # Empty list
    assert apply_discount([]) == [], "Empty list should return empty list"
    
    # Invalid products
    products: list[dict[str, Any]] = [
        {"name": "Invalid", "quantity": 3},
        {"name": "Missing", "price": 30.0},
        None
    ]
    assert apply_discount(products) == [], "Invalid products should return empty list"
