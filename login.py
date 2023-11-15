from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk, Image
import sys
import subprocess
from connection import *

class Login:
    
    def __init__(self,ventana_login):
        self.window=ventana_login  
        self.window.title("INICIAR SESION")
        self.window.geometry("330x370")
        self.window.resizable(0,0)
        self.window.config(bd=10)

        "--------------- Loginlogo --------------------"
        imagen_login=Image.open("C:/Users/TUF GAMING/Documents/GitHub/chatbotia/imagenes/logo-certus.png")
        nueva_imagen=imagen_login.resize((120,40))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana_login, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=20)

        "--------------- Marco --------------------"
        marco = LabelFrame(ventana_login, text="Ingrese sus datos",fg="black", font=("Arial", 10,"bold"))
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_cod=Label(marco,text="Código: ",font=("Arial", 10,"bold"), fg="black").grid(row=0,column=0,sticky='s',padx=5,pady=10)
        self.cod=Entry(marco,width=25)
        self.cod.focus()
        self.cod.grid(row=0, column=1, padx=5, pady=10)

        label_password=Label(marco,text="Contraseña: ",font=("Arial", 10,"bold"), fg="black").grid(row=1,column=0,sticky='s',padx=10,pady=10)
        self.password=Entry(marco,width=25,show="*")
        self.password.grid(row=1, column=1, padx=10, pady=10)
        
        "--------------- Frame botones --------------------"
        frame_botones=Frame(ventana_login)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_ingresar=Button(frame_botones,text="INGRESAR",command=self.Login,height=2,width=25,bg="#00205B",fg="white",font=("Arial", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)

    def Validar_formulario_completo(self):
        if len(self.cod.get()) !=0 and len(self.password.get()) !=0:
            return True
        else:
            messagebox.showerror("ERROR DE INGRESO", "Ingrese su código y contraseña!!!")

    def Validar_login(self, cod, password):
        db=DataBase()
        if self.Validar_formulario_completo():
            sql_select_Query = f"SELECT cod_estudiante, con_estudiante, nom_estudiante, ape_estudiante FROM t_estudiantes WHERE cod_estudiante = '{cod}' AND con_estudiante = '{password}'"
            cursor = db.connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()  # Obtenemos el primer registro (debería ser único)
            cursor.close()
            
            if records:
                return True, records[0][2], records[0][3]
            else:
                return False, None, None
            
    
    def Login(self):
        if(self.Validar_formulario_completo()):
            cod= self.cod.get()
            password= self.password.get()
            autenticado, nombre, apellido = self.Validar_login(cod, password)

            if autenticado:
                messagebox.showinfo("BIENVENIDO(A)", f'Estudiante {nombre} {apellido}') 
                ventana_login.destroy()    
                subprocess.call([sys.executable, 'C:/Users/TUF GAMING/Documents/GitHub/chatbotia/bot.py', 'htmlfilename.htm'])  
            else:
                messagebox.showerror("ERROR DE INGRESO", "Código o contraseña incorrectos") 

#verificar si el modulo ha sido ejecutado correctamente  
if __name__ == '__main__':
    ventana_login=Tk()
    application=Login(ventana_login)
    ventana_login.mainloop()

