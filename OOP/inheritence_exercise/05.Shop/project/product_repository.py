from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            product = next(filter(lambda x: x.name == product_name, self.products))
            return product
        except StopIteration:
            pass

    def remove(self, product_name: str):
        try:
            product = next(filter(lambda x: x.name == product_name, self.products))
            self.products.remove(product)
        except StopIteration:
            pass

    def __repr__(self):
        result = "\n".join(f"{p.name}: {p.quantity}" for p in self.products)
        return result
