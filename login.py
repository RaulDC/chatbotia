import mysql.connector
import tkinter as tk
from tkinter import messagebox
from mysql.connector import Error




def login():
    user = user_entry.get()
    password = password_entry.get()

    try:
        connection = mysql.connector.connect(
            user="root",
            password="72806558",
            database="bd_certus",
            port="3306"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM t_estudiantes WHERE cod_estudiante = %s AND con_estudiante = %s", (user, password))
            records = cursor.fetchall()

            if len(records) == 1:
                messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
            else:
                messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

    except Error as e:
        messagebox.showerror("Error", "Error al conectar a la base de datos:\n" + str(e))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Crear la ventana de inicio de sesión
root = tk.Tk()
root.title("Inicio de sesión")

# Personalizar el diseño
root.geometry("400x300")  # Tamaño de la ventana
root.configure(bg="#00205B")  # Color de fondo

# Crear etiquetas y campos de entrada de texto
user_label = tk.Label(root, text="Nombre de usuario:", bg="#00205B", fg="white", font=("Arial", 14))
user_label.pack(pady=10)
user_entry = tk.Entry(root, font=("Arial", 12))
user_entry.pack(pady=5)

password_label = tk.Label(root, text="Contraseña:", bg="#00205B", fg="white", font=("Arial", 14))
password_label.pack()
password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack(pady=10)

login_button = tk.Button(root, text="Iniciar sesión", command=login, bg="#2980b9", fg="white", font=("Arial", 12))
login_button.pack()

root.mainloop()