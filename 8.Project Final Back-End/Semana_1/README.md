# Cuestionario del módulo: Inicio del proyecto

**1.**Question 1

Para servir los archivos estáticos en una aplicación Django, ¿cuál de los siguientes pasos debe seguir? Seleccione todas las opciones que correspondan.

1 / 1 point

- [x]  **Incluya la aplicación staticfiles en la lista INSTALLED_APPS.**

Correct

Correcto. La aplicación **django.contrib.staticfiles** debe estar instalada. Por lo general, no está instalada por defecto.

- [x]  **Cargue la etiqueta de plantilla estática**

Correct

Correcto. Use la etiqueta **{% load static %}** para cargar la URL estática.

- [ ]  **Sirva el archivo con static/<file-name> como su ruta.**
- [x]  **Establezca STATIC_ROOT en el directorio en el que se almacenan los archivos estáticos.**

Correct

Correcto. Esta variable se establece en el archivo settings.py del proyecto.

**2.**Question 2

Para permitir que Django busque los archivos estáticos en carpetas que no sean la carpeta **STATIC_ROOT** , ¿cuál de las siguientes variables debe definir en el archivo settings.py?

1 / 1 point

**STATIC_ URL**

**`STATICFILES_DIRS`**

**MEDIA_ROOT**

**collectstatic**

Correct

Correcto. Esta variable contiene una lista de los directorios desde los que se recopilan los archivos estáticos.

**3.**Question 3

Complete la siguiente frase. La opción de comando **dbshell** del script manage.py abre un ___________________.

1 / 1 point

**terminal de comando**

**Terminal bash de Git**

**consola python**

**`cliente de línea de comandos de base de datos`**

Correct

Correcto. Para abrir la consola de Python dentro del proyecto Django, use la opción de comando de shell de manage.py.

**4.**Question 4

¿Cuál de las siguientes funciones puede usar para definir rutas URL? Seleccione todas las opciones que correspondan.

1 / 1 point

- [x]  **include()**

Correct

Correcto. La función **include()** se usa para incluir definiciones de patrones de URL de una aplicación en el proyecto.

- [x]  **path()**

Correct

Correcto. La función **path()** agrega una ruta de URL a la lista **urlpatterns** mediante la asignación de una cadena de URL a la función de vista.

- [x]  **re_path()**

Correct

Correcto. Puede usar la función **re_path()** para crear la ruta de URL si necesita asignar una función de vista a un patrón de URL de una cadena sin formato.

- [ ]  **render()**

**5.**Question 5

¿Cuál de las siguientes afirmaciones es verdadera? Seleccione todas las opciones que correspondan.

1 / 1 point

- [x]  **El comando git push envía archivos del repositorio local al repositorio remoto.**

Correct

Correcto. Utiliza el comando push para sincronizar el repositorio remoto con el repositorio local.

- [x]  **El comando git add envía archivos desde el área de trabajo al área de preparación.**

Correct

Correcto. Los archivos recién agregados o modificados en el repositorio de trabajo se agregan primero al área de preparación antes de enviarlos al repositorio local.

- [ ]  **El comando git commit envía archivos desde el repositorio de trabajo al repositorio local.**
- [ ]  **El comando git add envía archivos desde el área de ensayo al repositorio local.**

**6.**Question 6

¿Cuáles de las siguientes opciones se conocen como herramientas de control de versiones? Seleccione todas las opciones que correspondan.

1 / 1 point

- [x]  **SVN**

Correct

Correcto. SVN es una de las herramientas de control de versiones más populares.

- [x]  **Git**

Correct

Correcto. Git es la herramienta más utilizada para el control de versiones.

- [ ]  **GitHub**
- [x]  **Mercurial**

Correct

Correcto. Mercurial es un sistema de control de versiones.

**7.**Question 7

¿Cuáles de las siguientes son formas de descargar un repositorio de GitHub en su computadora local? Seleccione todas las opciones que correspondan.

1 / 1 point

- [ ]  **Utiliza el comando git pull.**
- [x]  **Utiliza el comando git clone.**

Correct

Correcto. Utiliza el comando **git clone** para crear una copia local del repositorio de GitHub.

- [ ]  **Utiliza el comando git restore.**
- [x]  **Puede descargar el repositorio como un archivo ZIP.**

Correct

Correcto. El contenido de un repositorio de GitHub se puede descargar como un archivo ZIP.

**8.**Question 8

¿Cómo sube archivos en un repositorio local a GitHub?

1 / 1 point

**`Utiliza el comando git push.`**

**Utiliza la interfaz web de GitHub.**

**Utiliza el comando git add.**

**Utiliza el comando git commit.**

Correct

Correcto. El comando git push transfiere los archivos del repositorio local al repositorio de GitHub.

**9.**Question 9

¿Cuál de los siguientes requisitos se debe cumplir para acceder a la interfaz de administración de Django? Seleccione todas las opciones que correspondan.

1 / 1 point

- [x]  **Debe incluir django.contrib.admin en la lista INSTALLED_APPS en el archivo settings.py.**

Correct

Correcto. La aplicación de administración generalmente se instala de forma predeterminada en un proyecto de Django.

- [x]  **Debe crear al menos un superusuario.**

Correct

Correcto. Debe crear al menos un superusuario porque necesita credenciales de superusuario para iniciar sesión en la interfaz de administración.

- [ ]  **El proyecto Django debe tener al menos una aplicación.**
- [x]  **Debe ejecutar las migraciones.**

Correct

Correcto. Debe ejecutar las migraciones para crear las tablas necesarias en la base de datos para almacenar usuarios y grupos.

**10.**Question 10

¿Cuál de las siguientes opciones no es un tipo de usuario en Django?

1 / 1 point

**`admin`**

**superuser**

**staff**

**active**

Correct