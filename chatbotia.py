import mysql.connector
import getpass
import re
import random
# Variables globales para almacenar el curso seleccionado
selected_course = None

# Conexión a la base de datos MySQL
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='bd_certus',
            user='root',
            password='72806558'
        )
        return connection
    except mysql.connector.Error as e:
        print("Error en la consulta", e)
        return None

# Autenticación de usuario
def authenticate_user():
    user = input("Ingrese el usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ")
    connection = connect_to_database()

    if connection:
        sql_select_Query = f"SELECT * FROM t_estudiantes WHERE cod_estudiante = '{user}' AND con_estudiante = '{password}'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        rp = cursor.rowcount

        if rp == 1:
            print("Inicio de sesión exitoso!")
            return True
        else:
            print("Error en las credenciales")
            return False
    else:
        return False

# Funciones del chatbot
def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
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

# Función para obtener información básica del curso
def get_course_info(course):
    if course == "ia":
        return "La modalidad del curso es 100% virtual.\nEl sílabo se encuentra en: https://tinyurl.com/f4ydy7z6\nHay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo.\nEl curso equivale a 3 créditos."
    # Agrega más cursos y sus detalles aquí

def check_all_messages(message):
    global selected_course  # Agrega esta línea para declarar selected_course como una variable global

    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        message_prob = message_probability(message, list_of_words, single_response, required_words)
        highest_prob[bot_response] = message_prob

    response('Hola soy botCertus', ['hola', 'hi', 'saludos', 'buenas'], single_response=True)
    response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
    response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
    response('Arquitectura y Diseño con IA', ['sexto ciclo', 'sexto', 'cursos de sexto'], single_response=True)

    if selected_course:
        if any(word in message for word in ['ia', 'inteligencia', 'artificial']):
            selected_course = "ia"
            response('¿Qué deseas saber del curso de IA: \n - Información básica del curso \n - Requisitos del curso', ['informacion', 'basica', 'requisitos', 'curso'], required_words=[selected_course])
        else:
            response('No entendí tu consulta', [], single_response=True)
    else:
        response('Información básica del curso: \n > La modalidad del curso es 100% virtual \n > El sílabo se encuentra en: https://tinyurl.com/f4ydy7z6 \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 3 créditos', ['informacion', 'basica'], required_words=[selected_course])

    best_match = max(highest_prob, key=highest_prob.get)
    return best_match



def unknown():
    response = ['No entendí tu consulta', 'No estoy seguro de lo que quieres', 'Disculpa, ¿puedes intentarlo de nuevo?'][random.randrange(3)]
    return response

if authenticate_user():
    while True:
        user_input = input('You: ')
        response = get_response(user_input)
        print("Bot: " + response)
else:
    print("No se pudo autenticar al usuario.")
