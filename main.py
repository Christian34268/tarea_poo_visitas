import tkinter as tk
from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppTkinter

if __name__ == "__main__":  
    root = tk.Tk()# Se crea la ventana 
    servicio = VisitaServicio()# Crea el cerebro del sistema 
    app = AppTkinter(root, servicio)# Crea la pantalla y le opasa el cerebro
    root.mainloop()#Abre la ventana y la mantiene activa 
