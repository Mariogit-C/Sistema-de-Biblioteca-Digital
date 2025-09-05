from .material import Material
from typing import List

class Biblioteca:
    def __init__(self):
        self.catalogo: List[Material] = []

    def agregar_material(self, material: Material):
        """
        Agrega un material al catálogo, verificando que sea una instancia de Material.

        Args:
            material (Material): El objeto material a agregar.
        """
        if isinstance(material, Material):
            self.catalogo.append(material)
        else:
            print(f"Error: El objeto proporcionado no es un material válido.")

    def mostrar_catalogo(self):
        if not self.catalogo:
            print("El catálogo de la biblioteca está vacío.")
            return

        print("--- Catálogo de la Biblioteca ---")
        total = 0
        for material in self.catalogo:
            print(material.descripcion())
            total += material.precio
        print("---------------------------------")
        # Usamos :,.2f para formatear el número con separador de miles
        print(f"Valor total del catálogo: ${total:,.2f}\n")