from .material import Material

class Libro(Material):
    """
    Clase que representa un libro, hereda de Material.
    Esta relación padre-hijo permite reutilizar atributos y métodos comunes.
    """

    def __init__(self, titulo, autor, precio, paginas):
        """
        Constructor de la clase Libro.

        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            precio (float): Precio del libro.
            paginas (int): Cantidad de páginas del libro.
        """
        super().__init__(titulo, autor, precio)
        self.paginas = paginas

    def descripcion(self):
        """
        Sobrescribe el método descripcion de la clase padre para mostrar
        información específica de los libros.

        Returns:
            str: Descripción detallada del libro.
        """
        return f"Libro: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}, Precio: ${self.precio:,.2f}"