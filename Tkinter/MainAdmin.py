import tkinter as tk
from tkinter import ttk
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("El Correo de Yury")

# Crear una tabla para mostrar los trabajadores
tabla_trabajadores = ttk.Treeview(ventana, columns=("rut", "nombre", "cargo", "area"))
tabla_trabajadores.heading("rut", text="RUT")
tabla_trabajadores.heading("nombre", text="Nombre")
tabla_trabajadores.heading("cargo", text="Cargo")
tabla_trabajadores.heading("area", text="Área")
tabla_trabajadores.pack()

# Función para listar trabajadores
def listar_trabajadores():
    cursor.execute("SELECT rut, nombre, cargo, area FROM trabajadores")
    resultados = cursor.fetchall()
    tabla_trabajadores.delete(*tabla_trabajadores.get_children())  # Limpiar la tabla
    for row in resultados:
        tabla_trabajadores.insert('', 'end', values=row)

# Menú de navegación
menubar = tk.Menu(ventana)

# Menú Trabajadores
menu_trabajadores = tk.Menu(menubar, tearoff=0)
menu_trabajadores.add_command(label="Listar trabajadores", command=listar_trabajadores)
# ... (otros comandos para agregar, editar, eliminar, buscar)
menubar.add_cascade(label="Trabajadores", menu=menu_trabajadores)

# ... (crear menús para Contactos, Cargas Familiares, Reportes y Usuarios)

ventana.config(menu=menubar)

# Mostrar la ventana
ventana.mainloop()