import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import SQL.BD as BD

def ventana_registro_trabajador(rut_usuario):
    # Crear la ventana y los elementos del formulario (similar a ventana_registro)
    ventana_trabajador = tk.Tk()
    ventana_trabajador.title("Datos del Trabajador")

    trabajador = BD.obtener_trabajador_por_rut(rut_usuario)

    if trabajador:
        # Crear etiquetas para mostrar los datos del trabajador
        label_nombre = ttk.Label(ventana_trabajador, text=f"Nombre: {trabajador.nombre}")
        # ... (crear etiquetas para otros datos)

        # Crear un Treeview para mostrar los contactos y familiares
        tree = ttk.Treeview(ventana_trabajador, columns=("Nombre", "Teléfono", "Relación"))
        tree.heading("Nombre", text="Nombre")
        tree.heading("Teléfono", text="Teléfono")
        tree.heading("Relación", text="Relación")

        # Obtener los contactos y familiares del trabajador desde la base de datos
        contactos = BD.obtener_contactos_trabajador(rut_usuario)
        for contacto in contactos:
            tree.insert("", "end", values=(contacto.nombre, contacto.telefono, contacto.relacion))

        tree.pack()
    else:
        messagebox.showinfo("Información", "Aún no estás asignado, vuelve más tarde.")

    ventana_trabajador.mainloop()

    # Mostrar la ventana
    ventana_registro_trabajador.mainloop()