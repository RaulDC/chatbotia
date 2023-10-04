drop database bd_certus;
create database bd_certus;
use bd_certus;

CREATE TABLE t_estudiantes (
    cod_estudiante VARCHAR(100) NOT NULL,
    con_estudiante VARCHAR(100) NOT NULL,
    nom_estudiante VARCHAR(100) NOT NULL,
    ape_estudiante VARCHAR(100) NOT NULL
);

INSERT INTO t_estudiantes(cod_estudiante,con_estudiante,nom_estudiante,ape_estudiante)values('72806558','123','Raul','Diaz');

SELECT * FROM t_estudiantes;

