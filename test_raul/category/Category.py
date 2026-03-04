class Category:
    def __init__(self, name: str, description: str = ""):
        self.__name = name
        self.__description = description
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Category) and self.__name == other.__name

    def __hash__(self) -> int:
        return self.hash(self.__name)
    
    def __repr__(self) -> str:
        return f"Name: {self.__name}; Description: {self.__description}"