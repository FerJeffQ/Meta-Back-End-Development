# Cuestionario del módulo: Introducción a Django

## **1.**Pregunta 1

¿Cuáles de las siguientes son algunas de las diferencias entre los comandos **django-admin** y **manage.py**? Seleccione todas las opciones que correspondan.

1 / 1 punto

- [ ]  **No existe diferencia entre django-admin y manage.py.**
- [x]  **django-admin se instala en el entorno Python cuando instala Django con la utilidad PIP. El archivo manage.py se crea dentro de cada carpeta de proyecto de Django.**

`Correcto. Encontrará **manage.py** en la carpeta del proyecto y **django-admin** en la carpeta de *scripts* de Python.`

- [x]  **django-admin es una utilidad de línea de comandos y manage.py es un *script* de Python.**

`Correcto. **manage.py** debe ejecutarse como un módulo de Python. **django-admin** es un archivo ejecutable que se ejecuta en la terminal.`

- [x]  **manage.py se prefiere a django-admin.**

`Correcto. **manage.py** se ejecuta dentro de la carpeta del proyecto. Al utilizar **django-admin**, debe establecer la variable **--settings** en el archivo *settings.py* del proyecto requerido.`

## **2.**Pregunta 2

El archivo **urls.py** está en el paquete del proyecto y en el paquete de la aplicación.

- `R:` **Verdadero**

`Correcto. El **urls.py** de la carpeta del proyecto define la **URLConf**. El **urls.py** de la aplicación se incluye en la lista de **urlpatterns** del proyecto.`

- **Falso**

## **3.**Pregunta 3

¿Qué sucede cuando la función de vista creada dentro del archivo **views.py** se modifica mientras el servidor de desarrollo aún se está ejecutando?

- **La página web en el navegador se vuelve a cargar automáticamente para reflejar los nuevos cambios.**
- **El servidor deberá reiniciarse manualmente para reflejar los nuevos cambios.**
- `R:` **El servidor de desarrollo se volverá a cargar automáticamente y los cambios se reflejarán en la recarga de la página web.**
- **El servidor de desarrollo finalizará.**

`Correcto. Podrá ver los cambios que el servidor vuelve a cargar en el indicador de comando una vez que guarde el archivo **views.py**. Al volver a cargar manualmente la página web, se reflejarán los nuevos cambios.`

**4.**Pregunta 4

¿Dónde se encuentra el archivo **manage.py**?

- `R:` **Dentro de la carpeta del contenedor externo del proyecto**
- **Dentro de la carpeta del paquete de la aplicación**
- **Dentro de la carpeta del paquete del proyecto**
- **Dentro de la carpeta de *scripts* del entorno Python actual.**

`Correcto. En la carpeta externa del proyecto, encontrará el *script* **manage.py** junto con el paquete de la aplicación y el paquete del proyecto.`

## **5.**Pregunta 5

By default, Django's built-in development server runs on the local machine with IP address 127.0.0.1 and port 8000.

- `R:` **True**
- **False**

`Correct! The **runserver** command option for **django-admin** and manage.py starts the development server and listens to the incoming requests on port 8000 of the localhost by default.`

## **6.**Pregunta 6

Does the View layer in Django correspond to the View layer in MVC architecture?

- **Yes**
- `R:` **No**

`Correct! Django’s view layer performs the role of Controller in MVC architecture.`

**7.**Pregunta 7

Which of the following statements is true about the view function? Select all that apply.

- [x]  **Loads the template**
- [x]  **Receives the request object from the server.**

`Correct! The view function receives the request object from the server context.`

- [x]  **Returns a response to the client**

`Correct! The view does return a **HttpResponse** to the client.`

- [x]  **Interacts with the model layer**

`Correct! The view performs the CRUD operations on the models.`

## **8.**Pregunta 8

Which of the following statements are true about a model in Django? Select all that apply.

- [ ]  **The Model defines the processing logic of the Django application.**
- [x]  **A model is a Python class**

`Correct! A model class represents a database table structure.`

- [x]  **Model class attributes are used to create a database table.**

`Correct! Django performs migration to construct a database table from the model attributes.`

- [ ]  **A Django Template fetches the data from a Model and displays it on a web page.**

## **9.**Pregunta 9

Which Python module is used from the command-line to create a virtual environment?

- `R:` **venv**
- **startapp**
- **pip3**
- **shell**

`Correct! The Python virtual environment is created with the command **python –m venv envname**.`

## **10.**Pregunta 10

Which of these pre-built apps are installed in a Django project by default? Select all that apply.

- [x]  **django.contrib.admin**

`Correct! This app is added in **INSTALLED_APPS** by default.`

- [x]  **django.contrib.auth**

`Correct! This app is added in **INSTALLED_APPS** by default.`

- [x]  **django.contrib.messages**

`Correct! This app is added in **INSTALLED_APPS** by default.`

- [ ]  **postgress app**