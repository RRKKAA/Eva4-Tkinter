import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import SQL.BD as BD

def ventana_registro_trabajador(rut_trabajador):
    # Crear la ventana y los elementos del formulario (similar a ventana_registro)
    ventana_trabajador = tk.Tk()
    ventana_trabajador.title("Datos del Trabajador")

    rut_trabajador = rut_trabajador

    trabajador = BD.obtener_trabajador_por_rut(rut_trabajador)
    contactos = BD.obtener_contactos_por_rut(rut_trabajador)
    familiares = BD.obtener_familiares_por_rut(rut_trabajador)

    notebook = ttk.Notebook(ventana_trabajador)
    notebook.pack(fill="both", expand=True)

    tab_contactos = ttk.Frame(notebook)
    tabla_contactos = ttk.Treeview(tab_contactos, columns=("Nombre", "Telefono", "Relación"))
    #tabla_contactos.heading("Nombre", text="Nombre")
    #tabla_contactos.heading("Teléfono", text="Teléfono")
    #tabla_contactos.heading("Relación", text="Relación")
    # ... (configurar tabla de contactos)
    tabla_contactos.pack(fill="both", expand=True)

    # Poblar la tabla
    for contacto in contactos:
        tabla_contactos.insert("", "end", values=(contacto.nombre_contacto, contacto.telefono_contacto, contacto.relacion))
    # ... (botones para agregar, editar, eliminar contactos)
    notebook.add(tab_contactos, text="Contactos")

    tab_familiares = ttk.Frame(notebook)
    tabla_familiares = ttk.Treeview(tab_contactos, columns= ("Nombre", "Parentesco", "Sexo", "Rut"))
    tabla_familiares.pack(fill="both", expand=True)

    for familiar in familiares:
        tabla_familiares.insert("", "end", values=(familiar.nombre_familiar, familiar.parentesco, familiar.sexo_familiar, familiar.rut_familiar))
    # ... (botones para agregar, editar, eliminar contactos)
    notebook.add(tab_familiares, text="Familiares")


    datos_trabajador = vars(trabajador)
        # Crear un frame para organizar los elementos
    frame_datos = ttk.Frame(ventana_trabajador)
    frame_datos.pack(padx=20, pady=20)

    # Crear etiquetas y mostrar los datos en un layout de grid
    row = 0
    for campo, valor in datos_trabajador.items():
        label = ttk.Label(frame_datos, text=f"{campo.capitalize()}: {valor}", font=("Helvetica", 12))
        label.grid(row=row, column=0, sticky="w")
        row += 1

        # Crear un botón para cerrar la ventana
    btn_cerrar = ttk.Button(ventana_trabajador, text="Cerrar", command=ventana_trabajador.destroy)
    btn_cerrar.pack(pady=10)
    
    menu_bar = tk.Menu(ventana_trabajador)
    ventana_trabajador.config(menu=menu_bar)

    # Menú "Opciones"
    menu_opciones = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Opciones", menu=menu_opciones)

    # Opción "Modificar datos personales"
    menu_opciones.add_command(label="Modificar datos personales", command=lambda: modificar_datos_personales(trabajador))
    menu_opciones.add_command(label="Crear nuevo contacto", command=lambda: crear_contactos(rut_trabajador))
    menu_opciones.add_command(label="Crear nuevo familiar", command=lambda: crear_familiares(rut_trabajador))

    # Opción "Ver contactos"
    #menu_opciones.add_command(label="Ver contactos", command=lambda: crear_contactos)

    # Opción "Ver familiares"
    #menu_opciones.add_command(label="Ver familiares", command=ver_familiares)

    ventana_trabajador.mainloop()

def modificar_datos_personales(trabajador):
    ventana_modificar = tk.Toplevel()
    ventana_modificar.title("Editar datos personales")

    opciones_sexo = ["Hombre", "Mujer", "Otro"]
    
    label_nombre = ttk.Label(ventana_modificar, text="Nombre:")
    label_nombre.pack()
    entry_nombre = ttk.Entry(ventana_modificar)
    entry_nombre.insert(0, trabajador.nombre)
    entry_nombre.pack()

    label_apellido = ttk.Label(ventana_modificar, text="Apellido:")
    label_apellido.pack()
    entry_apellido = ttk.Entry(ventana_modificar)
    entry_apellido.insert(0, trabajador.apellido)
    entry_apellido.pack()

    label_sexo = ttk.Label(ventana_modificar, text="Sexo:")
    label_sexo.pack()
    combobox_sexo = ttk.Combobox(ventana_modificar, values=opciones_sexo)
    combobox_sexo.insert(0, trabajador.sexo)
    combobox_sexo.pack()

    label_direccion = ttk.Label(ventana_modificar, text="Direccion:")
    label_direccion.pack()
    entry_direccion = ttk.Entry(ventana_modificar)
    entry_direccion.insert(0, trabajador.direccion)
    entry_direccion.pack()

    label_telefono = ttk.Label(ventana_modificar, text="Telefono:")
    label_telefono.pack()
    entry_telefono = ttk.Entry(ventana_modificar)
    entry_telefono.insert(0, trabajador.telefono)
    entry_telefono.pack()

    def actualizar_trabajador():
        rut = trabajador.rut
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        sexo = combobox_sexo.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        cargo = trabajador.cargo
        area = trabajador.area
        departamento = trabajador.departamento

        BD.actualizar_trabajador(rut, nombre, apellido, sexo, direccion, telefono, cargo, area, departamento)

        ventana_modificar.destroy()
        
        messagebox.showinfo("Éxito", "Trabajador registrado correctamente.")

    boton_guardar = ttk.Button(ventana_modificar, text="Guardar", command=actualizar_trabajador)
    boton_guardar.pack()

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
    

#def ver_familiares():
    # Crear una nueva ventana para mostrar los familiares
    # ... (implementar la lógica para mostrar, agregar, modificar y eliminar familiares)