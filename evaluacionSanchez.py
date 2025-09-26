#importación de librerías necesarias
import tkinter as tk 
from tkinter import ttk, messagebox
from datetime import datetime

#función para enmascarar fecha
def enmascarar_fecha(texto): #texto=recibe la fecha
    limpio=''.join(filter(str.isdigit,texto))
    formato_final=""
 # Si hay más de 8 dígitos, recorta a los primeros 8    
    if len(limpio)>8:
        limpio=limpio[:8]
 # Si hay más de 4 dígitos, formatea como "dd-mm-yyyy"
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"#ordena los digitos de 2 en 2, luego l resto queda separado por guión
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio # Si son menos de 2 dígitos, solo se devuelve lo que hay
    
    # Si el valor en la caja de texto es diferente del formato calculado, lo actualiza
    if fechaN.get() !=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0,formato_final)
    # Si la fecha tiene el formato completo "dd-mm-yyyy", calcula la edad
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_nacimiento.year 
        edadVar.set(edad)
    else:
        edadVar.set("")# Si no se tiene la fecha completa, borra la edad
    return True

# Función para guardar la lista de pacientes en un archivo de texto
def guardar_en_archivo():
    with open("pacientePeso.txt","w",encoding="utf-8") as archivo:   #utf_8 permite aceptar caracteres especiales y la letra ñ / with para cerrar correctamemte el archivo
        for paciente in paciente_data:                          # Recorre la lista de pacientes
            archivo.write(
            f"{paciente['Nombre']}|"            
            f"{paciente['Fecha de Nacimiento']}|"
            f"{paciente['Edad']}|"
            f"{paciente['Género']}|"
            f"{paciente['Grupo Sanguíneo']}|{paciente['Tipo de Seguro']}|"
            f"{paciente['Tipo de Seguro']}|{paciente['Peso']}\n")
            
# Función para cargar los pacientes desde el archivo           
def cargar_desde_archivo_pacientes():
    try:
        with open("pacientePeso.txt","r",encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==8:
                    paciente={
                        "Nombre":datos[0],
                        "Fecha de Nacimiento":datos[1],
                        "Edad":datos[2],
                        "Género":datos[3],
                        "Grupo Sanguíneo":datos[4],
                        "Tipo de Seguro":datos[5],
                        "Centro Médico":datos[6],
                        "Peso":datos[7],
                        
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("pacientePeso.txt","w",encoding="utf-8").close()
        
def eliminarPaciente():
    seleccionado=treeview.selection()# Obtiene el paciente seleccionado en el TreeView
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        # Pregunta de confirmación para eliminar el paciente
        if messagebox.askyesno("Eliminar Paciente",f"¿Está seguro de eliminar el paciente'{treeview.item(id_item,'values')[0]}'?"):
            del paciente_data[indice]# Elimina el paciente de la lista
            guardar_en_archivo()  #Guardar los cambios en el archivo
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente","Paciente eliminado exitosamente")
    else:   #Este else es de if seleccionado
        messagebox.showwarning("Eliminar Paciente","No se ha seleccionado ningún paciente")
        return

#Lista de pacientes(inicialmente vacía)
paciente_data=[]

#Función para registrar paciente
def registrarPaciente():
    #Craer un diccionario con los datos ingresados
    paciente={
        "Nombre":nombreP.get(),
        "Fecha de Nacimiento":fechaN.get(),
        "Edad":edadVar.get(),
        "Género":genero.get(),
        "Grupo Sanguíneo":grupoSanguineo.get(),
        "Tipo de Seguro":tipo_seguro.get(),
        "Centro Médico":centro_medico.get(),
        "Peso":peso.get()
    }
    #Agregar paciente a la lista
    paciente_data.append(paciente)# Agregar paciente a la lista
    guardar_en_archivo()# Guardar en el archivo
   
    cargar_treeview()# Recargar el TreeView
# Función para cargar los pacientes en el Treeview
def cargar_treeview():
    #Limpiar el Treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #Insertar cada paciente
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Género"],
                item["Grupo Sanguíneo"],
                item["Tipo de Seguro"],
                item["Centro Médico"],
                item["Peso"]
            )
        )
    

#Crear una ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores") #Titulo de la ventana
ventana_principal.geometry("850x700")#Tamañao de la ventana

#Crear contenedor Notebook(pestañas)
pestañas=ttk.Notebook(ventana_principal)
#Crear frames(uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
#Agregar pestañas al Notebook(para organizar el contenido)
pestañas.add(frame_pacientes,text="Pacientes")

#Mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both") #fill=relleno, both para que se muestre en todo el espacio
# Resto de las entradas para la información del paciente
#Nombre
labelNombre=tk.Label(frame_pacientes,text="Nombre Completo: ")
labelNombre.grid(row=0,column=0,sticky="w",padx=5,pady=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,sticky="w",padx=5,pady=5)

#Fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes,text="Fecha de Nacimiento: ")
labelFechaN.grid(row=1,column=0,sticky="w",padx=5,pady=5)

validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes,validate="key",validatecommand=(validacion_fecha,'%P'))
fechaN.grid(row=1,column=1,sticky="w",padx=5,pady=5)

#Edad(readonly)
labelEdad=tk.Label(frame_pacientes,text="Edad: ")
labelEdad.grid(row=2,column=0,sticky="w",padx=5,pady=5)
edadVar=tk.StringVar()
edadP=tk.Entry(frame_pacientes,textvariable=edadVar,state="readonly") 
edadP.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#Género
labelGenero=tk.Label(frame_pacientes,text="Género: ")
labelGenero.grid(row=3,column=0,sticky="w",padx=5,pady=5)
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,sticky="w",padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,sticky="w",padx=5)

#Grupo Sanguíneo
labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo Sanguíneo: ")
labelGrupoSanguineo.grid(row=5,column=0,sticky="w",padx=5,pady=5)
grupoSanguineo=tk.Entry(frame_pacientes,text="Grupo Sanguíneo")
grupoSanguineo.grid(row=5,column=1,padx=5,pady=5,sticky="w")


#Tipo de Seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de seguro: ")
labelTipoSeguro.grid(row=6,column=0,sticky="w",padx=5,pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público")#Valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes,values=["Público","Privado","Ninguno"],textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6,column=1,sticky="w",padx=5,pady=5)

#Centro Médico
labelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud: ")
labelCentroMedico.grid(row=7,column=0,sticky="w",padx=5,pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #Valos por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital Central","Clínica Norte","Centro Sur"],textvariable=centro_medico)
comboCentroMedico.grid(row=7,column=1,sticky="w",padx=5,pady=5)

#Peso
labelPeso=tk.Label(frame_pacientes,text="Peso: ")
labelPeso.grid(row=8,column=0,sticky="w",padx=5,pady=5)
peso=tk.Entry(frame_pacientes,text="Peso")
peso.grid(row=8,column=1,padx=5,pady=5,sticky="w")

#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=9,column=0,columnspan=2,pady=5,sticky="w")

#Botón Registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command=registrarPaciente)
btn_registrar.grid(row=0,column=0,padx=5)
btn_registrar.configure(bg="LimeGreen")

#Botoón eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar",command=eliminarPaciente)
btn_eliminar.grid(row=0,column=1,padx=5)
btn_eliminar.configure(bg="Tomato")

#Crear TreeView para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM","Peso"),show="headings")

#Definir encabezados
treeview.heading("Nombre",text="Nombre Completo")
treeview.heading("FechaN",text="Fecha Nacimiento")
treeview.heading("Edad",text="Edad")
treeview.heading("Genero",text="Género")
treeview.heading("GrupoS",text="Grupo Sanguíneo")
treeview.heading("TipoS",text="Tipo de Seguro")
treeview.heading("CentroM",text="Centro Médico")
treeview.heading("Peso",text="Peso")

#Definir ancho de columnas
treeview.column("Nombre",width=130)
treeview.column("FechaN",width=120)
treeview.column("Edad",width=50,anchor="center")
treeview.column("Genero",width=70,anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120)
treeview.column("Peso",width=100,anchor="center")

#Indicar el TreeView en la cuadrícula
treeview.grid(row=10,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

#Scrolibar vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=10,column=2,sticky="w")


cargar_desde_archivo_pacientes()   #Cargar datos desde el archivo al iniciar la aplicacion


ventana_principal.mainloop()