# Web scraper de mercadolibre, venex, Mexx y Full Hard
En este proyecto realizaremos un web scraper para cada una de las páginas web mencionadas.
## Recomendaciones
Recomiendo utilizar [pipenv](https://pipenv.pypa.io/en/latest/) para manejar el entorno virtual en el cual estaremos trabajando.
En caso de no poder instalar el mismo se puede utilizar otra herramienta como [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).
## Instalación y configuración del entorno virtual
Primero necesitamos instalar [pipenv](https://pipenv.pypa.io/en/latest/), en caso de tenerlo ya instalado se puede omitir este paso.
```bash
pip install pipenv

o

pip install virtualenv
```
En caso de querer comprobar si lo tenemos instalado, podemos hacerlo desde la consola, con el comando:
```bash
[~]$ pipenv --version
pipenv, version 2022.9.8

o 

[~]$ python3 -m virtualenv --version
virtualenv 20.7.2
```
Una vez instalada la herramienta con la que controlaremos nuestro entorno virtual, necesitamos clonar el repositorio del [proyecto](https://github.com/ispc-programador2022/GPQRR5.git) para luego movernos con 'cd' hasta la ubicación del mismo. Una vez dentro del directorio del proyecto, podemos ejecutar el entorno virtual de la siguiente manera
```bash
# Iniciamos el entorno virtual
$ pipenv shell
# Instalamos las dependencias necesarias
$ pipenv install -r requirements.txt
```
El proceso puede demorar, cuando termine de ejecutar ya tendremos todas las dependencias necesarias para trabajar con el proyecto instaladas.
En caso de necesitar desactivar el entorno virtual, se puede hacer con el comando
```bash
$ deactivate
```
## Base de datos
Por el momento la base de datos la tendremos solo de forma local, por ende sientanse libres de cambiar las configuraciones pertinentes para hacerlo funcionar en su entorno de trabajo, importante que utilicen **MYSQL** como motor.
Recordar que luego de cada cambio a la base de datos se necesita ejecutar el comando:
```bash
$ python3 manage.py makemigrations gestionScrapers
$ python3 manage.py migrate 
```
Siendo este el metodo para verificar que todas las configuraciones se hayan realizado correctamente.
## Contenido del repo
La carpeta de nombre **scraper** es desde la cual configuraremos y controlaremos nuestra aplicación web creada con [Django](https://docs.djangoproject.com/en/4.1/) esta misma tambien contiene el archivo que unifica todos los scrapers, llamado *mainScraper.py* el cual será explicado mas adelante, de momento lo unico que haremos sera cambiar el archivo 'settings.py' para [configurar la base de datos](https://docs.djangoproject.com/en/4.1/ref/databases/#mysql-notes).
Tambien tenemos otra carpeta llamada **gestionScrapers** la cual es la aplicación que se encarga de modelar la base de datos y tambien de gestionar las vistas.
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
Aparte de las vistas modeladas por nosotros, tambien podemos revisar el estado de la base de datos desde el [Panel de administración](http://127.0.0.1:8000/admin).
## Main scraper
Dentro de la carpeta llamada *scraper* tenemos un archivo que se llama *mainScraper.py*. El script esta compuesto por funciones que reciben como parametro un string ,la misma realiza una busqueda de todos los productos que tengan stock con ese nombre y los guarda en la base de datos.
Al final del archivo tenemos esta función:
```python
if __name__ == '__main__':
    items = ['microprocesador','placa de video','notebook','teclado']
    for item in items:
        searcherFullHard(item)
        searcherVenex(item)
        searcherMexx(item)
        searcherMeli(item)
        print(f'Termine de buscar: {item}\n\n\n')
```
```bash
# Podemos ejecutar este archivo con el comando
[~] python3 mainScraper.py
```
Se pueden agregar mas strings a la lista *items* para agregarlos a la busqueda de los scrapers.
Se puede revisar que los datos se guarden correctamente desde la vista [busqueda_productos](http://localhost:8000/busqueda_productos/) si se coloca un espacio y se presiona el boton buscar nos traerá todos los items que tengamos en la base de datos, de la misma forma podemos buscar cualquier item que hayamos guardado previamente en la base de datos.
Otra forma de revisar la integridad de la base de datos es desde el ya mencionado [Panel de administración](http://127.0.0.1:8000/admin) para ello primero tienen que crear un superuser, esto se hace con el comando:
```bash
$ python3 manage.py createsuperuser
``` 
Se debe proporcionar un usuario un correo y una contraseña lo suficientemente fuerte, para posteriormente logearse.
## Vistas
Dentro de la vista [busqueda_productos](http://localhost:8000/busqueda_productos/) podemos realizar las diferentes busquedas.
Dentro de la vista [pruebas_script](http://127.0.0.1:8000/pruebas_script/) podemos lanzar scripts via web para alimentar nuestra base de datos con nuevos items. Podemos ver el proceso desde la consola en la cual tenemos ejecutado nuestro servidor al finalizar nos redirigirá a una página web en la cual nos notificará del estado de la busqueda realizada. 
## Excel
En caso de querer transformar la base de datos a excel podemos hacerlo mediante el archivo **ploter_excel.py** el cual contiene una función llamada *bbdd_to_excel* la cual podremos llamar para realizar la transcripción de la misma.
Se puede ejecutar con el siguiente comando:
```bash
[~] Python3 ploter_excel.py
```
Ya que contiene la función
```python
if __name__ == '__main__':
    bbdd_to_excel()
```
### Integrantes:
    -Agustin Piccoli
    -Lina Mikaela Gutierrez Arribas
    -Lourdes Reynaldo
    -Horacio Eduardo Quiroga