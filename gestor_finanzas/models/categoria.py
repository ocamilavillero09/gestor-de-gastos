class Categoria:
    """
    Clase que representa una categoría para clasificar transacciones o elementos.
    """
    
    def __init__(self, id_categoria: int, nombre: str):
        """
        Inicializa una nueva categoría.

        :param id_categoria: Identificador único de la categoría.
        :param nombre: Nombre de la categoría.
        """
        self.id_categoria = id_categoria
        self.nombre = nombre