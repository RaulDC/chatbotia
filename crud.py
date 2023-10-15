import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import hashlib

# Función para insertar un nuevo registro
def insert_into():
    def hash_password(password):
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        return md5.hexdigest()
    
    def insert_record():
        cod = cod_entry.get()
        nom = nom_entry.get()
        ape = ape_entry.get()
        #con = hash_password(con_entry.get())
        con = con_entry.get()


        # Validar la contraseña
        if len(con) < 10:
            messagebox.showerror("Error", "La contraseña debe tener al menos 12 caracteres.")
            return
        

        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO t_estudiantes(cod_estudiante, nom_estudiante, ape_estudiante, con_estudiante) VALUES (%s, %s, %s, %s)", (cod, nom, ape, con))
            connection.commit()
            messagebox.showinfo("Éxito", "Registro insertado!")
            insert_window.destroy()
        except Error as e:
            messagebox.showerror("Error", "Error al insertar registro:\n" + str(e))

    insert_window = tk.Toplevel(root)
    insert_window.title("Insertar Registro")

    cod_label = tk.Label(insert_window, text="Código:")
    cod_label.pack()
    cod_entry = tk.Entry(insert_window)
    cod_entry.pack()

    nom_label = tk.Label(insert_window, text="Nombres:")
    nom_label.pack()
    nom_entry = tk.Entry(insert_window)
    nom_entry.pack()

    ape_label = tk.Label(insert_window, text="Apellidos:")
    ape_label.pack()
    ape_entry = tk.Entry(insert_window)
    ape_entry.pack()

    con_label = tk.Label(insert_window, text="Contraseña:")
    con_label.pack()
    con_entry = tk.Entry(insert_window)
    con_entry.pack()

    insert_button = tk.Button(insert_window, text="Insertar", command=insert_record)
    insert_button.pack()

# Función para seleccionar y mostrar todos los registros
def select():
    select_window = tk.Toplevel(root)
    select_window.title("Ver Registros")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM t_estudiantes")
        records = cursor.fetchall()

        for row in records:
            record_text = f"Código = {row[0]}\nNombre = {row[1]}\nApellido = {row[2]}\nContraseña = {row[3]}\n\n"
            record_label = tk.Label(select_window, text=record_text)
            record_label.pack()

    except Error as e:
        messagebox.showerror("Error", "Error al seleccionar registros:\n" + str(e))

# Función para modificar la contraseña de un registro
def update():
    def update_record():
        cod_estudiante = cod_est_entry.get()
        new_con = new_con_entry.get()

        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE t_estudiantes SET con_estudiante = %s WHERE cod_estudiante = %s", (new_con, cod_estudiante))
            connection.commit()
            messagebox.showinfo("Éxito", "Registro actualizado!")
            update_window.destroy()
        except Error as e:
            messagebox.showerror("Error", "Error al actualizar registro:\n" + str(e))

    update_window = tk.Toplevel(root)
    update_window.title("Modificar Contraseña")

    cod_est_label = tk.Label(update_window, text="Código del Estudiante:")
    cod_est_label.pack()
    cod_est_entry = tk.Entry(update_window)
    cod_est_entry.pack()

    new_con_label = tk.Label(update_window, text="Nueva Contraseña:")
    new_con_label.pack()
    new_con_entry = tk.Entry(update_window)
    new_con_entry.pack()

    update_button = tk.Button(update_window, text="Actualizar", command=update_record)
    update_button.pack()

# Función para eliminar un registro
def delete():
    def delete_record():
        cod_est = cod_est_entry.get()

        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM t_estudiantes WHERE cod_estudiante = %s", (cod_est,))
            connection.commit()
            messagebox.showinfo("Éxito", "Registro eliminado!")
            delete_window.destroy()
        except Error as e:
            messagebox.showerror("Error", "Error al eliminar registro:\n" + str(e))

    delete_window = tk.Toplevel(root)
    delete_window.title("Eliminar Registro")

    cod_est_label = tk.Label(delete_window, text="Código del Estudiante:")
    cod_est_label.pack()
    cod_est_entry = tk.Entry(delete_window)
    cod_est_entry.pack()

    delete_button = tk.Button(delete_window, text="Eliminar", command=delete_record)
    delete_button.pack()

# Configuración de la ventana principal
root = tk.Tk()
root.title("CRUD de Estudiantes")

# Menú
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Salir", command=root.quit)

crud_menu = tk.Menu(menu)
menu.add_cascade(label="CRUD", menu=crud_menu)
crud_menu.add_command(label="Insertar Registro", command=insert_into)
crud_menu.add_command(label="Ver Registros", command=select)
crud_menu.add_command(label="Modificar Contraseña", command=update)
crud_menu.add_command(label="Eliminar Registro", command=delete)

# Conexión a la base de datos
try:
    connection = mysql.connector.connect(host='localhost',
                                        database='bd_certus',
                                        user='root',
                                        password='72806558')
except mysql.connector.Error as e:
    messagebox.showerror("Error", "Error en la conexión a la base de datos:\n" + str(e))
    exit()

root.mainloop()