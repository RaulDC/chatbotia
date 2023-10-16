from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connection import *

# Configuración de la ventana principal
root = Tk()
root.title("CRUD")
root.geometry("800x670")
root.resizable(0,0)
root.config(bd=10)

db=DataBase()

"--------------- Titulo --------------------"
titulo= Label(root, text="REGISTRO DE ESTUDIANTES",fg="black",font=("Comic Sans", 17,"bold"),pady=10).pack()

"--------------- Frame marco --------------------"
marco = LabelFrame(root, text="Insertar registro",font=("Comic Sans", 10,"bold"),borderwidth=2,relief="groove")
marco.config(bd=2)
marco.pack() # Agrega espacio alrededor del marco

"--------------- Formulario --------------------"
cod_label = Label(marco,text="Código del estudiante: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
cod_entry=Entry(marco,width=30)
cod_entry.focus_set()
cod_entry.grid(row=0, column=1, padx=5, pady=8)

nom_label = Label(marco,text="Nombres: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
nom_entry=Entry(marco,width=30)
nom_entry.grid(row=1, column=1, padx=10, pady=8)

ape_label = Label(marco,text="Apellidos: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=8)
ape_entry=Entry(marco,width=30)
ape_entry.grid(row=0, column=3, padx=10, pady=8)

con_label = Label(marco,text="Contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=2,sticky='s',padx=5,pady=8)
con_entry=Entry(marco,width=30)
con_entry.grid(row=1, column=3, padx=5, pady=8)

"--------------- Tabla --------------------"    
tree=ttk.Treeview(marco, height=20)
tree.grid(column=0, row=3, columnspan=4, padx=10)
tree["columns"]=("CODIGO",  "CONTRASEÑA", "NOMBRES", "APELLIDOS")

tree.column("#0", width=0, stretch=NO)
tree.column("CODIGO", width=70, minwidth=75, anchor=CENTER)
tree.column("CONTRASEÑA", width=170, minwidth=75, anchor=CENTER)
tree.column("NOMBRES", width=170, minwidth=75, anchor=CENTER)
tree.column("APELLIDOS", width=170, minwidth=75, anchor=CENTER)

tree.heading("#0",text="")
tree.heading("CODIGO",text="CODIGO", anchor=CENTER)
tree.heading("CONTRASEÑA",text="CONTRASEÑA", anchor=CENTER)
tree.heading("NOMBRES",text="NOMBRES", anchor=CENTER)
tree.heading("APELLIDOS",text="APELLIDOS", anchor=CENTER)

#txtMensaje=Label(marco, text="mensajes", fg="green").grid(column=0,row=2, columnspan=4)

"--------------- Botones --------------------"
delete_button=Button(marco,text="ELIMINAR",command=lambda:delete_record(),height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=4, column=1, padx=10, pady=15)

insert_button=Button(marco,text="INSERTAR",command=lambda:insert_record(),height=2,width=10,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=4, column=2, padx=10, pady=15)

update_button=Button(marco,text="ACTUALIZAR",command=lambda:update_record(),height=2,width=10,bg="gray",fg="white",font=("Comic Sans", 10,"bold")).grid(row=4, column=3, padx=10, pady=15)
               
"--------------- CRUD --------------------"   
# Función para seleccionar y mostrar todos los registros
def validar():
   return len(cod_entry.get()) and len(nom_entry.get()) and len(ape_entry.get()) and len(con_entry.get())
   
def limpiar():
   nom_entry.delete(0, END)
   ape_entry.delete(0, END)
   cod_entry.delete(0, END)
   con_entry.delete(0, END)

def vaciar_tabla():
   records = tree.get_children()
   for row in records:
      tree.delete(row)

def llenar_tabla():
   vaciar_tabla()
   sql="SELECT * FROM t_estudiantes"
   db.cursor.execute(sql)
   records = db.cursor.fetchall()
   for row in records:
      cod = row[0]
      tree.insert("", END, cod, text= cod, values=row)

def delete_record():
   try:
      cod= tree.selection()[0] 
      dato = tree.item(tree.selection())['values'][0]
   except IndexError as e:
      messagebox.showerror("ERROR","Porfavor selecciona un elemento") 
      return
   respuesta=messagebox.askquestion("ADVERTENCIA",f"¿Seguro que desea eliminar el registro: {dato}?")      

   if respuesta == 'yes':
      cursor = db.connection.cursor()
      sql="delete from t_estudiantes where cod_estudiante= %s"

      try:
         cursor.execute(sql, (cod,))
         db.connection.commit()
         tree.delete(cod)
         messagebox.showinfo('Éxito', f'Registro eliminado: {dato}')

      except Exception as e:
         messagebox.showerror('ERROR',f'Error al eliminar el registro: {dato} - {str(e)}')
   else:
         messagebox.showinfo('Operación cancelada', 'No se eliminó el registro.')


def insert_record():

   if validar():
      val=(cod_entry.get(), nom_entry.get(), ape_entry.get(), con_entry.get())
      sql="INSERT INTO t_estudiantes(cod_estudiante, nom_estudiante, ape_estudiante, con_estudiante) VALUES (%s, %s, %s, %s)"
      db.cursor.execute(sql, val)
      db.connection.commit()
      messagebox.showinfo("REGISTRO EXITOSO", f'Estudiante registrado:\n {nom_entry.get()} {ape_entry.get()}')
      llenar_tabla()
      limpiar()
   else:
      messagebox.showerror("Error", "¡Campos vacíos!")  


def update_record():
   try:
      tree_item = tree.item(tree.selection())
      cod = tree_item['text']
   except IndexError as e:
      messagebox.showerror("ERROR","Porfavor selecciona un elemento") 
      return
   new_con = con_entry.get()

   Ventana_editar = Toplevel()
   Ventana_editar.title('MODIFICAR CONTRASEÑA')
   Ventana_editar.resizable(0,0)

   label_password=Label(Ventana_editar,text="Nueva contraseña:",font=("Comic Sans", 10,"bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)

   new_password = Entry(Ventana_editar, textvariable=StringVar(Ventana_editar, value=new_con),width=25)
   new_password.grid(row=0, column=1, padx=5, pady=8)

   boton_actualizar = Button(Ventana_editar, text="ACTUALIZAR", command=lambda: Actualizar(new_password.get(),cod), height=1, width=12, bg="black", fg="white",font=("Comic Sans", 8,"bold")) 
   boton_actualizar.grid(row=2, column=1, columnspan=2, padx=10, pady=15)

   def Actualizar(new_password, new_con):
      try:  
         cursor = db.connection.cursor()

         sql="UPDATE t_estudiantes SET con_estudiante = %s WHERE cod_estudiante = %s"
         val = (new_password, new_con)
         cursor.execute(sql, val)
         db.connection.commit()

         messagebox.showinfo("EXITO", "¡Contraseña actualizada!")
         Ventana_editar.destroy()
         llenar_tabla()

      except Exception as e:
         messagebox.showerror("ERROR", "Hubo un error al actualizar la contraseña: " + str(e))
   
llenar_tabla()
root.mainloop()

