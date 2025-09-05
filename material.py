class Material:
    """
    Clase base que representa un material genérico de la biblioteca.
    """

    def __init__(self, titulo, autor, precio):
        """
        Constructor de la clase Material.

        Args:
            titulo (str): Título del material.
            autor (str): Autor del material.
            precio (float): Precio del material.
        """
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio  # Atributo encapsulado

    @property
    def precio(self):
        """
        Método para obtener el precio del material.

        Returns:
            float: Precio del material.
        """
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        """
        Método para establecer un nuevo precio, validando que sea mayor a 0.

        Args:
            nuevo_precio (float): Nuevo precio a establecer.
        """
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio debe ser un número positivo.")

    def descripcion(self):
        """
        Método que devuelve una descripción general del material.

        Returns:
            str: Descripción del material.
        """
        return f"Material: {self.titulo}, Autor: {self.autor}"