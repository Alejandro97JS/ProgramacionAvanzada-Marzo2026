# pyproject.toml ha ganado popularidad en gestión de dependencias para
# proyectos Python.

# Name mangling para conseguir hacer llamadas a métodos privados:
# https://www.geeksforgeeks.org/python/name-mangling-in-python/

# Atributo privado con "sentido" solamente interno
class Mortgage:

    def __init__(self, amount, rate):
        self.amount = amount
        self.rate = rate
        self.__is_conceded = None

    def __calculate_is_conceded(self):
        self.__is_conceded= self.amount < 200000 and self.rate > 0.02
    
    def check_is_conceded(self):
        if self.__is_conceded is None:
            self.__calculate_is_conceded()
        return self.__is_conceded
    
    def modify_rate(self, new_rate):
        self.rate = new_rate
        self.__calculate_is_conceded()

if __name__=="__main__":
    my_mortage = Mortgage(100000, 0.021)
    my_mortage.check_is_conceded()
    my_mortage.modify_rate(0.015)

# Handler de excepciones, 404s...
# https://fastapi.tiangolo.com/es/tutorial/handling-errors/


# Autenticación por OAuth:

# 1 - Servidor tiene un endpoint GET /token
# 2 - Cliente le manda una request a /token con sus credenciales
# 3 - Servidor devuelve un token ...asdfipkashdfhkasdf... y un tiempo de validez (5 min)
# 4 - Las siguientes requests que haga el cliente a los endpoints del servidor, debe enviar ese token
# y el servidor es el dato que usa para validar.
