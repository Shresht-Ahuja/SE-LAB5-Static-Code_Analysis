"""Inventory Management System Module.

This module provides classes and functions for managing an inventory
of products. It includes features for adding, updating, deleting, and
displaying products, with built-in validation and error handling.
"""

import logging
from typing import List, Dict, Optional


class InventoryError(Exception):
    """Custom exception for inventory-related errors."""
    pass


class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id: int, name: str, quantity: int, price: float) -> None:
        """Initialize a product with ID, name, quantity, and price."""
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative values.")
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, new_quantity: int) -> None:
        """Update product quantity after validating input."""
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = new_quantity

    def __repr__(self) -> str:
        """Return a readable string representation of the product."""
        return f"Product({self.product_id}, '{self.name}', qty={self.quantity}, price={self.price:.2f})"


class Inventory:
    """Manages a collection of products."""

    def __init__(self) -> None:
        """Initialize an empty inventory."""
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product) -> None:
        """Add a product to the inventory."""
        if product.product_id in self.products:
            raise InventoryError(f"Product ID {product.product_id} already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id: int) -> None:
        """Remove a product from the inventory."""
        if product_id not in self.products:
            raise InventoryError(f"Product ID {product_id} not found.")
        del self.products[product_id]

    def update_product(self, product_id: int, new_quantity: Optional[int] = None,
                       new_price: Optional[float] = None) -> None:
        """Update a product’s quantity or price."""
        if product_id not in self.products:
            raise InventoryError(f"Product ID {product_id} not found.")

        product = self.products[product_id]
        if new_quantity is not None:
            product.update_quantity(new_quantity)
        if new_price is not None:
            if new_price < 0:
                raise ValueError("Price cannot be negative.")
            product.price = new_price

    def list_products(self) -> List[Product]:
        """Return a list of all products in the inventory."""
        return list(self.products.values())


def main() -> None:
    """Main function to demonstrate inventory management."""
    logging.basicConfig(
        filename="inventory.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    inventory = Inventory()

    try:
        product1 = Product(1, "Laptop", 10, 75000.00)
        product2 = Product(2, "Mouse", 50, 500.00)

        inventory.add_product(product1)
        inventory.add_product(product2)
        inventory.update_product(2, new_price=550.00)

        for item in inventory.list_products():
            logging.info("Inventory Item: %s", item)

    except (InventoryError, ValueError) as err:
        logging.error("Error: %s", err)


if __name__ == "__main__":
    main()
