from models.transaccion import Transaccion
from datetime import datetime

class GestorTransacciones:
    def __init__(self):
        self.transacciones = []

    def registrar_transaccion(self, id_transaccion: int, usuario_id: int, categoria_id: int, tipo: str, monto: float, fecha: datetime):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        if tipo not in ["ingreso", "gasto"]:
            raise ValueError("El tipo de transacción debe ser 'ingreso' o 'gasto'")

        nueva_transaccion = Transaccion(id_transaccion, usuario_id, categoria_id, tipo, monto, fecha)
        self.transacciones.append(nueva_transaccion)

    def obtener_transacciones_por_usuario(self, usuario_id: int):
        return [t for t in self.transacciones if t.usuario_id == usuario_id]

    def filtrar_por_fecha(self, usuario_id: int, fecha_inicio: datetime, fecha_fin: datetime):
        return [t for t in self.transacciones if t.usuario_id == usuario_id and fecha_inicio <= t.fecha <= fecha_fin]
