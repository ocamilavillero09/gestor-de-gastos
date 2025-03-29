from models.transaccion import Transaccion
from datetime import datetime

class GestorTransacciones:
    """
    Clase para gestionar las transacciones de los usuarios.
    Permite registrar transacciones, obtener transacciones por usuario
    y filtrar transacciones por fecha.
    """
    
    def __init__(self):
        """
        Inicializa una lista vacía de transacciones.
        """
        self.transacciones = []

    def registrar_transaccion(self, id_transaccion: int, usuario_id: int, categoria_id: int, tipo: str, monto: float, fecha: datetime):
        """
        Registra una nueva transacción.

        :param id_transaccion: Identificador único de la transacción.
        :param usuario_id: Identificador del usuario asociado a la transacción.
        :param categoria_id: Identificador de la categoría de la transacción.
        :param tipo: Tipo de transacción ('ingreso' o 'gasto').
        :param monto: Monto de la transacción (debe ser mayor a cero).
        :param fecha: Fecha en la que se realizó la transacción.
        :raises ValueError: Si el monto no es mayor a cero o el tipo no es válido.
        """
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        if tipo not in ["ingreso", "gasto"]:
            raise ValueError("El tipo de transacción debe ser 'ingreso' o 'gasto'")

        nueva_transaccion = {
            "id": id_transaccion,
            "usuario_id": usuario_id,
            "categoria_id": categoria_id,
            "tipo": tipo,
            "monto": monto,
            "fecha": fecha
        }

        print("Registrando transacción:", nueva_transaccion)  # Depuración

        self.transacciones.append(nueva_transaccion)


    def obtener_transacciones_por_usuario(self, usuario_id: int):
        """
        Retorna una lista de transacciones filtradas por usuario_id.
        Si no hay transacciones, devuelve una lista vacía.
        """
        return [t for t in self.transacciones if isinstance(t, dict) and t.get("usuario_id") == usuario_id]
    
    def filtrar_por_fecha(self, usuario_id: int, fecha_inicio: datetime, fecha_fin: datetime):
        """
        Filtra las transacciones de un usuario dentro de un rango de fechas.

        :param usuario_id: Identificador del usuario.
        :param fecha_inicio: Fecha de inicio del rango.
        :param fecha_fin: Fecha de fin del rango.
        :return: Lista de transacciones dentro del rango de fechas.
        """
        return [t for t in self.transacciones if t.usuario_id == usuario_id and fecha_inicio <= t.fecha <= fecha_fin]
