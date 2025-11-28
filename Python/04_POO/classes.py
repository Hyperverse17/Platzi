class Book:
    """Clase para instanciar Libros"""
    instances = []

    def __init__(self, title:str, author:str, year:int, isbn:str, available:bool):
        """Método constructor"""
        self.instances.append(self)
        self.title = title.title()
        self.author = author.title()
        self.year = year
        self.isbn = isbn.upper()
        self.available = available
        self.borrows = 0

    def __str__(self) -> str:
        """Método Default que retorna un string con información de cada instancia Book"""
        return f"{self.title} ({self.year}) by {self.author}. Availability: {self.available}"
    
    def borrowing(self):
        """Cambia la disponibilidad a False"""
        if self.available == True:
            self.available = False
            self.borrows += 1
            print(f"{self.title} by {self.author} borrowed succesfully!")
        else:
            print(f"Unable to borrow {self.title} by {self.author}")
        
    def returning(self):
        """Cambia la disponibilidad a True"""
        if self.available == False:
            self.available = True
            print(f"{self.title} by {self.author} returned succesfully!")

