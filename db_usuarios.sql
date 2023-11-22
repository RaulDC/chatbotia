drop database bd_certus;
create database bd_certus;
use bd_certus;

CREATE TABLE t_estudiantes (
    cod_estudiante VARCHAR(100) NOT NULL PRIMARY KEY,
    con_estudiante VARCHAR(100) NOT NULL,
    nom_estudiante VARCHAR(100) NOT NULL,
    ape_estudiante VARCHAR(100) NOT NULL
);

INSERT INTO t_estudiantes(cod_estudiante,con_estudiante,nom_estudiante,ape_estudiante)values('72806558','123','Raul','Diaz');

SELECT * FROM t_estudiantes;
DELETE FROM t_estudiantes WHERE cod_estudiante = 12345678;
Select * from t_estudiantes WHERE cod_estudiante = 92828134;
drop table t_estudiantes;

INSERT INTO t_estudiantes(cod_estudiante, con_estudiante, nom_estudiante, ape_estudiante)
VALUES
  ('72806551', '123456', 'Alfonso', 'Cuba'),
  ('72806559', 'password', 'María', 'González'),
  ('72806560', 'student', 'Juan', 'López'),
  ('72806561', 'abc123', 'Ana', 'Pérez'),
  ('72806562', 'qwerty', 'Pedro', 'Fernández'),
  ('72806563', 'letmein', 'Sofía', 'Martínez'),
  ('72806564', '123abc', 'Luis', 'Rodríguez'),
  ('72806565', 'abcdef', 'Carla', 'Gómez'),
  ('72806566', '111111', 'Diego', 'Hernández'),
  ('72806567', '222222', 'Lucía', 'Torres'),
  ('72806568', '333333', 'Miguel', 'Sanchez'),
  ('72806569', '444444', 'Elena', 'Ramírez'),
  ('72806570', '555555', 'Pablo', 'Vargas'),
  ('72806571', '666666', 'Valentina', 'Jiménez'),
  ('72806572', '777777', 'Gabriel', 'Morales'),
  ('72806573', '888888', 'Isabella', 'Silva'),
  ('72806574', '999999', 'Javier', 'Ortega'),
  ('72806575', 'abcdefg', 'Carmen', 'Dominguez'),
  ('72806576', 'password1', 'Manuel', 'Cruz'),
  ('72806577', 'qwerty1', 'Natalia', 'Rojas'),
  ('72806578', 'letmein1', 'Andrés', 'Paredes'),
  ('72806579', 'student1', 'Lorena', 'Mendoza'),
  ('72806580', 'abc1234', 'Hugo', 'Guerrero'),
  ('72806581', '1234567', 'Raquel', 'Soto'),
  ('72806582', 'password2', 'Camilo', 'Reyes');
  
INSERT INTO t_estudiantes VALUES
('72806560', '789', 'Carlos', 'Martínez'),
('72806561', '012', 'Ana', 'López'),
('72806562', '345', 'Javier', 'Ramírez'),
('72806563', '678', 'Marta', 'Fernández'),
('72806564', '901', 'Diego', 'Hernández'),
('72806565', '234', 'Elena', 'Torres'),
('72806566', '567', 'Sergio', 'García'),
('72806567', '890', 'Isabel', 'Ruiz'),
('72806568', '123', 'Antonio', 'Sánchez'),
('72806569', '456', 'Paula', 'Jiménez'),
('72806570', '789', 'Luis', 'Pérez'),
('72806571', '012', 'Carmen', 'Molina'),
('72806572', '345', 'Pablo', 'Castro'),
('72806573', '678', 'Silvia', 'Ortega'),
('72806574', '901', 'Mario', 'Gutiérrez'),
('72806575', '234', 'Eva', 'Navarro'),
('72806576', '567', 'Adrián', 'Vega'),
('72806577', '890', 'Laura', 'Morales'),
('72806578', '123', 'Jorge', 'Díaz'),
('72806579', '456', 'Rocío', 'Rojas'),
('72806580', '789', 'Ángel', 'Guerrero'),
('72806581', '012', 'Natalia', 'Suárez');

INSERT INTO t_estudiantes(cod_estudiante, con_estudiante, nom_estudiante, ape_estudiante)
VALUES
  ('72806584', 'password3', 'Luisa', 'García'),
  ('72806585', 'student2', 'Carlos', 'Pérez'),
  ('72806586', 'abc12345', 'Sara', 'Fernández'),
  ('72806587', 'qwerty3', 'Javier', 'Ramírez'),
  ('72806588', 'letmein2', 'Laura', 'Gómez'),
  ('72806589', '111222', 'Andrea', 'Torres'),
  ('72806590', 'password4', 'Martín', 'Sanchez'),
  ('72806591', 'abcdefg1', 'Eva', 'Hernández'),
  ('72806592', '1234abcd', 'Pablo', 'López'),
  ('72806593', '222333', 'Sandra', 'Martínez'),
  ('72806594', 'password5', 'Felipe', 'González'),
  ('72806595', 'student3', 'Mónica', 'Dominguez'),
  ('72806596', 'abcde123', 'Alejandro', 'Rojas'),
  ('72806597', 'qwerty4', 'Isabel', 'Ortega'),
  ('72806598', 'letmein3', 'Diego', 'Cruz'),
  ('72806599', '12345678', 'Patricia', 'Mendoza'),
  ('72806600', 'password6', 'Julián', 'Paredes'),
  ('72806601', 'abcdefg2', 'Luis', 'Guerrero'),
  ('72806602', '555666', 'Natalia', 'Soto'),
  ('72806603', '666777', 'Roberto', 'Morales'),
  ('72806604', 'qwerty5', 'Rosa', 'Ibáñez'),
  ('72806605', '777888', 'Antonio', 'Reyes'),
  ('72806606', 'letmein4', 'Ana María', 'Pérez'),
  ('72806607', 'password7', 'Hector', 'López');

INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('92828134','15089','Pedro','Martinez');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('13814374','17664','Maria','Perez');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('57221607','71156','Luis','Olas');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('96077472','07448','Lucia','Cabrera');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('53066252','29260','Carmen','Mirano');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('94816825','18046','Romario','Palacios');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('89134105','86952','Toribio','Rodriguez');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('47585688','47716','Matilde','Lopez');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('44310606','74661','Oscar','Huaman');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('63628258','96996','Jorge','Maicelo');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('92909233','62404','Alvaro','Sebastian');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('50842542','05421','Marcia','Cardozo');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('49433081','63163','Maria','Castañeda');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('16791174','96542','Valeri','Alba');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('94564817','42479','Alejandra','Villanueva');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('41176252','67326','Erick','Muñoz');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('44215617','76522','Ana','Gonzales');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('64927983','15520','Maritza','Muñoz');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('94024680','31983','Edwin','Ortiz');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('51164808','84577','Silvia','Tejada');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('78608256','82661','Martin','Terrones');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('14033601','90619','Ursula','Gutierrez');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('44536332','98797','Gustavo','Miranos');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('54665988','55922','Brayan','Gomez');
INSERT INTO `t_estudiantes` (`cod_estudiante`,`con_estudiante`,`nom_estudiante`,`ape_estudiante`) VALUES ('41983507','27923','Millie','Brown');

