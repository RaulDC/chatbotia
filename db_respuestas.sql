CREATE TABLE tb_respuestas (
    codigo VARCHAR(5),
    respuesta VARCHAR(255),
    palabra_clave VARCHAR(255),
	single_response BOOLEAN,
    required_word VARCHAR(255)
);
SELECT * FROM tb_respuestas;
DROP TABLE tb_respuestas;

-- Inserción de datos en la tabla
INSERT INTO tb_respuestas (codigo, respuesta, palabra_clave, single_response, required_word) VALUES 
	('R001', 'Hola soy botCertus', 'hola', 1 ,''),
	('R001', 'Hola soy botCertus', 'hi', 1 , ''),
	('R001', 'Hola soy botCertus', 'saludos', 1 ,''),
	('R001', 'Hola soy botCertus', 'buenas', 1 ,''),
	('R002', 'Estoy bien y tu?', 'como', 0 ,'como'),
	('R002', 'Estoy bien y tu?', 'estas', 0 ,'como'),
	('R002', 'Estoy bien y tu?', 'vas', 0 ,'como'),
	('R003', 'Siempre a la orden', 'gracias', 1 ,''),
	('R003', 'Siempre a la orden', 'te lo agradezco', 1 ,''),
	('R003', 'Siempre a la orden', 'thanks', 1 ,'');