import mysql.connector
import getpass
import re
import random
import hashlib

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
    def hash_password(password):
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        return md5.hexdigest()
    
    user = input("Ingrese el usuario: ")
    #password = hash_password(getpass.getpass("Ingrese su contraseña: "))
    password = getpass.getpass("Ingrese su contraseña: ")
    connection = connect_to_database()

    if connection:
        sql_select_Query = f"SELECT nom_estudiante, ape_estudiante FROM t_estudiantes WHERE cod_estudiante = '{user}' AND con_estudiante = '{password}'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchone()  # Obtenemos el primer registro (debería ser único)
        rp = cursor.rowcount

        if rp == 1:
            nombre = records[0]  # Índice 0 es el nombre
            apellido = records[1]  # Índice 1 es el apellido
            print("Inicio de sesión exitoso.")
            print("=====================================")
            print(f"¡Bienvenido(a), {nombre} {apellido}! Estoy aquí para ayudarte a resolver tus consultas.")
            print("=====================================")
            return True
        else:
            print("Inicio de sesión fallido. Por favor, verifique sus datos e intente nuevamente.")
            return False
    else:
        return False

# Funciones del chatbot
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

    response('Hola soy botCertus', ['hola', 'hi', 'saludos', 'buenas'], single_response=True)
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

if authenticate_user():
    while True:
        user_input = input('You: ')
        response = get_response(user_input)
        print("Bot: " + response)
else:
    print("No se pudo autenticar al usuario.")
