# Cuestionario del módulo: Seguridad y pruebas

**1.**Question 1

¿Cuál de las siguientes clases de representador debería establecer como predeterminada para una API REST?

1 / 1 point

- [x]  **BrowsableAPIRenderer**

Correct

Correcto. Para aprovechar la API navegable de DRF, debe incluir **BrowsableAPIRenderer** en la lista de clases de representación predeterminada.

- [x]  **JSONRenderer**

Correct

Correcto. Una API REST genera la respuesta JSON. Por lo tanto, debe configurar **JSONRender** como la clase de representador predeterminada en la configuración del proyecto.

- [ ]  **TemplateHTMLRenderer**
- [ ]  **StaticHTMLRenderer**

**2.**Question 2

Complete la siguiente oración. Si usa el parámetro **many=True** en una clase **Serializer** , da como resultado _________________.

1 / 1 point

**`Serializando múltiples objetos en el conjunto de consultas.`**

**Aplicando múltiples reglas de validación.**

**Aplicando múltiples criterios de permiso.**

**Obteniendo múltiples objetos en el conjunto de consultas.**

Correct

Correcto. El parámetro **many=True** del constructor **Serializer** serializa todos los objetos obtenidos en el conjunto de consultas.

**3.**Question 3

¿Qué tipos de esquemas de autenticación están integrados en el marco REST de Django? Seleccione todas las opciones que correspondan.

1 / 1 point

- [x]  **TokenAuthentication**

Correct

Correcto. El módulo **rest_framework.authentication** tiene definida la clase **TokenAuthentication**.

- [x]  **Autenticación de sesión**

Correct

Correcto. El módulo **rest_framework.authentication** tiene definida la clase **SessionAuthentication**.

- [x]  **BasicAuthentication**

Correct

Correcto. El módulo **rest_framework.authentication** tiene definida la clase **BasicAuthentication**.

- [ ]  **JWTAuthentication**

**4.**Question 4

Sí o no. ¿Es compatible el marco REST de Django con JWT?

1 / 1 point

**Sí**

**`No`**

Correct

Correcto. Debe instalar **restframework_jwt** y el módulo **Djoser** para implementar JWT.

**5.**Question 5

Complete la siguiente oración. En una API de DRF, una respuesta no autenticada contiene el código de estado ________.

1 / 1 point

**501 Not Implemented**

**`401 Unauthorized`**

**404 Not Found**

**201 Created**

Correct

Correcto. La respuesta no autenticada tiene un código de estado 401.

**6.**Question 6

Complete la siguiente oración. La autenticación basada en token es adecuada para ___________.

1 / 1 point

**`Configuraciones cliente-servidor`**

**Clientes AJAX**

**Fines de prueba**

**Clientes no confiables**

Correct

Correcto. La autenticación de token se utiliza para la autenticación en un entorno cliente-servidor.

**7.**Question 7

¿Cuál de las siguientes es una herramienta de prueba de API? Seleccione todas las opciones que corresponden.

1 / 1 point

- [x]  **Insomnia**

Correct

Correcto. Insomnia es una herramienta GUI para probar puntos de conexión de API.

- [x]  **Curl**

Correct

Correcto. Curl es una herramienta de línea de comandos para probar puntos de conexión de API.

- [ ]  **Git**
- [x]  **Postman**

Correct

Correcto. Puede usar la aplicación Postman para probar los puntos de conexión de la API.

**8.**Question 8

Verdadero o falso. Para ejecutar las pruebas unitarias en una aplicación Django, debe instalar la biblioteca **unittest** con pip.

1 / 1 point

**Verdadero**

**`Falso`**

Correct

Correcto. El módulo **unittest** se incluye con la biblioteca estándar de Python. No necesita ser instalado.

**9.**Question 9

¿Cuál de las siguientes es una opción de comando para que el script manage.py ejecute pruebas unitarias?

1 / 1 point

**unittest**

**TestCase**

**`prueba`**

**TestRunner**

Correct

Correcto. Puede usar el comando **python manage.py test** para ejecutar pruebas unitarias.

**10.**Question 10

¿Cuáles de las siguientes opciones están disponibles cuando utiliza la biblioteca Djoser? Seleccione todas las opciones que correspondan.

1 / 1 point

- [x]  **/users/me/**

Correct

Correcto. Esta opción proporciona el nombre de usuario y la contraseña del usuario actualmente conectado.

- [x]  **/jwt/create/**

Correct

Correcto. Puede visitar esta URL para generar un token web JSON.

- [ ]  **api-token-auth/**
- [x]  **/token/login/**

Correct

Correcto. Cuando visita este punto de conexión, se genera el token de autenticación para un usuario determinado.