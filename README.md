# ironranking-project

<p align="center">
  <img src="https://www.ironhack.com/assets/campus-image/madrid.jpg">
</p>

**Descripción**: 

El objetivo de este proyecto es crear una API cuyos endpoints nos ayuden a conseguir información de las pull requests que hemos realizado hasta ahora en nuestro bootcamp.

**Objetivos**: 

- Crear una API usando flask
- Hacer una análisis a través de llamadas a la API de Github que nos genere archivos json.
- Usar la librería pymongo de Python para generar una base de datos en mongoDB Compass.
- [Workshop] Docker, Heroku y Cloud databases.

**Desarrollo**:

Esta semana l@s ironhackers hemos trabajado muy, muy duro para sacar nuestros proyectos adelante, eso sí! ha sido todo un placer hacerlo en equipo y con la ayuda de nuestros instructors. ¿Quieres saber cómo lo hemos hecho? Lets' go! 

<p align="center">
  <img src="https://scontent-mad1-1.xx.fbcdn.net/v/t1.0-9/19511188_1882197358685727_2309459635894965835_n.png?_nc_cat=109&_nc_sid=85a577&_nc_ohc=c8K9CyXEBgMAX85ICq1&_nc_ht=scontent-mad1-1.xx&oh=beea34a8e5d888d3eb05ee382b191cf7&oe=5F9169E0">
</p>

--------------

El **primer paso** fue analizar los datos necesarios que íbamos a necesitar en nuestra bases de datos y una vez encontrados, generamos llamadas a la API de Github para obtener las urls de las pull de nuestro repo *datamad0820*. En mi caso, generé 2 archivos json para subir a **mongoDB**, uno para recoger todas las pulls y otro para mostrar todos los labs. 

Los datos recogidos en cada colección son los siguientes:

**Pulls**
- lab_id
- user_id
- user_name
- name_lab
- state
- created
- closed

**Labs**
- lab_id
- user_id
- user_name
- name_lab
- instructor
- lab_shared
- img

Una vez creada la base de datos, realizamos la conexión a nuestra **API** ubicada en localhost puerto 3000.

Los endpoints generados son los siguientes:

1. *src/controllers/student_controller.py*\
Crear un nuevo alumno en la colección de las pulls:\
**/student/create/studentname/**

2. *src/controllers/student_controller.py*\
Crear una lista con los nombres de todos los alumnos:\
**/student/all**

3. *src/controllers/lab_controller.py*
Crear un nuevo lab en la colección de los labs:\
**/lab/create/labname**

4. *src/controllers/lab_controller.py*\
Devuelve un meme random\
**lab/lab_name/meme**

5. *src/controllers/lab_controller.py*\
**/lab/name_lab/search**\
El numero de PR abiertas\
El numero de PR cerradas\
El porcentaje de PR abiertas\
El porcentaje de PR cerradas\
La lista de memes únicos\
El tiempo máximo de correción del lab\
El tiempo mínimo de correción del lab\
El promedio de tiempo de correción del lab








