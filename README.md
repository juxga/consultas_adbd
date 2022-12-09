# Utilidad para compartir consultas de BD
## Instalación (requisitos)

- python, pip y python3-notebook (versión 3 de todos, instalar con apt (o el gestor de paquetes que utilices))
- postgreSQL - Como viene en el guión de instalación del lab.
- psycopg2 - Ver abajo
- pandas - Instalar con `pip install pandas`

### psycopg2

Es la librería para conectar de forma directa con postgreSQL desde python

Para OS basados en debian con gestor de paquetes apt:
1) `sudo apt install python3-dev libpq-dev` (Son las dependencias de psycopg2)
2) `pip install pyscopg2`  (Instalar psycopg2)

## Configuración
Lo más fácil para que podamos utilizar el mismo archivo es utilizar una base de datos y utilizar un usuario y contraseña común. Si no quieres, puedes cambiar el archivo `db_config.py` y utilizar los parámetros de configuración que prefieras.

Si optas por utilizar los datos en común y por defecto:
```
sudo -s
sudo -iu postgres
psql
CREATE USER usuariopython ENCRYPTED PASSWORD 'clavepython';
CREATE DATABASE bdepython OWNER usuariopython;
```

## Uso
Para abrir el cuaderno jupyter ejecuta: `jupyter-notebook`

Se abrirá el navegador, busca el archivo `consultas.ipynb` y ábrelo. 

Cambia el valor de la variable global `path_to_sql_script` con la ruta a tu script sql y ejecuta esa celda.

Para hacer una consulta solamente debes llamar a la función `query` con tu consulta, por ejemplo 
```
query("SELECT * FROM estudiantes;")
```
y ejecutar esa celda, lo cual te generará el resultado de tu consulta debajo.