from classes import Book

try:
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
        print(f"Libro {cnt}: {book}") # en este caso al llamar a la instancia se toma por defecto el __str__ definido dentro de la clase
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
    book2.returning()
    book1.returning()

    book1.borrowing()
    book1.returning()
    book2.borrowing()
    book2.returning()
    book1.borrowing()
    book1.returning()
    book2.borrowing()
    book2.returning()

    print()

    cnt = 1
    for book in bookshelf:
        print(f"Libro {cnt}: {book}")
        cnt += 1

# Acceso a atributos privados
    print("\nAccediendo a atributos privados...")
    #print(f"Borrows: {book1.__borrows}") # Intentar acceder directamente detona un AttributeError
    cnt = 1
    for book in bookshelf:
        print(f"Libro {cnt}: {book} [{book.getAttribute("borrows")} veces prestado]")
        cnt += 1

    print("***")
    book1.resetBorrows()
    cnt = 1
    for book in bookshelf:
        print(f"Libro {cnt}: {book} [{book.getAttribute("borrows")} veces prestado]")
        cnt += 1


    
    
    
except AttributeError as error:
    print(f"\nParece que estas accediendo a un atributo privado\nError: {error}")

finally:
    print("\nFin del programa\n")

