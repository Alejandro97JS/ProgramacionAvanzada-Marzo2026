class Product:
    def __init__(self, name: str, sku: str, price: float, current_stock: int = 0,
                 categories: list = None, tags: list = None):
        self.__name = name
        self.__sku = sku
        self.__price = price
        self.__current_stock = current_stock
        self.__categories = [] if categories is None else categories
        self.__tags = [] if tags is None else tags

    def check_stock(self, requested_units: int) -> tuple[bool, int]:
        return (True, requested_units) if requested_units <= self.__current_stock else (False, self.__current_stock)

    def update_stock(self, amount: int) -> None:
        self.__current_stock += amount

    def get_info(self) -> str:
        print_sku = f"(SKU: {self.__sku})"
        print_price = f"${self.__price:.2f}"
        print_stock = f"{self.__current_stock}"
        print_categories = ",".join([cat for cat in self.__categories]) or "N/A"
        print_tags = ",".join([t for t in self.__tags]) or "N/A"

        return f"Product: {self.__name} {print_sku} - Price: {print_price}, Stock: {print_stock}, Categories: {print_categories}, Tags: {print_tags}"

    def get_sku(self) -> str:
        return self.__sku
    
    def get_current_stock(self) -> int:
        return self.__current_stock

    def get_price(self) -> int:
        return self.__price
               
    def __repr__(self) -> str:
        return f"""- Name: {self.__name} 
                   - SKU: {self.__sku} 
                   - Price: {self.__price}
                   - Stock: {self.__current_stock} 
                   - Categories: {[",".join(n) for n in self.__categories]}
                   - Tags: {[",".join(t) for t in self.__tags]}"""