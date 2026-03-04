class Tag:
    def __init__(self, name: str):
        self.__name = name

    def __eq__(self, other) -> bool:
        return isinstance(other, Tag) and other.__name == self.__name

    def __hash__(self) -> int:
        return self.hash(self.__name)

    def __repr__(self) -> str:
        return f"Name: {self.__name}"
