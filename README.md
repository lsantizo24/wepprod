Proceso para ejecutar el proyecto: 
Requerimientos:
 - linux 
 - Python 3 o mayor
 - Docker
 - Django (version estable)
 - postgresSQL
 - Bostrap 

----------------------------------
configuracion de base de datos:
Antes de hacer las migraciones configura el archivo settings.py en el apartado de la base de datos:
   DATABASES = 
        'default': 
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',  # O la dirección IP del contenedor de PostgreSQL
        'PORT': '5432',  # El puerto por defecto de PostgreSQL


----------------------------------

Crear una carpeta en tu disco local C o preferencia(ejemplo):
mkdir proyecto

crear el enviroment en tu carpeta (ejemplo)
 python3 -m venv env
 
Iniciar el enviroment 
 Source env/bin/activate
instalar django 
pip install django 
instalar pandas: 
pip install pandas

Nota: cabe mencionar que para la ejecución del proyecto total debes de configurar la estación del PLC para poder establecer la conexión y así poder leer el archivo log que se genera, mencionar que para eso debes de configurar la red compartida y crear un map a la computadora donde se va ejecutar la app y configurar el path(dirección del log) y asi se pueda contabilizar sin problemas. 
 

CLONAR el proyecto:
https://github.com/fatfreecrm/fat_free_crm?tab=readme-ov-file  (dejar pendiente hata que suba el proyecto a git)

-cambiar al modo enviroment y ejecuta los siguientes comandos:
    python manage.py makemigrations
    python manage.py migrate
 esto servirá para crear todas las tablas de la base de datos. y no tengas problemas al iniciar el proyecto


iniciar el proyecto:
Nota: para eso debes asegurar que tu contenedor de postgresQL se este ejecutando.

usar el comando: python manage.py runserver


de esta forma el proyecto se estará ejecutando, abre el proyecto en el localhost:8000 y visualiza el proyecto.


