CREATE DATABASE IF NOT EXISTS bd_certus;

USE bd_certus;

CREATE TABLE tb_respuestas (
    id_respuesta INT AUTO_INCREMENT PRIMARY KEY,
    respuesta TEXT,
    palabras_clave TEXT
);

-- Insertar algunas respuestas personalizadas
INSERT INTO tb_respuestas (respuesta, palabras_clave) VALUES
('¡Hola! Soy un bot personalizado.', 'hola,hi,saludos'),
('Estoy bien, ¿y tú?', 'como,estas,va,vas,sientes'),
('Gracias, siempre estoy aquí para ayudarte.', 'gracias,te lo agradezco,thanks'),
('Qué deseas saber:  \n - Información básica de algun curso \n - Requisitos de algun curso', 'deseo, curso, informacion'),
('Información básica del curso: \n > Curso: Diseño de Soluciones con Inteligencia Artificial \n > Código de curso NRC: 13365 \n > La modalidad del curso es 100% virtual \n > El sílabo se encuentra en: https://tinyurl.com/f4ydy7z6 \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 3 créditos', 'ia'),
('Información básica del curso: \n > Curso: Diseño de Soluciones Blockchain \n > Código de curso NRC: 13365 \n > La modalidad del curso es 100% virtual \n > El sílabo se encuentra en: https://tinyurl.com/f4ydy7z6 \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 3 créditos', 'blockchain'),
('Información básica del curso: \n > Curso: Emprendimiento: Proyecto Integrador \n > Código de curso NRC: 13365 \n > La modalidad del curso es 100% virtual \n > El sílabo se encuentra en: https://tinyurl.com/f4ydy7z6 \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 3 créditos', 'emprendimiento'),
('Información básica del curso: \n > Curso: Gestión de Marca Personal \n > Código de curso NRC: 13365 \n > La modalidad del curso es 100% virtual \n > El sílabo se encuentra en: https://tinyurl.com/f4ydy7z6 \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 3 créditos', 'marca, personal'),
('Información básica del curso: \n >Curso: Arquitectura de tecnología de la información \n > Código de curso NRC: 13365 \n > La modalidad del curso es 100% virtual \n > El sílabo se encuentra en: https://tinyurl.com/f4ydy7z6 \n > Hay un total de 4 evaluaciones, una evaluación cada 4 semanas. Para obtener más información, revisa la página 6 del sílabo. \n > El curso equivale a 3 créditos', 'arquitectura');
