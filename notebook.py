#importacion de librerias
import tkinter as tk
from tkinter import ttk,messagebox

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


#Pestañas doctores
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores,text="Doctores")
pestañas.pack(expand=True, fill="both")


ventana_principal.mainloop()