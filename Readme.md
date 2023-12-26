 # Proyecto final de coder
 ## Participantes 
 ### Exequiel Moreyra y Nicolas Dondo
 ### Comisión 47790

 # Configuración inicial del proyecto
 0. Crear una carpeta para inicializar el proyecto en este caso se llama: entregafinal-coder47790-moreyra
 1. Abrir la carpeta en un editor de codigo en este caso se utilizó Visual Studio Code
 2. Realizar instalacion de django : pip install django e inicializar el servidor con el siguiente    comando: python manage.py runserver
 3. Instalacion del entorno virtual:  python -m venv .venv, luego de la instalacion, presionar **Ctrl + shift + p** y sleccionar python interpreter. Cerrar la terminal y volver a abrir otra para que se pueda ejecutar el 
 emtorno virtual, al principio del script de la terminal tiene que estar en **venv**.
 4. Creacion de la app (en este caso Blog)de la siguiente manera: **django-admin startproject blog**
 5. Al tener todo instalado, cerrar el servidor y ejecutar los siguientes comandos para realizar la migracion:
  **python manage.py makemigrations**
  **python manage.py migrate**
  **python manage.py runserver**
6. El proyecto se basa en un blog dedicado al cine y a las peliculas, donde se resistrar un usuario, loguearse, realizar un post y editarlo. Seccion nosotros, se puede ver una pequeña descripcion de los creadores con un boton que redirige al perfil de **LinkedIn** de cada uno.
7. Posee herencia de HTML en todas las vistas y secciones de la app, asi tambien varios estilos CSS.

