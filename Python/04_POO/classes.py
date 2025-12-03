class Book:
    """Clase para instanciar Libros"""
    instances = []

    def __init__(self, title:str, author:str, year:int, isbn:str, available:bool):
        """Método constructor"""
        self.instances.append(self) # Sirve para crear una lista donde se van a guardar todas las instancias de esta clase
        self.title = title.title()
        self.author = author.title()
        self.year = year
        self.isbn = isbn.upper()
        self.available = available
#       Colocar un guion bajo es una forma de anotar que la variable/método no debería ser modificada externamente o acceder externamente, sin embargo, Python lo permitiría 
#       colocar doble guion bajo hace reales estas restricciones 
        self.__borrows = 0
        self.__popular = False

    def __str__(self) -> str:
        """Método Default que retorna un string con información de cada instancia Book"""
        return f"{self.title} ({self.year}) by {self.author}. Availability: {self.available}, Is Popular: {self.__popular}"
    
    def borrowing(self):
        """Cambia la disponibilidad a False"""
        if self.available == True:
            self.available = False
            self.__borrows += 1 # Con doble guion bajo sólo es posible modificar/acceder dentro de la clase

            if self.__borrows >= 5:
                self.__popular = True
            else:
                self.__popular = False

            print(f"{self.title} by {self.author} borrowed succesfully!")
        else:
            print(f"Unable to borrow {self.title} by {self.author}")
        
    def returning(self):
        """Cambia la disponibilidad a True"""
        if self.available == False:
            self.available = True
            print(f"{self.title} by {self.author} returned succesfully!")

#   getters y setters
    def getAttribute(self, attribute:str): # Método (getter) que permite acceder a atributos privados
        """Retorna atributos privados"""
        if attribute.lower() == "borrows":
            response = self.__borrows

        elif attribute.lower() == "popular":
            response = self.__popular

        else:
            response = f"No such attribute {attribute}"

        return response
    
    def resetBorrows(self): # Método (setter) que permite acceder a atributos privados
        """Reinicia el contador de préstamos"""
        self.__borrows = 0
        print("Contador de préstamos reiniciado!")

