import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Crear ventana principal
ventana=tk.Tk()
ventana.title("Ejemplo Combobox")
ventana.geometry("300x200")

#Etiqueta
etiqueta=tk.Label(ventana,text="Seleccione especialidad:")
etiqueta.grid(row=0,column=0,padx=10,pady=10,sticky="w")

#Crear Combobox
opciones=["Cardiología","Neurología","Pediatría","Dermatología","Oncología"]
combo=ttk.Combobox(ventana,values=opciones,state="readonly")
combo.current(0)   #Seleccionar primera opcion por defecto
combo.grid(row=0,column=1,padx=10,pady=10)

#Funcion para mostrar la seelecion
def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("Seleccion",f"Has elegido:{seleccion}")
    
#Boton para confirmar seleccion
boton=tk.Button(ventana,text="Aceptar",command=mostrar)
boton.grid(row=1,column=0,columnspan=2,pady=15)

ventana.mainloop()
