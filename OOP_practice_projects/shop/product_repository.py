from typing import List, Optional

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        return next((p for p in self.products if p.name == product_name), None)

    def remove(self, product_name):
        if product_name in self.products:
            self.products.remove(product_name)

    def __repr__(self):
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])





