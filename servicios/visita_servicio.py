from modelos.visitante import Visitante
#Aqui se ejecuta lo mas importante, es como el cerebro de todo el sistema 

class VisitaServicio:
    def __init__(self):
        self.__visitantes = [] #Lista donode se guarda los visiatantes.

    def agregar_visitante(self, cedula, nombre, motivo):
        for v in self.__visitantes: #Revisa que la cedula no este repetida.
            if v.cedula == cedula:
                raise ValueError(f"Y existe un usuario con las cédula {cedula}.")
        nuevo = Visitante(cedula, nombre, motivo) # Crea el visitante
        self.__visitantes.append(nuevo) # ESta función lo agrega a la lista 

    def obtener_visitantes(self):
        return list(self.__visitantes) # Esta función devuelve todos los visitantes

    def eliminar_visitante(self, cedula):
        for v in self.__visitantes:
            if v.cedula == cedula:
                self.__visitantes.remove(v) # Lo borra de la lista 
                return True
        return False # No se lo encontró