from ..product.Product import Product

class Order:

    def __init__(self, order_id: str):
        self.__order_id = order_id
        self.__products = dict()

    def add_product(self, product: Product, quantity: int) -> None:
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a positive integer value")
        if product is None:
            raise ValueError("Product must be defined")

        if product.get_sku() in self.__products.keys():
            self.__products[product.get_sku()]['quantity'] += quantity
        self.__products[product.get_sku()] = {"product": product, "quantity": quantity}

    def buy(self) -> str:
        total = 0
        for product_order in self.__products.values():
            product = product_order.get("product")
            quantity = product_order.get("quantity")

            if not product.check_stock(quantity)[0]:
                print(f"There's not sufficient stock. current stock: {product.get_current_stock()}")
                continue
            else:
                total += quantity * product.get_price()
                product.update_stock(-quantity)
        
        return f"Order ID: {self.__order_id} - Total: ${total:.2f}  - Purchase Completed"

    def __repr__(self) -> str:
        index = 0
        str = f"- Order ID: {self.__order_id}"
        for ordered_product in self.__products.values():
            str += f"\n\t- Product {index}: {ordered_product['product'].get_info()}"""
            index += 1
        return str
        
if __name__ == "__main__":
    p1 = Product("Laptop", "SKU123", 1200, 10)
    p2 = Product("Mouse", "SKU456", 25, 100)

    order = Order("ORDER001")
    order.add_product(p1, 2)
    order.add_product(p2, 5)

    print(order.buy())
    # -> Order ID: ORDER001 - Total: $2525.00 - Purchase Completed
    
    print(order)