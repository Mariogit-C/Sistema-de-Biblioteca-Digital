from .material import Material

class Revista(Material):
    """
    Clase que representa una revista, hereda de Material.
    """

    def __init__(self, titulo, autor, precio, edicion):
        """
        Constructor de la clase Revista.

        Args:
            titulo (str): Título de la revista.
            autor (str): Autor de la revista.
            precio (float): Precio de la revista.
            edicion (int): Número de edición de la revista.
        """
        super().__init__(titulo, autor, precio)
        self.edicion = edicion

    def descripcion(self):
        """
        Sobrescribe el método descripcion de la clase padre para mostrar
        información específica de las revistas.

        Returns:
            str: Descripción detallada de la revista.
        """
        return f"Revista: {self.titulo}, Autor: {self.autor}, Edición: {self.edicion}, Precio: ${self.precio:,.2f}"