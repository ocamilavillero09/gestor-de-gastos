from datetime import datetime

class Transaccion:
    """
    Clase que representa una transacción financiera.
    Puede ser de tipo 'ingreso' o 'gasto'.
    """
    
    def __init__(self, id_transaccion: int, usuario_id: int, categoria_id: int, tipo: str, monto: float, fecha: datetime):
        """
        Inicializa una nueva transacción.

        :param id_transaccion: Identificador único de la transacción.
        :param usuario_id: Identificador del usuario que realizó la transacción.
        :param categoria_id: Identificador de la categoría de la transacción.
        :param tipo: Tipo de transacción ('ingreso' o 'gasto').
        :param monto: Monto de la transacción.
        :param fecha: Fecha en la que se realizó la transacción.
        """
        self.id_transaccion = id_transaccion
        self.usuario_id = usuario_id
        self.categoria_id = categoria_id
        self.tipo = tipo
        self.monto = monto
        self.fecha = fecha

    def __str__(self):
        """
        Devuelve una representación en cadena de la transacción.

        :return: Cadena con la fecha, tipo y monto de la transacción.
        """
        return f"[{self.fecha}] {self.tipo.upper()} - ${self.monto}"


