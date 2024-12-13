import tkinter as tk
from tkinter import ttk
from SQL import BD

# Crear la ventana principal
ventana_admin = tk.Tk()
ventana_admin.title("El Correo de Yury")

# Crear una tabla para mostrar los trabajadores
tabla_trabajadores = ttk.Treeview(ventana_admin, columns=("rut", "nombre", "cargo", "area"))
tabla_trabajadores.heading("rut", text="RUT")
tabla_trabajadores.heading("nombre", text="Nombre")
tabla_trabajadores.heading("cargo", text="Cargo")
tabla_trabajadores.heading("area", text="Área")
tabla_trabajadores.pack()

def listar_trabajadores_admin():
    datos_trabajadores = BD.obtener_trabajadores()

# Menú de navegación
menubar = tk.Menu(ventana_admin)

# Menú Trabajadores
menu_trabajadores = tk.Menu(menubar, tearoff=0)
menu_trabajadores.add_command(label="Listar trabajadores", command=listar_trabajadores_admin)
# ... (otros comandos para agregar, editar, eliminar, buscar)
menubar.add_cascade(label="Trabajadores", menu=menu_trabajadores)

# ... (crear menús para Contactos, Cargas Familiares, Reportes y Usuarios)

ventana_admin.config(menu=menubar)

# Mostrar la ventana
ventana_admin.mainloop()