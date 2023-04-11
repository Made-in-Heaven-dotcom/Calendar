# Calendar

Creas un directorio y dentro sigues los siguientes pasos:

1. git clone https://github.com/Heaven-sFeel/Calendar.git

2. cd app

3. virtualenv env

4. .env/Scripts/activate.ps1

5. pip install django

6. python manage.py makemigrations

7. python manage.py migrate

8. python manage.py runserver

# Como desplegar la aplicacion web en Apache?

1. Descargar Apache y sus dependencias; instalar las dependencias primero: 
Apache - https://www.apachelounge.com/download/
Dev C++ - https://visualstudio.microsoft.com/visual-cpp-build-tools/

2. Descomprimir el archivo y pegarlo en el disco local.

3. Abrir CMD, buscar la ruta: C:/Apache24/bin/. con el comando (cd) y luego ejecutar los siguientes comandos:
Para instalar el servidor: httpd.exe -k install
Para iniciar el servidor: httpd.exe -k start

Ademas, estan los siguientes comandos:
Para parar el servidor: httpd.exe -k stop
Para reiniciar el servidor: httpd.exe -k resart
