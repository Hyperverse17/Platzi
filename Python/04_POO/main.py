from classes import Book

print()
#print(help(Book)) # help() Muestra toda la estructura de la clase
print(Book.__doc__) # Muestra el docstring de la clase

book1 = Book("origen", "dan brown", 2017, "unknown", True)
book2 = Book("El último secreto", "dan brown", 2025, "unknown", True)
book3 = Book("morir con cero", "bill perkins", 2022, "978-84-9111-902-9", True)
book4 = Book("misery", "stephen king", 1987, "unknown", True)
book5 = Book("cementerio de animales", "stephen king", 1983, "unknown", True)

print()
bookshelf = [book1, book2, book3, book4, book5]
cnt = 1

for book in bookshelf:
    print(f"Libro {cnt}: {book} [{book.borrows}]")
    cnt += 1

print()

book1.borrowing()
book2.borrowing()
book1.returning()
book1.borrowing()
book2.returning()
book2.borrowing()
book3.borrowing()
book4.borrowing()
book2.returning()
book2.borrowing()

book1.returning()
book1.borrowing()

print()

borrows = [b.borrows for b in Book.instances] # Se obtiene una lista del atriuto borrows 
print(borrows)
print()

popularPos = borrows.index(max(borrows)) # Forma de obtener la posición del número máximo de una lista

mostPopular = Book.instances[popularPos]

print(f"Libro más popular: {mostPopular.title} de {mostPopular.author}")
print()
