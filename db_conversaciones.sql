CREATE TABLE t_conversaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cod_estudiante VARCHAR(100),
    mensaje_usuario TEXT NOT NULL,
    respuesta_bot TEXT NOT NULL,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cod_estudiante) REFERENCES t_estudiantes(cod_estudiante)
);