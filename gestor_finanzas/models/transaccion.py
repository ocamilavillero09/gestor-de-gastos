from datetime import datetime

class Transaccion:
    def __init__(self, id_transaccion: int, usuario_id: int, categoria_id: int, tipo: str, monto: float, fecha: datetime):
        self.id_transaccion = id_transaccion
        self.usuario_id = usuario_id
        self.categoria_id = categoria_id
        self.tipo = tipo
        self.monto = monto
        self.fecha = fecha

    def __str__(self):
        return f"[{self.fecha}] {self.tipo.upper()} - ${self.monto}"

