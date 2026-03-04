from product.Product import Product

class Inventory:

    def __init__(self):
        self.__products = dict()

    def add_product(self, product: Product) -> None:
        key = product.get_sku()
        if key not in self.__products.keys():
            self.__products[key] = product

    def get_product(self, sku: str) -> Product | None:
        return self.__products[sku] if sku in self.__products.keys() else None
        
    def generate_inventory_report(self) -> str:
       products_info = [product.get_info() for product in self.__products.values()]

       return "\\n".join(products_info)

    def __repr__(self) -> str:
        return f"Inventory({len(self.products)} products)"
    
if __name__ == "__main__":
    inventory = Inventory()

    product_one = Product("name", "sku", 100.11122, 300)

    inventory.add_product(product_one)

    print(inventory.get_product("sku").check_stock(301))

    print(inventory.generate_inventory_report())