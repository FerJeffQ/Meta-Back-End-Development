# Cuestionario del módulo: API de REST

**1.Pregunta 1**

¿Cuáles son las ventajas de utilizar pipenv? Seleccione todas las opciones que correspondan.

- [x]  **Crea un entorno virtual para su proyecto.**

```markup
Correcto. Pipenv crea automáticamente un entorno virtual e instala todas las dependencias en este.
```

- [ ]  **Hace que su proyecto sea más seguro.**
- [ ]  **Acelera la ejecución del proyecto.**
- [x]  **Gestiona las dependencias.**

```markup
Correcto. Usando pipenv puede gestionar las dependencias de su proyecto.
```

**2.Pregunta 2**

¿Cuál es el número de puerto por defecto utilizado por el servidor web de Django?

**`8000`**

**443**

**8001**

```markup
Correcto. 8000 es el número de puerto por defecto utilizado por el servidor web de Django cuando se aplica este comando de python manage.py runserver dentro de un directorio de un proyecto de Django.
```

**3.Pregunta 3**

¿Qué hace el siguiente comando?

```markup
**python manage.py startapp**
```

**Crea un proyecto de Django.**

**`Crea una nueva aplicación de Django.`**

**Instala Django.**

```markup
Correcto. Puede usar este comando dentro de un proyecto de Django para crear una nueva aplicación de Django siguiendo el nombre de la aplicación. Si el nombre de su aplicación es LittleLemonAPI, deberá aplicar este comando python manage.py startapp LittleLemonAPI.
```

**4.Pregunta 4**

Autenticación y autorización son lo mismo.

**Verdadero**

**`Falso`**

```markup
Correcto. La autenticación y la autorización son cosas diferentes, y desempeñan un papel muy importante en la seguridad de su proyecto. La autenticación comprueba si el usuario puede entrar en el sistema, y la autorización comprueba si el usuario autenticado tiene los privilegios adecuados para realizar una tarea.
```

**5.Pregunta 5**

¿Cuál de los siguientes códigos de estado de HTTP se utiliza para indicar errores del lado del cliente y del lado del servidor? Seleccione todas las opciones que correspondan.

- [ ]  **201 - Created**
- [x]  **404 Not Found**

```markup
Correcto. Este código se utiliza cuando alguien solicita un elemento inexistente.
```

- [x]  **503 - Service Unavailable**

```markup
Correcto. Este código se utiliza cuando el servidor está caído o no puede gestionar la solicitud debido a una sobrecarga.
```

- [x]  **403 – Forbidden**

```markup
Correcto. Este código se utiliza cuando las credenciales del cliente, como el nombre de usuario y la contraseña, o el token, no son válidos.
```

- [ ]  **301- Moved Permanently**

**6.Pregunta 6**

¿Cuáles son los encabezados **Accept** válidos para solicitar contenido XML? Seleccione todas las opciones que correspondan.

- [ ]  **application/xml-content**
- [x]  **text/xml**

```markup
Correcto. Se trata de un encabezado válido para solicitarle contenido XML al servidor.
```

- [ ]  **application/x-xml**
- [x]  **application/xml**
- [ ]  **code/xml**

**7.Pregunta 7**

¿Qué puede provocar el daño de los datos en un proyecto de API? Seleccione todas las opciones que correspondan.

- [ ]  **Falta de almacenamiento en caché**
- [x]  **Falta de autorización**

```markup
Correcto. La falta de una capa de autorización sólida puede hacer que cualquier usuario con un token de autenticación válido acceda a cualquier punto de conexión de la API y modifique los datos.
```

- [x]  **Falta de autenticación**

```markup
Correcto. Sin autenticación cualquiera puede ingresar y modificar los datos.
```

- [ ]  **Ausencia de limitación**
- [x]  **Falta de validación y saneamiento de datos**

```markup
Correcto. Los datos incorrectos o con el formato inadecuado pueden almacenarse en la base de datos sin una validación adecuada de los datos. La falta de saneamiento puede crear amenazas de seguridad que también pueden dañar los datos.
```

**8.Pregunta 8**

¿Cuáles de las siguientes afirmaciones son válidas para Insomnia? Seleccione todas las opciones que correspondan.

- [x]  **Es un cliente API de REST.**

```markup
Correcto. Puede utilizar Insomnia para realizar solicitudes de HTTP.
```

- [x]  **Insomnia puede enviar diferentes tipos de cargas.**

```markup
Correcto. Al hacer una llamada de API, puede enviar diferentes tipos de cargas como JSON o datos codificados en URL del formulario utilizando Insomnia.
```

- [ ]  **Insomnia tiene un cliente móvil.**
- [ ]  **Insomnia tiene una herramienta de línea de comandos**
- [x]  **Insomnia es multiplataforma.**

```markup
Correcto. Puede descargar Insomnia para múltiples sistemas operativos como Windows, macOS y Linux.
```

**9.Pregunta 9**

¿Cuál de las siguientes herramientas o clientes de API tiene versiones web y de escritorio?

** `Postman`**

**Curl**

** Insomnia**

```markup
Correcto. Postman viene con una aplicación de escritorio y ofrece una versión web que se puede utilizar en el navegador para realizar llamadas de API.
```

**10.Pregunta 10**

¿Para qué sirven las clases de representadores en DRF?

** Convierten los datos serializados para mostrarlos como HTML, XML y JSON.**

** Convierten la instancia del modelo en tipos de datos nativos de Python.**

**`Realizan un andamiaje rápido de un proyecto de API de CRUD.`**