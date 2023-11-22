from tkinter import *
import re
import random
import sys
import subprocess
from connection import *

# Conexión a la base de datos
db = DataBase()

# Modificar la consulta SQL para obtener respuestas
db.cursor.execute("""
    SELECT respuesta, palabras_clave
    FROM tb_respuestas
""")
rows = db.cursor.fetchall()

# Almacenar respuestas en un diccionario
responses = {}
for row in rows:
    recognized_words = row[1].lower().split(',')
    responses[row[0]] = {'recognized_words': recognized_words}

# Realizar consulta a la base de datos una sola vez
db.cursor.execute("SELECT * FROM tb_respuestas")
rows = db.cursor.fetchall()

# Inicializar highest_prob en el ámbito global
highest_prob = {}

# Función para obtener la respuesta del bot
def get_response(msg):
    # Obtener la lista de palabras del usuario
    split_message = re.findall(r'\b\w+\b', msg.lower())
    print(f"User message words: {split_message}")
    response = check_all_messages(split_message)
    return response

# lectura de palabras requeridas
required_words = []

# message_probability
def message_probability(user_message, recognized_words):
    user_message_set = set(user_message)

    recognized_word_count = sum(1 for word in recognized_words if word in user_message_set)

    percentage = (recognized_word_count / len(recognized_words)) * 100 if recognized_words else 0

    print(f"User Message: {user_message}")
    print(f"Recognized Words: {recognized_words}")
    print(f"Recognized Word Count: {recognized_word_count}")
    print(f"Percentage: {percentage}")

    return int(percentage)

# check_all_messages
def check_all_messages(user_message):
    global highest_prob

    highest_prob = {}

    for response, data in responses.items():
        recognized_words = [re.sub(r'[^a-zA-Z0-9]', '', word.lower()) for word in data['recognized_words']]
        prob = message_probability(user_message, recognized_words)

        print(f"Response: {response}, Recognized Words: {recognized_words}, Probability: {prob}")

        if prob >= UMBRAL_MINIMO:
            process_response(response, recognized_words, user_message)

    print(f"Probabilities: {highest_prob}")

    if not highest_prob:
        return unknown()

    best_match = max(highest_prob, key=highest_prob.get)
    print(f"Best match: {best_match}")

    return best_match

def process_response(bot_response, recognized_words, user_message):
    global highest_prob
    highest_prob[bot_response] = message_probability(user_message, recognized_words)

def unknown():
    response = ['No entendí tu consulta', 'No estoy seguro de lo que quieres', 'Disculpa, ¿puedes intentarlo de nuevo?'][random.randrange(3)]
    return response

UMBRAL_MINIMO = 30  

def enviar():
    global highest_prob

    msg = user_entry.get()
    sender = "You"

    if not msg:
        return

    user_entry.delete(0, 'end')

    msg1 = f"{msg}> {sender}\n"
    chat_bg.configure(state=NORMAL)
    chat_bg.insert(END, msg1, "user_message")
    chat_bg.configure(state=DISABLED)

    if "clean" in msg.lower():
        limpiar_chat()
        return True

    if "cerrar" in msg.lower():
        root.destroy()
        redireccionar_pagina()
        return False

    bot_response = get_response(msg)
    print(f"User: {msg}")
    print(f"Bot Response: {bot_response}")
    
    msg2 = f"Bob> {bot_response}\n"
    chat_bg.configure(state=NORMAL)
    chat_bg.insert(END, msg2, "bot_message")
    chat_bg.configure(state=DISABLED)

    chat_bg.see(END)

    print(f"Final Probabilities: {highest_prob}")

def limpiar_chat():
    chat_bg.configure(state=NORMAL)
    chat_bg.delete('1.0', END)  # Eliminar todo el contenido del chat
    chat_bg.configure(state=DISABLED)

def redireccionar_pagina():
    root.destroy()
    subprocess.call([sys.executable, 'C:/Users/TUF GAMING/Documents/GitHub/chatbotia/login.py', 'htmlfilename.htm'])

def on_scroll(*args):
    chat_bg.yview(*args)

root = Tk()
root.title('ChatBob Certus')
root.resizable(width=False, height=False)
root.configure(width=470, height=550, bg='#00205B')

# CABECERA
title = Label(root, bg='#00205B', text='BIENVENIDO(A)', font=('helvetica', 13, "bold"), fg='#EAECEE', pady=10)
title.place(relwidth=1)

# BOTON CERRAR SESION
button_width = 12
button_height = 1

button_cerrar = Button(root, text="Cerrar Sesión", font=('helvetica', 10, "bold"), bg='#d32f2f', fg='white', command=redireccionar_pagina, width=button_width, height=button_height, activeforeground='#FF0914', relief=FLAT, border=0, activebackground='white')
button_cerrar.place(relx=0.73, rely=0.012)

# DIVISOR
line = Label(root, width=450, bg='white')
line.place(relwidth=1, rely=0.07, relheight=0.012)

# Contenedor de texto o chat
chat_bg = Text(root, width=20, height=2, bg='#ABB2B9', fg='black', font=('helvetica', 12), padx=5, pady=5, wrap='word')
chat_bg.place(relheight=0.745, relwidth=0.974, rely=0.08)
chat_bg.configure(state=DISABLED)

# Configura estilos
chat_bg.tag_configure("user_message", justify='right', foreground="#00205B")
chat_bg.tag_configure("bot_message", justify='left', foreground="#5c5a5a")

# Scroll bar
scrollbar = Scrollbar(root, command=on_scroll)
scrollbar.place(relheight=1, relx=0.974)
chat_bg.configure(yscrollcommand=scrollbar.set)

# Bottom label
bottom_label = Label(root, bg='white', height=80)
bottom_label.place(relwidth=1, rely=0.825)

def on_enter(event):
    enviar()

# Caja de entrada de texto o mensaje
user_entry = Entry(bottom_label, bg='#ABB2B9', fg="#5c5a5a", font=('helvetica', 12), relief=FLAT, border=0)
user_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
user_entry.insert(0, 'Escribir mensaje...')  # Texto predeterminado

user_entry.bind("<FocusIn>", lambda event: user_entry.delete(0, "end"))
user_entry.bind("<FocusOut>", lambda event: user_entry.insert(0, 'Escribir mensaje...'))

# Boton de enviar
send_button = Button(bottom_label, height=1, width=3, bg='#00205B', text='➣', command=enviar,
                     font=('helvetica', 23), activeforeground='white', fg='white', relief=FLAT, border=0,
                     activebackground='#00205B')
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

root.mainloop()
