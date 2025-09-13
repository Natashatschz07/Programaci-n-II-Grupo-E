#importacion de librerias
import tkinter as tk
from tkinter import ttk,messagebox

def mostrarEdad():
    tk.messagebox.showinfo("Edad",f"La edad seleccionada es:{spin.get()}")

#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("500x600")

#Crear contenedor Notebook(pestañas)
pestañas=ttk.Notebook(ventana_principal)

#Crear frames(uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
#Agregar pestañas al Notebook
pestañas.add(frame_pacientes,text="Pacientes")
#Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")

#Nombre
labelNombre=tk.Label(frame_pacientes,text="Nombre Completo:")
labelNombre.grid(row=0,column=0,padx=5,pady=5,sticky="w")
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,padx=5,pady=5,sticky="w")

#Fecha de Nacimiento
labelFechaN=tk.Label(frame_pacientes,text="Fecha de Nacimiento:")
labelFechaN.grid(row=1,column=0,padx=5,pady=5,sticky="w")
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1,column=1,sticky="w",padx=5,pady=5)

#Edad
labelEdad=tk.Label(frame_pacientes,text="Edad:")
labelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadP=tk.Entry(frame_pacientes,state="readonly")
edadP.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#Genero
labelGenero=tk.Label(frame_pacientes,text="Género:")
labelGenero.grid(row=3,column=0,sticky="w",padx=5,pady=5)

genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,sticky="w",padx=5)

radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,sticky="w",padx=5)

#Grupo Sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5,column=0,sticky="w",padx=5,pady=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5,column=1,sticky="w",padx=5,pady=5)

#Tipo de seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de seguro:")
labelTipoSeguro.grid(row=6,column=0,sticky="w",padx=5,pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público")
comboTipoSeguro=ttk.Combobox(frame_pacientes,values=["Público","Privado","Ninguno"],textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6,column=1,sticky="w",padx=5,pady=5)

#Centro médico
labelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud:")
labelCentroMedico.grid(row=7,column=0,sticky="w",padx=5,pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")#Valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital Central","Clínica Norte","Centro Sur"],textvariable=centro_medico)
comboCentroMedico.grid(row=7,column=1,sticky="w",padx=5,pady=5)

#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=10,column=0, columnspan=2, pady=5,sticky="w")

#Boton Registrar
btn_registrar=tk.Button(btn_frame,text="Registrar", command="",bg="LimeGreen")
btn_registrar.grid(row=0,column=0, padx=5)

#Botn Eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="",bg="Tomato")
btn_eliminar.grid(row=0,column=1, padx=5)

#Crear treeView para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM"),show="headings")

#Definir encabezados
treeview.heading("Nombre",text="Nombre Completo")
treeview.heading("FechaN",text="Fecha de Nacimiento")
treeview.heading("Edad",text="Edad")
treeview.heading("Genero",text="Género")
treeview.heading("GrupoS",text="Grupo Sanguíneo")
treeview.heading("TipoS",text="Tipo Seguro")
treeview.heading("CentroM",text="Centro Médico")

#Definir anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)

#Ubicar el TreeView en la cuadrícula
treeview.grid(row=9,column=0, columnspan=2, padx=5,pady=10, sticky="nsew")

#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=9,column=2, sticky="ns")


#Pestañas doctores
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores,text="Doctores")
pestañas.pack(expand=True, fill="both")

labelRegistro = tk.Label(frame_doctores, text="Registro de Doctores", font=("Arial", 14, "bold"))
labelRegistro.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

#Nombre
labelNombr=tk.Label(frame_doctores,text="Nombre :")
labelNombr.grid(row=1,column=0,padx=5,pady=5,sticky="w")
nombrD=tk.Entry(frame_doctores)
nombrD.grid(row=1,column=1,padx=5,pady=5,sticky="w")

#Especialidad
labelEspecialidad=tk.Label(frame_doctores,text="Especialidad:")
labelEspecialidad.grid(row=2,column=0,sticky="w",padx=5,pady=5)
especialidad=tk.StringVar()
especialidad.set("Cardiología")#Valor por defecto
comboEspecialidad=ttk.Combobox(frame_doctores,values=["Cardiología","Pediatría","Neurología","Traumatología"],textvariable=especialidad)
comboEspecialidad.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#Edad
labelEdadD=tk.Label(frame_doctores,text="Edad")
labelEdadD.grid(row=3,column=0,padx=5,pady=5,sticky="w")
spin=tk.Spinbox(frame_doctores,from_=1,to=100)
spin.grid(row=3,column=1,padx=5,pady=5,sticky="w")

#Teléfono
labelTelef=tk.Label(frame_doctores,text="Teléfono:")
labelTelef.grid(row=4,column=0,padx=5,pady=5,sticky="w")
telefD=tk.Entry(frame_doctores)
telefD.grid(row=4,column=1,padx=5,pady=5,sticky="w")


#Frame para los botones
btn_frameD=tk.Frame(frame_doctores)
btn_frameD.grid(row=9,column=0, columnspan=2, pady=5,sticky="w")

#Boton Registrar
btn_registrarD=tk.Button(btn_frameD,text="Registrar", command="",bg="LimeGreen")
btn_registrarD.grid(row=0,column=0, padx=5)

#Botn Eliminar
btn_eliminarD=tk.Button(btn_frameD, text="Eliminar", command="",bg="Tomato")
btn_eliminarD.grid(row=0,column=1, padx=5)

#Crear treeView para mostrar pacientes
treeviewD=ttk.Treeview(frame_doctores,columns=("Nombre","Especialidad","Edad","Telefono"),show="headings")

#Definir encabezados
treeviewD.heading("Nombre",text="Nombre")
treeviewD.heading("Especialidad",text="Especialidad")
treeviewD.heading("Edad",text="Edad")
treeviewD.heading("Telefono",text="Teléfono")


#Definir anchos de columnas
treeviewD.column("Nombre", width=120)
treeviewD.column("Especialidad", width=120)
treeviewD.column("Edad", width=100, anchor="center")
treeviewD.column("Telefono", width=100, anchor="center")


#Ubicar el TreeView en la cuadrícula
treeviewD.grid(row=10,column=0, columnspan=2, padx=5,pady=10, sticky="nsew")

#Scrollbar vertical
scroll_yD=ttk.Scrollbar(frame_doctores,orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scroll_yD.set)
scroll_yD.grid(row=10,column=2, sticky="ns")



ventana_principal.mainloop()