import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from SQL import BD
from Clases import Trabajadores

# Crear la ventana principal
ventana_admin = tk.Tk()
ventana_admin.title("El Correo de Yury")

# Crear una tabla para mostrar los trabajadores
tabla_trabajadores = ttk.Treeview(ventana_admin, columns=("rut", "nombre", "sexo", "cargo"))
tabla_trabajadores.heading("rut", text="RUT")
tabla_trabajadores.heading("nombre", text="Nombre")
tabla_trabajadores.heading("sexo", text="Sexo")
tabla_trabajadores.heading("cargo", text="Cargo")
tabla_trabajadores.pack()

def listar_trabajadores_admin():
    datos_trabajadores = BD.obtener_trabajadores()

    print(datos_trabajadores)

    tabla_trabajadores.delete(*tabla_trabajadores.get_children())
    for trabajador in datos_trabajadores:
        tabla_trabajadores.insert('', 'end', values=(trabajador.rut, trabajador.nombre, trabajador.sexo, trabajador.cargo))


def registrar_nuevo_trabajador():
    # Crear una ventana modal
    ventana_registro1 = tk.Toplevel()
    ventana_registro1.title("Registrar Nuevo Trabajador")

    rut_disponibles = BD.obtener_ruts_disponibles()
    opciones_sexo = ["Hombre", "Mujer", "Otro"]
    opciones_cargos = ["Consultor", "Desarrollador", "Diseñador", "Gerente"]
    opciones_areas = ["Ventas", "Marketing", "Desarrollo", "Administración"]
    opciones_departamentos = ["Tecnología", "Comercial", "Recursos Humanos"]

    # Crear los campos del formulario
    label_rut = ttk.Label(ventana_registro1, text="Rut:")
    label_rut.pack()
    combobox_rut = ttk.Combobox(ventana_registro1, values=rut_disponibles)
    combobox_rut.pack()

    label_nombre = ttk.Label(ventana_registro1, text="Nombre:")
    label_nombre.pack()
    entry_nombre = ttk.Entry(ventana_registro1)
    entry_nombre.pack()

    label_apellido = ttk.Label(ventana_registro1, text="Apellido:")
    label_apellido.pack()
    entry_apellido = ttk.Entry(ventana_registro1)
    entry_apellido.pack()

    label_sexo = ttk.Label(ventana_registro1, text="Sexo:")
    label_sexo.pack()
    combobox_sexo = ttk.Combobox(ventana_registro1, values=opciones_sexo)
    combobox_sexo.pack()

    label_direccion = ttk.Label(ventana_registro1, text="Direccion:")
    label_direccion.pack()
    entry_direccion = ttk.Entry(ventana_registro1)
    entry_direccion.pack()

    label_telefono = ttk.Label(ventana_registro1, text="Telefono:")
    label_telefono.pack()
    entry_telefono = ttk.Entry(ventana_registro1)
    entry_telefono.pack()

    label_cargo = ttk.Label(ventana_registro1, text="Cargo:")
    label_cargo.pack()
    combobox_cargo = ttk.Combobox(ventana_registro1, values=opciones_cargos)
    combobox_cargo.pack()

    label_area = ttk.Label(ventana_registro1, text="Area:")
    label_area.pack()
    combobox_area = ttk.Combobox(ventana_registro1, values=opciones_areas)
    combobox_area.pack()

    label_departamento = ttk.Label(ventana_registro1, text="Departamento:")
    label_departamento.pack()
    combobox_departamento = ttk.Combobox(ventana_registro1, values=opciones_departamentos)
    combobox_departamento.pack()
    

    # Función para guardar los datos
    def guardar_trabajador():
        rut = combobox_rut.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        sexo = combobox_sexo.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        cargo = combobox_cargo.get()
        area = combobox_area.get()
        departamento = combobox_departamento.get()
        
        # Insertar los datos en la base de datos
        BD.insertar_trabajador(rut, nombre, apellido, sexo, direccion, telefono, cargo, area, departamento)  # Ajusta según tu función
        
        # Cerrar la ventana modal
        ventana_registro1.destroy()
        
        # Mostrar un mensaje de confirmación
        messagebox.showinfo("Éxito", "Trabajador registrado correctamente.")

    # Botón para guardar
    boton_guardar = ttk.Button(ventana_registro1, text="Guardar", command=guardar_trabajador)
    boton_guardar.pack()


# Menú de navegación
menubar = tk.Menu(ventana_admin)

# Menú Trabajadores
menu_trabajadores = tk.Menu(menubar, tearoff=0)
menu_trabajadores.add_command(label="Listar trabajadores", command=listar_trabajadores_admin)
# ... (otros comandos para agregar, editar, eliminar, buscar)
menubar.add_cascade(label="Trabajadores", menu=menu_trabajadores)


menu_acciones = tk.Menu(menu_trabajadores, tearoff=0)
menu_acciones.add_command(label="Registrar nuevo", command=registrar_nuevo_trabajador)
#menu_acciones.add_command(label="Modificar", command=modificar_trabajador)
menu_trabajadores.add_cascade(label="Acciones", menu=menu_acciones)

menu_trabajadores.add_command(label="Listar todos", command=listar_trabajadores_admin)
#menu_trabajadores.add_command(label="Filtrar", command=listar_trabajadores_filtrados)

# ... (crear menús para Contactos, Cargas Familiares, Reportes y Usuarios)

ventana_admin.config(menu=menubar)

# Mostrar la ventana
ventana_admin.mainloop()

def crear_contactos(rut_1):
    ventana_contactocrear = tk.Toplevel()
    ventana_contactocrear.title("Crear Nuevo Contacto")

    opciones_relacion = ["Amigo", "Familiar", "Vecino", "Compañero", "Otro"]
    rut_1 = rut_1

    # Crear los campos del formulario
    label_nombre_contacto = ttk.Label(ventana_contactocrear, text="Nombre:")
    label_nombre_contacto.pack()
    entry_nombre_contacto = ttk.Entry(ventana_contactocrear)
    entry_nombre_contacto.pack()

    label_relacion = ttk.Label(ventana_contactocrear, text="Relacion:")
    label_relacion.pack()
    combobox_relacion = ttk.Combobox(ventana_contactocrear, values=opciones_relacion)
    combobox_relacion.pack()

    label_telefono_contacto = ttk.Label(ventana_contactocrear, text="Telefono:")
    label_telefono_contacto.pack()
    entry_telefono_contacto = ttk.Entry(ventana_contactocrear)
    entry_telefono_contacto.pack()

    boton_guardar_contacto = ttk.Button(ventana_contactocrear, text="Guardar", command=lambda: crear_contacto(rut_1))
    boton_guardar_contacto.pack()

    def crear_contacto(rut_1):
        nombre = entry_nombre_contacto.get()
        relacion = combobox_relacion.get()
        telefono = entry_telefono_contacto.get()
        rut_1 = rut_1
        
        # Insertar los datos en la base de datos
        BD.registrar_contacto(nombre, relacion, telefono, rut_1)  # Ajusta según tu función
        
        # Cerrar la ventana modal
        ventana_contactocrear.destroy()
        
        # Mostrar un mensaje de confirmación
        messagebox.showinfo("Éxito", "Contacto registrado correctamente.")

def crear_familiares(rut_1):
    ventana_familiarcrear = tk.Toplevel()
    ventana_familiarcrear.title("Crear Nuevo Familiar")

    opciones_parentesco = ["Padre/Madre", "Abuelo/Abuela", "Hermano/Hermana", "Hijo/Hija", "Tio/Tia", "Suegro/Suegra", "Otro"]
    rut_1 = rut_1

    # Crear los campos del formulario
    label_nombre_familiar = ttk.Label(ventana_familiarcrear, text="Nombre:")
    label_nombre_familiar.pack()
    entry_nombre_contacto = ttk.Entry(ventana_familiarcrear)
    entry_nombre_contacto.pack()

    label_parentesco = ttk.Label(ventana_familiarcrear, text="Parentesco:")
    label_parentesco.pack()
    combobox_parentesco = ttk.Combobox(ventana_familiarcrear, values=opciones_parentesco)
    combobox_parentesco.pack()

    label_sexo_familiar = ttk.Label(ventana_familiarcrear, text="Sexo:")
    label_sexo_familiar.pack()
    combobox_sexo_familiar = ttk.Combobox(ventana_familiarcrear, values=opciones_parentesco)
    combobox_sexo_familiar.pack()

    label_rut_familiar = ttk.Label(ventana_familiarcrear, text="RUT:")
    label_rut_familiar.pack()
    entry_rut_familiar = ttk.Entry(ventana_familiarcrear)
    entry_rut_familiar.pack()

    boton_guardar_familiar = ttk.Button(ventana_familiarcrear, text="Guardar", command=lambda: crear_familiar(rut_1))
    boton_guardar_familiar.pack()

    def crear_familiar(rut_1):
        nombre = entry_nombre_contacto.get()
        parentesco = combobox_parentesco.get()
        sexo = combobox_sexo_familiar.get()
        rut = entry_rut_familiar.get()
        rut_2 = rut_1
        
        # Insertar los datos en la base de datos
        BD.registrar_familiar(nombre, parentesco, sexo, rut, rut_2)  # Ajusta según tu función
        
        # Cerrar la ventana modal
        ventana_familiarcrear.destroy()
        
        # Mostrar un mensaje de confirmación
        messagebox.showinfo("Éxito", "Familiar registrado correctamente.")