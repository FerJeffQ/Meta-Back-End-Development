# Cuestionario del módulo: La pila completa usando Django

**1.**Question 1

De forma predeterminada, sin ninguna configuración e instalación adicional, el servidor de desarrollo incorporado de Django se ejecuta en la máquina local con la dirección IP 127.0.0.1 y el puerto 3306.

1 / 1 point

**Verdadero**

**`Falso`**

Correct

Correcto. La opción del comando **runserver** para **django-admin** y **manage.py** inicia el servidor de desarrollo y escucha las solicitudes entrantes en el puerto 8000 del host local de forma predeterminada. El puerto 3306 es el predeterminado cuando se usa un servidor de MySQL con Django.

**2.**Question 2

Una colección de objetos obtenidos de un modelo de Django mediante llamadas de funciones como **Model.objects.all()** será:

1 / 1 point

**Tupla**

**Lista**

**Objeto JSON**

**`QuerySet`**

Correct

Correcto. Un QuerySet representa una colección de objetos de la base de datos.

**3.**Question 3

¿Cuáles de las siguientes afirmaciones sobre la función de vista son verdaderas? Elija todas las opciones que correspondan.

1 / 1 point

- [ ]  **Convierte el modelo Queryset en consultas SQL en un proceso llamado ORM.**
- [x]  **Devuelve una respuesta al cliente.**

Correct

Correcto. La vista devuelve **HttpResponse** al cliente.

- [x]  **Carga la plantilla**

Correct

Correcto. La vista carga una plantilla, completa los datos de contexto y los devuelve al navegador del cliente.

- [x]  **Interactúa con la capa del modelo.**

Correct

Correcto. La vista realiza las operaciones CRUD en los modelos.

- [x]  **Recibe el objeto de solicitud del servidor.**

Correct

Correcto. La función de vista recibe el objeto de solicitud del contexto del servidor.

**4.**Question 4

_________ es la clase que contiene la implementación de Django para pruebas unitarias en Python.

1 / 1 point

- [x]  **TestCase**

Correct

Correcto. **TestCase** contiene la implementación de pruebas unitarias en un paquete llamado **django.tests.**

- [ ]  **TestUnit**
- [ ]  **UnitTest**
- [x]  **TestCaseUnit**

Correct

No exactamente. Mire nuevamente el video **Resumen: Sus conocimientos sobre Django** en el Módulo 3, Lección 1.

**5.**Question 5

¿Cuál de los siguientes no es un método de HTTP?

1 / 1 point

**POST**

**DELETE**

**`CREATE`**

**PUT**

Correct

Correcto. forma parte de una operación de base de datos llamada CRUD utilizada por los métodos de HTTP como **PUT**, **POST** y otros.

**6.**Question 6

REST, que significa Transferencia de estado representacional, se puede describir mejor como un tipo de:

1 / 1 point

**Estándar de servicio web**

**`Estilo de arquitectura para puntos de conexión`**

**Marco de la API web**

Correct

Correcto. REST es un estilo de arquitectura que proporciona estándares y descripciones para interfaces uniformes entre componentes en una arquitectura cliente-servidor.

**7.**Question 7

¿Cuáles de las siguientes son bases de datos relacionales compatibles con Django y que requieren configuraciones mínimas? Elija todas las opciones que correspondan.

1 / 1 point

- [x]  **PostgreSQL**

Correct

Correcto. PostgreSQL es ampliamente utilizado por los desarrolladores de Django y requiere de una configuración mínima en Django.

- [x]  **MariaDB**

Correct

Correcto. MariaDB es ampliamente utilizado por los desarrolladores de Django y requiere de una configuración mínima en Django.

- [x]  **MySQL**

Correct

Correcto. MySQL es ampliamente utilizado por los desarrolladores de Django y requiere de una configuración mínima en Django.

- [ ]  **MongoDB**

**8.**Question 8

¿Cuál es la asignación de ORM correcta que es compatible con Django Querysets para la siguiente consulta de SQL? Puede suponer que el nombre del modelo es **User** y la variable de objeto que creó es **user**.

**SELECT * FROM user WHERE id = 1**

1 / 1 point

**user = User.get(id=1)**

**user = User.objects.all(id=1)**

**user = User.objects.filter(id=1)**

**`user = User.objects.get(id=1)`**

Correct

Correcto. La función **get()**es el equivalente de usar la consulta **SELECT**  en SQL.

**9.**Question 9

Seleccione la implementación correcta de la función **render()** dentro de una vista para representar un diccionario de contexto en una plantilla agregada a **home.html**.

1 / 1 point

**`return render(request, ‘home.html', context)`**

**return render( ‘home.html’, request, context)**

**return render(request, context, 'home.html')**

**return render(context, request, 'home.html')**

Correct

Correcto. La función **render()** primero acepta el objeto de la solicitud seguido de la plantilla configurada dentro de la configuración de URL y se le pasa el diccionario.

**10.**Question 10

¿Qué líneas del siguiente bloque de código contienen errores? Elija las opciones que correspondan.

```markup
fetch('http://127.0.0.1:8000/api/menu-items') 
    .then(response => response.json()) 
    .then(data => 
{  console.log(data) }
)
```

1 / 1 point

- [ ]  **{console.log(data) }**
- [ ]  ** .then(data =>**
- [x]  **fetch(http://127.0.0.1:8000/api/menu-items)**

Correct

Correcto. El código correcto es **fetch(‘http://127.0.0.1:8000/api/menu-items’)** 
ya que debe pasar el punto de conexión de la URL como una cadena dentro de la función  **fetch()**.

- [x]  **.then(response => response.json)**

Correct

Correcto. El código correcto será  **.then(response => response.json())** as **json()** que es una función llamada en el objeto response.