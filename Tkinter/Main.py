import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Clases.Usuarios as Usuarios
import SQL.BD as BD

def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Sistema de Gestión")

    notebook = ttk.Notebook(ventana)
    notebook.pack(fill="both", expand=True)

    # Pestaña de Registro
    tab_registro = ttk.Frame(notebook)
    # ... (elementos de la pestaña de registro, como labels, entry, botones)

    label_usuario_registro = ttk.Label(tab_registro, text="Usuario:")
    label_usuario_registro.grid()
    entry_usuario_registro = ttk.Entry(tab_registro)
    entry_usuario_registro.grid()

    label_contrasena_registro = ttk.Label(tab_registro, text="Contraseña:")
    label_contrasena_registro.grid()
    entry_contrasena_registro = ttk.Entry(tab_registro, show="*")
    entry_contrasena_registro.grid()

    roles = ["Administrador", "RR.HH.", "Trabajador"]
    variable = tk.StringVar()
    variable.set(roles[0])  # Valor por defecto

    label_rol = ttk.Label(tab_registro, text="Rol:")
    label_rol.grid()
    combobox_rol = ttk.Combobox(tab_registro, textvariable=variable, values=roles)
    combobox_rol.grid()

    label_rut_registro = ttk.Label(tab_registro, text="Rut:")
    label_rut_registro.grid()
    entry_rut_registro = ttk.Entry(tab_registro)
    entry_rut_registro.grid()

# Botón de registro
    boton_registrar = ttk.Button(tab_registro, text="Registrar", command=registrar)
    boton_registrar.grid()

    # Pestaña de Login
    tab_login = ttk.Frame(notebook)
    # ... (elementos de la pestaña de login)

    # Mostrar la pestaña de Login por defecto
    notebook.add(tab_registro, text="Registrarse")
    notebook.add(tab_login, text="Iniciar Sesión")
    notebook.select(tab_login)  # Mostrar la pestaña de login al inicio

    # Funciones para mostrar/ocultar pestañas
    def mostrar_pestaña_registro():
        notebook.select(tab_registro)

    def mostrar_pestaña_login():
        notebook.select(tab_login)

    # Botón para cambiar de pestaña en la pestaña de registro
    boton_login_desde_registro = ttk.Button(tab_registro, text="¿Ya tienes una cuenta? Inicia sesión", command=mostrar_pestaña_login)
    boton_login_desde_registro.pack()

    # Botón para cambiar de pestaña en la pestaña de login
    boton_registro_desde_login = ttk.Button(tab_login, text="¿No tienes una cuenta? Regístrate", command=mostrar_pestaña_registro)
    boton_registro_desde_login.pack()

    # ... (resto del código para las funciones de registro y login)

    def registrar():
        nombre_usuario = entry_usuario_registro.get()
        contrasena = entry_contrasena_registro.get()
        rol = variable.get()
        rut_usuario = entry_rut_registro.get()

        # Validar datos (ej: longitud mínima, caracteres permitidos)
        if not nombre_usuario or not contrasena or not rol or not rut_usuario:
            messagebox.showerror("Error", "Por favor, complete sus datos.")
            return

        # Hashear la contraseña
        hashed_password = Usuarios.Usuario.hash_password(contrasena)

        # Insertar el usuario en la base de datos
        try:
            if BD.registrar_usuario(nombre_usuario, hashed_password, rol, rut_usuario):
                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
                # ... (limpiar campos)
                entry_usuario_registro.delete(0, tk.END)
                entry_contrasena_registro.delete(0, tk.END)
                variable.set("")
            else:
                messagebox.showerror("Error", "Error al registrar al usuario. Por favor, intenta nuevamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {str(e)}")

    ventana.mainloop()

if __name__ == "__main__":
    ventana_principal()