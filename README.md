# Web scraper de mercadolibre, venex, compragamer y Amazon
En este proyecto realizaremos un web scraper para cada una de las páginas web mencionadas y luego realizaremos una comparativa de precios.

## Recomendaciones
Recomiendo utilizar [pipenv](https://pipenv.pypa.io/en/latest/) para manejar el entorno virtual en el cual estaremos trabajando.

## Instalación y configuración del entorno virtual
Primero necesitamos instalar [pipenv](https://pipenv.pypa.io/en/latest/), en caso de tenerlo ya instalado se puede omitir este paso.
```bash
pip install pipenv
```
En caso de querer comprobar si lo tenemos instalado, podemos hacerlo desde la consola, con el comando:
```bash
[~]$ pipenv --version
pipenv, version 2022.9.8
```
Una vez instalada la herramienta con la que controlaremos nuestro entorno virtual, necesitamos clonar el repositorio del [proyecto](https://github.com/ispc-programador2022/GPQRR5.git) para luego movernos con 'cd' hasta la ubicación del mismo. Una vez dentro del directorio del proyecto, podemos ejecutar el entorno virtual de la siguiente manera
```bash
# Iniciamos el entorno virtual
$ pipenv shell
# Instalamos las dependencias necesarias
$ pipenv install -r requirements.txt
```
Veremos que nos ha generado uno o dos archivos, llamados 'Pipfile' y 'Pipfile.lock' no debemos hacer nada con dichos archivos. *tampoco debemos pushearlos al repositorio*.
El proceso puede demorar, cuando termine de ejecutar ya tendremos todas las dependencias necesarias para trabajar con el proyecto instaladas.
En caso de necesitar desactivar el entorno virtual, se puede hacer con el comando
```bash
$ deactivate
```
## Base de datos
Por el momento la base de datos la tendremos solo de forma local, hasta que configuremos el acceso remoto, por ende sientanse libres de cambiar las configuraciones pertinentes para hacerlo funcionar en su entorno de trabajo, importante que utilicen **MYSQL** como motor.
Recordar que luego de cada cambio a la base de datos se necesita ejecutar el comando:
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
Siendo este el metodo para verificar que todas las configuraciones se hayan realizado correctamente.
## Contenido del repo
Tenemos varias carpetas dentro del repositorio, las que tienen el nombre de diferentes paginas web, son las que utilizaremos para albergar los respectivos scrapers, en cambio la carpeta de nombre **scraper** es desde la cual configuraremos y controlaremos nuestra aplicación web creada con [Django](https://docs.djangoproject.com/en/4.1/) de momento lo unico que haremos sera cambiar el archivo 'settings.py' para configurar la base de datos en caso de necesitarlo.
## Uso
Se puede ejecutar el servidor local con el comando
```bash
$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 26, 2022 - 15:28:25
Django version 4.1.2, using settings 'scraper.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
En caso de que todo haya salido bien deberia mostrarnos ese output.
## Venex scraper
Dentro de la carpeta llamada *venex* tenemos un archivo que se llama *scraper_venex.py* para configurar el mismo necesitamos agregar el path al repositorio en la tercera linea, cada quien tendra un directorio diferente, es importante en windows que se reemplacen las barras invertidas por barras comunas (\ --> /) ya que es el caracter con el que se escapan caracteres en python y lo interpretará de forma erronea esta configuración será removida mas tarde cuando unifiquemos todo dentro de la carpeta '*scraper*' con un solo archivo conteniendo las diferentes funciones para todos los scrapers. El resto del script esta compuesto por una función que recibe como parametro un string el cual realiza una busqueda de todos los productos que tengan stock con ese nombre y los guarda en la base de datos, se puede revisar que los mismos se guarden correctamente desde el [Panel de administración](http://127.0.0.1:8000/admin) para ello seguramente tengan que crear un superuser, esto se hace con el comando:
```bash
$ python3 manage.py createsuperuser
``` 
Se debe proporcionar un usuario un correo y una contraseña lo suficientemente fuerte, para posteriormente logearse en el ya mencionado [Panel de administración](http://127.0.0.1:8000/admin).
### Integrantes:
    -Agustin Piccoli
    -Lina Mikaela Gutierrez Arribas
    -Lourdes Reynaldo
    -Horacio Quiroga
    -Ignacio Rocha