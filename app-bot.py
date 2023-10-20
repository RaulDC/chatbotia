from tkinter import *
import re
import random
import sys
import subprocess

def get_response(user_info):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_info.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hola soy botCertus y te ayudaré a obtener información de tus cursos. \n Si deseas limpiar el chat escribe clean, si deseas cerrar sesión escribe cerrar.', ['hola', 'hi', 'saludos', 'buenas'], single_response=True)
    response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
    response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
    response('Qué deseas saber:  \n - Información básica de algun curso \n - Requisitos de algun curso', ['deseo', 'curso', 'informacion'], required_words=['deseo'])
    response('Información básica del curso: \n > Curso: Diseño de Soluciones con Inteligencia Artificial \n > Código de curso NRC: 13365 \n > La modalidad del curso es 100% virtual \n > El sílabo se encuentra en: https://tinyurl.com/f4ydy7z6 \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 3 créditos', ['informacion', 'basica', 'informacion basica', 'ia'], required_words=['ia'])
    response('Información básica del curso: \n > Curso: Diseño de Soluciones Blockchain \n > Código de curso NRC: 13330 \n > La modalidad del curso es 100% virtual \n > El sílabo se encuentra en: https://tinyurl.com/2s39547k \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 5 créditos', ['informacion', 'basica', 'informacion basica', 'blockchain'], required_words=['blockchain'])
    response('Información básica del curso: \n > Curso: Emprendimiento: Proyecto Integrador \n > Código de curso NRC: 13253 \n > La modalidad del curso es 100% presencial \n > Sedes: Surco - Independencia - Etc.  \n > El sílabo se encuentra en: https://tinyurl.com/yckfn7by \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 3 créditos', ['informacion', 'basica', 'informacion basica', 'emprendimiento'], required_words=['emprendimiento'])
    response('Información básica del curso: \n > Curso: Gestión de Marca Personal \n > Código de curso NRC: 11642 \n > La modalidad del curso es 100% virtual \n > El sílabo se encuentra en: https://tinyurl.com/ymtkxcm2 \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 2 créditos', ['informacion', 'basica', 'informacion basica', 'gestion' ,'marca', 'personal'], required_words=['marca', 'personal'])
    response('Información básica del curso: \n > Curso: Arquitectura de tecnología de la información \n > Código de curso NRC: 10016 \n > La modalidad del curso es 100% virtual \n > El sílabo se encuentra en: https://tinyurl.com/ymtkxcm2 \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 2 créditos', ['informacion', 'basica', 'informacion basica', 'arquitectura', 'tecnologia'], required_words=['arquitectura'])

    best_match = max(highest_prob, key=highest_prob.get)
    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['No entendí tu consulta', 'No estoy seguro de lo que quieres', 'Disculpa, ¿puedes intentarlo de nuevo?'][random.randrange(3)]
    return response

def enviar():
    msg = user_entry.get()  # Obtener el mensaje del usuario
    sender = "You"  # Establecer el remitente (puedes cambiar esto según tus necesidades)

    if not msg:
        return
    
    user_entry.delete(0, 'end') # Borrar el mensaje de entrada

    # Agregar el mensaje del usuario a la ventana de chat
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

    # Obtener la respuesta del bot y agregarla a la ventana de chat
    msg2 = f"Bot: {get_response(msg)}\n"
    chat_bg.configure(state=NORMAL)
    chat_bg.insert(END, msg2)
    chat_bg.configure(state=DISABLED)

    chat_bg.see(END)# Desplazar la ventana de chat hacia abajo

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

#CABECERA
title = Label(root, bg='#00205B', text='BIENVENIDO(A)', font=('helvetica', 13, "bold"), fg='#EAECEE', pady=10)
title.place(relwidth=1)

#DIVISOR
line = Label(root, width=450, bg='white')
line.place(relwidth=1, rely=0.07, relheight=0.012)

#Contenedor de texto o chat
chat_bg = Text(root, width=20, height=2, bg='#ABB2B9', fg='black', font=('helvetica', 12), padx=5, pady=5)
chat_bg.place(relheight=0.745, relwidth=1, rely=0.08)
chat_bg.configure(cursor="arrow", state=DISABLED)

#scroll bar
scrollbar = Scrollbar(chat_bg)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.configure(command=chat_bg.yview)

#bottom label
bottom_label = Label(root, bg='white', height=80)
bottom_label.place(relwidth=1, rely=0.825)

def on_enter(event):
    msg = user_entry.get()
    enviar(msg, "You")

#Caja de entrada de texto o mensaje
user_entry = Entry(bottom_label, bg='#ABB2B9', fg="black", font=('helvetica', 12))
user_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
user_entry.focus()
user_entry.bind("<Return>", on_enter)

#Boton de enviar
send_button = Button(bottom_label, height=1, width=3, bg='#00205B', text='➣', command=enviar, font=('helvetica', 23), activeforeground='white', fg='white', relief=FLAT, border=0, activebackground='#00205B')
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

root.mainloop()
