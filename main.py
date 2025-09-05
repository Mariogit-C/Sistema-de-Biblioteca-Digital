from src.libro import Libro
from src.revista import Revista
from src.periodico import Periodico
from src.biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    libro = Libro("Python para Todos", "Charles Severance", 15000, 300)
    revista = Revista("Tech Monthly", "Ana Torres", 5000, 42)
    periodico = Periodico("El Informador", "Luis Pérez", 1000, "04/09/2025")

    # Usamos la propiedad para cambiar el precio de forma más natural
    libro.precio = 16000

    biblioteca.agregar_material(libro)
    biblioteca.agregar_material(revista)
    biblioteca.agregar_material(periodico)

    biblioteca.mostrar_catalogo()

if __name__ == "__main__":
    main()