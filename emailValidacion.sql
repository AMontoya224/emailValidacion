

USE email_validacion;

SELECT *
FROM email;

INSERT INTO email(correo, create_at) 
VALUES('prueba@gmail.com', NOW());

DELETE FROM dojos WHERE id>0;