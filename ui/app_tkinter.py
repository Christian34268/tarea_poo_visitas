# Aqui se maneja todo lo visual tales cosas como botones, ventana, campos, tablas.
import tkinter as tk
from tkinter import ttk, messagebox  # ttk para la tabla, messagebox para los popups de alerta

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root          # La ventana principal
        self.servicio = servicio  # El servicio que maneja los datos (cerebro)

        self.root.title("Sistema de Registro de Visitantes")  # Título de la ventana
        self.root.geometry("700x500")      # Tamaño de la ventana
        self.root.resizable(False, False)  # No se puede cambiar el tamaño
        self.root.configure(bg="#f0f4f8")  # Color de fondo gris claro

        self._construir_ui()  # Llama al método que dibuja todo lo visual

    def _construir_ui(self):
        # Título
        titulo = tk.Label(
            self.root,
            text="🏢 Registro de Visitantes",
            font=("Helvetica", 18, "bold"),
            bg="#3e4b58",  # Fondo azul oscuro
            fg="white",    # Texto blanco
            pady=12
        )
        titulo.pack(fill=tk.X)  # Se estira en todo el ancho de la ventana

        # Formulario
        frame_form = tk.LabelFrame(
            self.root,
            text="Datos del Visitante",  # Título del recuadro
            font=("Helvetica", 11, "bold"),
            bg="#f0f4f8",
            fg="#2c3e50",
            padx=15,
            pady=10
        )
        frame_form.pack(fill=tk.X, padx=20, pady=10)  # Ocupa todo el ancho con margen

        # Campo cédula: etiqueta + caja de texto
        tk.Label(frame_form, text="Cédula:", bg="#f0f4f8", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w", pady=4)
        self.entry_cedula = tk.Entry(frame_form, width=30, font=("Helvetica", 10))
        self.entry_cedula.grid(row=0, column=1, padx=10, pady=4)

        # Campo nombre: etiqueta + caja de texto
        tk.Label(frame_form, text="Nombre completo:", bg="#f0f4f8", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w", pady=4)
        self.entry_nombre = tk.Entry(frame_form, width=30, font=("Helvetica", 10))
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=4)

        # Campo motivo: etiqueta + caja de texto
        tk.Label(frame_form, text="Motivo de visita:", bg="#f0f4f8", font=("Helvetica", 10)).grid(row=2, column=0, sticky="w", pady=4)
        self.entry_motivo = tk.Entry(frame_form, width=30, font=("Helvetica", 10))
        self.entry_motivo.grid(row=2, column=1, padx=10, pady=4)

        # Botones
        frame_botones = tk.Frame(self.root, bg="#f0f4f8")
        frame_botones.pack(pady=5)

        # Botón verde: guarda el visitante
        tk.Button(
            frame_botones, text="✅ Registrar", width=15,
            bg="#1e5033", fg="white", font=("Helvetica", 10, "bold"),
            command=self._registrar  # Al hacer clic llama a _registrar
        ).grid(row=0, column=0, padx=8)

        # Botón rojo: borra el visitante seleccionado
        tk.Button(
            frame_botones, text="❌ Eliminar", width=15,
            bg="#79190e", fg="white", font=("Helvetica", 10, "bold"),
            command=self._eliminar  # Al hacer clic llama a _eliminar
        ).grid(row=0, column=1, padx=8)

        # Botón azul: limpia los campos del formulario
        tk.Button(
            frame_botones, text="🧹 Limpiar", width=15,
            bg="#428d92", fg="white", font=("Helvetica", 10, "bold"),
            command=self._limpiar  # Al hacer clic llama a _limpiar
        ).grid(row=0, column=2, padx=8)

        # Tabla
        frame_tabla = tk.LabelFrame(
            self.root,
            text="Lista de Visitantes",  # Título del recuadro
            font=("Helvetica", 11, "bold"),
            bg="#020e1a",  # Fondo oscuro
            fg="#1D5185",
            padx=10,
            pady=8
        )
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)  # Ocupa el espacio restante

        columnas = ("cedula", "nombre", "motivo")  # Nombres internos de las columnas
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)

        # Títulos visibles de cada columna
        self.tabla.heading("cedula", text="Cédula")
        self.tabla.heading("nombre", text="Nombre Completo")
        self.tabla.heading("motivo", text="Motivo de Visita")

        # Ancho de cada columna en píxeles
        self.tabla.column("cedula", width=120, anchor="center")
        self.tabla.column("nombre", width=220, anchor="w")
        self.tabla.column("motivo", width=280, anchor="w")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)  # Conecta la barra con la tabla

        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Barra al lado derecho de la tabla

    def _registrar(self):
        # Lee lo que escribió el usuario en cada campo
        cedula = self.entry_cedula.get().strip()  # .strip() quita espacios al inicio y al final
        nombre = self.entry_nombre.get().strip()
        motivo = self.entry_motivo.get().strip()

        # Si algún campo está vacío, muestra advertencia y no continúa
        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        try:
            self.servicio.agregar_visitante(cedula, nombre, motivo)  # Manda los datos al servicio
            self._actualizar_tabla()  # Refresca la tabla con el nuevo visitante
            self._limpiar()           # Limpia los campos del formulario
            messagebox.showinfo("Éxito", f"Visitante '{nombre}' registrado correctamente.")  # Mensaje de éxito
        except ValueError as e:
            messagebox.showerror("Error", str(e))  # Muestra el error si la cédula ya existe

    def _eliminar(self):
        seleccion = self.tabla.selection()  # Obtiene la fila que el usuario seleccionó
        if not seleccion:
            messagebox.showwarning("Sin selección", "Selecciona un visitante de la tabla para eliminar.")
            return  # Si no hay selección, avisa y para

        item = self.tabla.item(seleccion[0])  # Obtiene los datos de la fila seleccionada
        cedula = item["values"][0]  # Saca la cédula de la primera columna
        nombre = item["values"][1]  # Saca el nombre de la segunda columna

        confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar a '{nombre}'?")  # Pide confirmación
        if confirmar:
            self.servicio.eliminar_visitante(cedula)  # Le dice al servicio que lo borre
            self._actualizar_tabla()  # Refresca la tabla
            self._limpiar()           # Limpia los campos

    def _limpiar(self):
        self.entry_cedula.delete(0, tk.END)  # Borra el campo cédula
        self.entry_nombre.delete(0, tk.END)  # Borra el campo nombre
        self.entry_motivo.delete(0, tk.END)  # Borra el campo motivo

    def _actualizar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)  # Borra todas las filas visibles de la tabla
        for v in self.servicio.obtener_visitantes():
            self.tabla.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))  # Vuelve a llenar la tabla con los datos actuales