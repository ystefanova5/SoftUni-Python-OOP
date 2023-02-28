from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            match = next(filter(lambda x: x.name == product_name, self.products))
            return match
        except StopIteration:
            pass

    def remove(self, product_name: str):
        try:
            match = next(filter(lambda x: x.name == product_name, self.products))
            self.products.remove(match)
        except StopIteration:
            pass

    def __repr__(self):
        return '\n'.join(f"{x.name}: {x.quantity}" for x in self.products)
