import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Clases.Usuarios as Usuarios
import SQL.BD as BD
import Registrar
import MainAdmin

def login():
    nombre_usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if not nombre_usuario or not contrasena:
        messagebox.showerror("Error", "Por favor, ingresa un nombre de usuario y una contraseña.")
        return

    usuario_db = BD.verificar_usuario(nombre_usuario, contrasena)

    if usuario_db:
        usuario_app = Usuarios.Usuario(usuario_db.id, usuario_db.nombre_usuario, usuario_db.contrasena, usuario_db.rol)
        if usuario_app.rol == 'Administrador':
            messagebox.showinfo("Éxito", "Bienvenido, administrador")
            # se abre la ventana de administrador
            ventana_admin = tk.Tk()
            ventana_admin.title("Panel de Administrador")
            # ... (Código para configurar la ventana de administrador)
            MainAdmin.iniciar_ventana(ventana_admin)  # Llamamos a la función para iniciar la ventana principal
            ventana_login.destroy()  # Cerramos la ventana de login
        else:
            messagebox.showinfo("Éxito", f"Bienvenido, {usuario_app.nombre_usuario}")
            # se abre la ventana para trabajadores
    else:
        # se da un error de credenciales
        messagebox.showerror("Error", "Credenciales incorrectas")

ventana_login = tk.Tk()
ventana_login.title("Iniciar Sesión")
ventana_login.geometry("300x200")

#Los labels y campos

label_usuario = ttk.Label(ventana_login, text="Usuario:")
label_usuario.pack()
entry_usuario = ttk.Entry(ventana_login)
entry_usuario.pack()

label_contrasena = ttk.Label(ventana_login, text="Contraseña:")
label_contrasena.pack()
entry_contrasena = ttk.Entry(ventana_login, show="*")
entry_contrasena.pack()

#botones para iniciar sesion o para ir a registrarce

boton_login = ttk.Button(ventana_login, text="Iniciar Sesión", command=login)
boton_login.pack()

boton_registro = ttk.Button(ventana_login, text="¿No tienes una cuenta? Registrarte", command=lambda: [ventana_login.destroy(), Registrar.ventana_registro.mainloop()])
boton_registro.pack()

ventana_login.mainloop()

