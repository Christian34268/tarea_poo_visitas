# CAPA MODELO: visitantes.py
# Define la estructura de datos de un Visitante.
# Es solo un molde, no posee logica solo atributos.
class Visitante:
    def __init__(self, cedula, nombre, motivo):
        self.cedula = cedula   # Identificador único del visitante 
        self.nombre = nombre   # Nombre completo de la persona 
        self.motivo = motivo   # Razón por la que la persona visita la oficina