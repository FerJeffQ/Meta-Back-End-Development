# Cuestionario del módulo: Funcionalidad del proyecto

**1.**Question 1

¿Cuál de las siguientes sintaxis es correcta para revertir las migraciones aplicadas? Nota **00X** representa el número de secuencia de comandos de migración.

1 / 1 point

**python makemigrations 00X**

**python makemigrations myapp 00X**

**`python migrate myapp 00X`**

**python migrate 00X**

Correct

Correcto. Puede revertir los cambios usando el comando **migrate** mencionando el nombre de la aplicación y el script de migración.

**2.**Question 2

En el archivo **settings.py** , ¿qué hace la opción del comando **init_**en la configuración de BASES DE DATOS?

1 / 1 point

**Esta opción inicializa la conexión a la base de datos.**

**`Este es el comando inicial para enviar al servidor al momento de la conexión.`**

**Esta opción inicializa la base de datos.**

**Inicia la comunicación entre el servidor Django y el servidor de la base de datos.**

Correct

Correcto. Los comandos del parámetro **init_command** se ejecutan cuando se establece la conexión.

**3.**Question 3

¿Cuáles de las siguientes bases de datos son compatibles oficialmente con Django? Seleccione todas las opciones que correspondan.

1 / 1 point

- [ ]  **MongoDB**
- [x]  **MySQL**

Correct

Correcto. Django tiene un módulo backend incorporado para MySQL.

- [x]  **Oracle**

Correct

Correcto. Django tiene un módulo backend incorporado para Oracle.

- [x]  **SQLite**

Correct

Correcto. Django tiene un módulo backend incorporado para SQLite.

**4.**Question 4

¿Cuál de las siguientes afirmaciones sobre un modelo en Django es correcta? Seleccione todas las opciones que correspondan.

1 / 1 point

- [x]  **Un modelo usa opcionalmente Meta como una clase interna.**

Correct

Correcto. La clase **Meta** define metadatos adicionales sobre el modelo.

- [x]  **Un modelo es la fuente única y definitiva de información sobre sus datos en un proyecto de Django.**

Correct

Correcto. El modelo es una definición de la estructura de los datos a procesar.

- [x]  **Un modelo es una clase de Python que amplía la clase Model en el módulo django.db.models.**

Correct

Correcto. Un modelo subclasifica la clase **Model** en el módulo **django.db.models**.

- [ ]  **Un modelo define los atributos de clase del tipo de datos int o str.**

**5.**Question 5

¿Cuáles de las siguientes afirmaciones son verdaderas con respecto a las diferencias entre una API de Django y una aplicación web de Django? Seleccione todas las opciones que correspondan.

1 / 1 point

- [ ]  **El marco de Django tiene soporte incorporado para crear una aplicación web y API.**
- [x]  **Una API es un servicio que utiliza cualquier cliente HTTP, mientras que una aplicación web de Django interactúa principalmente con un cliente de navegador.**

Correct

Correcto. Cualquier cliente HTTP puede interactuar con el servidor API, mientras que una aplicación web Django interactúa principalmente con un navegador.

- [ ]  **La API necesita la autenticación del usuario, mientras que la aplicación web Django no tiene la provisión de autenticación.**
- [x]  **Una API devuelve una respuesta JSON o XML al cliente, mientras que una aplicación web de Django suele devolver una respuesta HTML.**

Correct

Correcto. Una API generalmente devuelve una respuesta JSON, mientras que una aplicación web Django devuelve una respuesta HTML.

**6.**Question 6

¿Qué es la limitación en una API de Django?

1 / 1 point

**`La limitación es el proceso de limitar la cantidad de solicitudes de API que puede realizar un usuario.`**

**La limitación es un mecanismo para acelerar la respuesta de la API.**

**La limitación es un método para probar el rendimiento de la API.**

**La limitación es un mecanismo para evitar el acceso no autenticado.**

Correct

Correcto. La limitación restringe el número de solicitudes de un usuario.

**7.**Question 7

¿Por qué no se recomienda la autenticación basada en contraseña en el marco REST de Django? Seleccione todas las opciones que correspondan.

1 / 1 point

- [x]  **No es seguro.**

Correct

Correcto. Enviar la información del usuario en la solicitud es un peligro para la seguridad.

- [x]  **Es tedioso y requiere mucho tiempo.**

Correct

Correcto. Ingresar un nombre de usuario y contraseña para cada solicitud es tedioso.

- [ ]  **Está en desuso.**
- [ ]  **No es compatible con el protocolo HTTPS**

**8.**Question 8

¿Qué es la deserialización en el marco REST de Django?

1 / 1 point

**Guarda los datos recibidos de un cliente en el modelo.**

**Convierte los datos recibidos del cliente en un objeto dict de python.**

**`Reconstruye la instancia del modelo a partir de los datos serializados.`**

**Convierte la respuesta JSON en una respuesta HTML.**

Correct

Correcto. La deserialización es el proceso de analizar los datos serializados en una instancia de modelo para guardar.

**9.**Question 9

¿Cuáles de los siguientes son los decoradores de políticas de vista en el marco REST de Django? Seleccione todas las opciones que correspondan.

1 / 1 point

- [x]  **@permission_classes()**

Correct

Correcto. Utiliza este decorador con una vista basada en funciones para hacer cumplir los permisos.

- [x]  **@authentication_classes()**

Correct

Correcto. Este decorador establece la clase de autenticación que se utilizará para una vista basada en funciones.

- [ ]  **@serializer_classes()**
- [ ]  **@api_view()**

**10.**Question 10

¿Cuáles de las siguientes son las clases de vista genéricas en el marco REST de Django?

1 / 1 point

- [ ]  **DetailView**
- [x]  **ListCreateAPIView**

Correct

Correcto. Esta vista maneja las solicitudes GET y POST.

- [x]  **RetrieveUpdateAPIView**

Correct

Correcto. Esta vista maneja las solicitudes GET y PUT.

- [ ]  **TemplateView**

**11.**Question 11

¿Cuáles son las ventajas de utilizar ViewSets en el marco REST de Django? Seleccione todas las opciones que correspondan.

1 / 1 point

- [ ]  **Hace cumplir automáticamente la autenticación.**
- [ ]  **Automáticamente serializa el conjunto de consultas.**
- [x]  **Puede concentrarse en modelar el estado y las interacciones de la API, dejando que la construcción de URL se maneje automáticamente.**

Correct

Correcto. Los ViewSets se encargan internamente de crear rutas URL.

- [x]  **Una sola clase maneja automáticamente todas las operaciones CRUD.**

Correct

Correcto. ViewSets hace que la lógica de vista sea compacta y eficiente.