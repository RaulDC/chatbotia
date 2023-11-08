from tkinter import *
import re
import random
import sys
import subprocess
import mysql.connector

# Conexión a la base de datos
connection = mysql.connector.connect(
    host="bbdyxtq2xayjozsfil1n-mysql.services.clever-cloud.com",
    user="u4wtydnovodwvldv",
    password="oNdjuw7Jl28J3A26x0U3",
    database="bbdyxtq2xayjozsfil1n"
)
cursor = connection.cursor()

# Modificar la consulta SQL para obtener respuestas
cursor.execute("""
    SELECT respuesta, palabras_clave
    FROM tb_respuestas
""")
rows = cursor.fetchall()

# Almacenar respuestas en un diccionario
responses = {}
for row in rows:
    recognized_words = row[1].lower().split(',')
    responses[row[0]] = {'recognized_words': recognized_words}

# Realizar consulta a la base de datos una sola vez
cursor.execute("SELECT * FROM tb_respuestas")
rows = cursor.fetchall()

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

    msg1 = f"{sender}: {msg}\n"
    chat_bg.configure(state=NORMAL)
    chat_bg.insert(END, msg1)
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
    msg2 = f"Bot: {bot_response}\n"
    chat_bg.configure(state=NORMAL)
    chat_bg.insert(END, msg2)
    chat_bg.configure(state=DISABLED)

    chat_bg.see(END)

    print(f"Final Probabilities: {highest_prob}")



def limpiar_chat():
    chat_bg.configure(state=NORMAL)
    chat_bg.delete('1.0', END)  # Eliminar todo el contenido del chat
    chat_bg.configure(state=DISABLED)

def redireccionar_pagina():
    subprocess.call([sys.executable, 'C:/Users/TUF GAMING/Documents/GitHub/chatbotia/login.py', 'htmlfilename.htm'])

root = Tk()
root.title('ChatBotIA Certus')
root.resizable(width=False, height=False)
root.configure(width=470, height=550, bg='#00205B')

# CABECERA
title = Label(root, bg='#00205B', text='BIENVENIDO(A)', font=('helvetica', 13, "bold"), fg='#EAECEE', pady=10)
title.place(relwidth=1)

# DIVISOR
line = Label(root, width=450, bg='white')
line.place(relwidth=1, rely=0.07, relheight=0.012)

# Contenedor de texto o chat
chat_bg = Text(root, width=20, height=2, bg='#ABB2B9', fg='black', font=('helvetica', 12), padx=5, pady=5)
chat_bg.place(relheight=0.745, relwidth=1, rely=0.08)
chat_bg.configure(cursor="arrow", state=DISABLED)

# Scroll bar
scrollbar = Scrollbar(chat_bg)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.configure(command=chat_bg.yview)

# Bottom label
bottom_label = Label(root, bg='white', height=80)
bottom_label.place(relwidth=1, rely=0.825)

def on_enter(event):
    enviar()

# Caja de entrada de texto o mensaje
user_entry = Entry(bottom_label, bg='#ABB2B9', fg="black", font=('helvetica', 12))
user_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
user_entry.focus()
user_entry.bind("<Return>", on_enter)

# Boton de enviar
send_button = Button(bottom_label, height=1, width=3, bg='#00205B', text='➣', command=enviar,
                     font=('helvetica', 23), activeforeground='white', fg='white', relief=FLAT, border=0,
                     activebackground='#00205B')
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

root.mainloop()
