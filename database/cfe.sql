create database cfe;
use cfe;

create table usuarios(
id_usuario integer auto_increment primary key,
nombre varchar(50) not null,
contrasena varchar(50) not null);

create table pagos(
id_pago integer auto_increment primary key,
direccion varchar(60),
num_medidor varchar(10),
lec_actual varchar(10),
periodo_consumo varchar(40),
fecha_pago varchar(10),
total_pago integer,
id_usuario integer references usuarios(id_usurio));



INSERT INTO `cfe`.`usuarios` (`id_usuario`, `nombre`, `contrasena`) VALUES ('1', 'Luis Sanchez', '12345678');
INSERT INTO `cfe`.`pagos` (`id_pago`, `direccion`, `num_medidor`, `lec_actual`, `periodo_consumo`, `fecha_pago`, `total_pago`, `id_usuario`) VALUES ('1', 'TULANCINGO HIDALGO ZONA CENTRO PARQUE JUAREZ No. 115', 'F153693', '00014', '10/03/2016 AL 10/07/2016', '02/08/2016', '47', '1');

