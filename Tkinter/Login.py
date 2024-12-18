import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Clases.Usuarios as Usuarios
import SQL.BD as BD
import Registrar
from Clases.Trabajadores import Trabajador

def login():
    nombre_usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if not nombre_usuario or not contrasena:
        messagebox.showerror("Error", "Por favor, ingresa un nombre de usuario y una contraseña.")
        return

    usuario_db = BD.verificar_usuario(nombre_usuario, contrasena)

    if usuario_db:
        usuario_app = Usuarios.Usuario(usuario_db.id, usuario_db.nombre_usuario, usuario_db.contrasena, usuario_db.rol, usuario_db.rut_usuario)
        if usuario_app.rol == 'Administrador':
            messagebox.showinfo("Éxito", "Bienvenido, administrador")
            ventana_login.destroy()  # Cerramos la ventana de login
            # se abre la ventana de administrador
            import MainAdmin
            # ... (Código para configurar la ventana de administrador)

        elif usuario_app.rol == 'Trabajador':
            rut_trabajador = usuario_db.rut_usuario
            trabajador = BD.obtener_trabajador_por_rut(rut_trabajador)
            if trabajador:
                messagebox.showinfo("Éxito", f"Bienvenido, {usuario_app.nombre_usuario}")
                ventana_login.destroy()
                import MainTrabajador
                MainTrabajador.ventana_registro_trabajador(rut_trabajador)
            else: 
                messagebox.showinfo("Acceso negado", "Todavia no estas asignado, contacta con RR.HH e intente mas tarde")
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
entry_usuario.insert(0, "admin") ###
entry_usuario.pack()

label_contrasena = ttk.Label(ventana_login, text="Contraseña:")
label_contrasena.pack()
entry_contrasena = ttk.Entry(ventana_login, show="*")
entry_contrasena.insert(0, "123") ###
entry_contrasena.pack()

#botones para iniciar sesion o para ir a registrarce

boton_login = ttk.Button(ventana_login, text="Iniciar Sesión", command=login)
boton_login.pack()

boton_registro = ttk.Button(ventana_login, text="¿No tienes una cuenta? Registrarte", command=lambda: [ventana_login.destroy(), Registrar.ventana_registro.mainloop()])
boton_registro.pack()

ventana_login.mainloop()

