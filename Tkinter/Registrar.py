import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Clases.Usuarios as Usuarios
import SQL.BD as BD
import Login
import bcrypt

def registrar():
    nombre_usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    rol = variable.get()  # Obtener el valor seleccionado del combobox

    # Validar datos (ej: longitud mínima, caracteres permitidos)
    if not nombre_usuario or not contrasena:
        messagebox.showerror("Error", "Por favor, ingresa un nombre de usuario y una contraseña.")
        return

    # Hashear la contraseña
    hashed_password = Usuarios.Usuario.hash_password(contrasena)

    # Insertar el usuario en la base de datos
    try:
        if BD.registrar_usuario(nombre_usuario, hashed_password, rol):
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
            # ... (limpiar campos)
            entry_usuario.delete(0, tk.END)
            entry_contrasena.delete(0, tk.END)
            variable.set("")
        else:
            messagebox.showerror("Error", "Error al registrar al usuario. Por favor, intenta nuevamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {str(e)}")

# ... (resto del código de la ventana, labels, etc.)

ventana_registro = tk.Tk()
ventana_registro.title("Registrarse")
ventana_registro.geometry("300x200")

# Crear un combobox para seleccionar el rol
label_usuario = ttk.Label(ventana_registro, text="Usuario:")
label_usuario.pack()
entry_usuario = ttk.Entry(ventana_registro)
entry_usuario.pack()

label_contrasena = ttk.Label(ventana_registro, text="Contraseña:")
label_contrasena.pack()
entry_contrasena = ttk.Entry(ventana_registro, show="*")
entry_contrasena.pack()

roles = ["Administrador", "RR.HH.", "Trabajador"]
variable = tk.StringVar()
variable.set(roles[0])  # Valor por defecto

label_rol = ttk.Label(ventana_registro, text="Rol:")
label_rol.pack()
combobox_rol = ttk.Combobox(ventana_registro, textvariable=variable, values=roles)
combobox_rol.pack()

# Botón de registro
boton_registrar = ttk.Button(ventana_registro, text="Registrar", command=registrar)
boton_registrar.pack()

boton_login = ttk.Button(ventana_registro, text="¿Ya tienes una cuenta? Ingresa aqui", command=lambda: [ventana_registro.destroy(), Login.ventana_login.mainloop()])
boton_login.pack()

ventana_registro.mainloop()