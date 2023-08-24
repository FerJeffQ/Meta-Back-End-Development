# INTRODUCCION A HTTP

Protocolo respuesta a solicitudes (Clientes - Servidores)

<img src="file:///C:/Users/ferje/Downloads/Coursera/Meta-Back-End-Development/Introduction%20to%20Back-End%20Development/Images/1.http.png" title="" alt="1.http" style="zoom:67%;">

Request:

<img src="file:///C:/Users/ferje/Downloads/Coursera/Meta-Back-End-Development/Introduction%20to%20Back-End%20Development/Images/2.http2.png" title="" alt="2.http2" style="zoom:67%;">

Response:

<img src="file:///C:/Users/ferje/Downloads/Coursera/Meta-Back-End-Development/Introduction%20to%20Back-End%20Development/Images/3.http3.png" title="" alt="3.http3" style="zoom:67%;">

## Ejemplos de HTTP

Toda solicitud HTTP comienza con la linea de solicitud

Consiste en un metodo HTTP, el resurso solicitado y la version del protocolo HTTP

```
GET/home.html HTTP/1.1
```

En este ejemplo $GET$ es el metodo HTTP, $/home.html$ es el recursosolicitado y $HTTP 1.1$ es el protocolo utilizado

## Metodos HTTP

Indican la accion que el cliente desea realizar sobre el recurso del servidor web.

| Metodo HTTP | Descripcion                                           |
| ----------- | ----------------------------------------------------- |
| GET         | El cliente solicita un recurso en el servidor web     |
| POST        | El ciente envia datos a un recurso en el servidor web |
| PUT         | El ciente sustituye un recurso en el servidor web     |
| DELETE      | El cliente elimina un recurso del servidor web        |

## Encabezados de solicitud

```
Host: example.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: */*
Accept-Language: en
Content-type: text/json
```



* El encabezado **Host** especifica el host del servidor e indica desde dónde se solicita el recurso.

* El encabezado **User-Agent** informa al servidor web de la aplicación que realiza la solicitud. Suele incluir el sistema operativo (Windows, Mac, Linux), la versión y el proveedor de la aplicación.

* El encabezado **Accept** informa al servidor web qué tipo de contenido aceptará el cliente como respuesta.

* El encabezado **Accept-Language** indica el idioma y, opcionalmente, la configuración regional que prefiere el cliente.

* El encabezado **Content-type** indica el tipo de contenido que se transmite en el cuerpo de la solicitud.
  
  
  
  

## Cuerpo de la solicitud HTTP

Puede incluir opcionalmente un cuerpo de solicitud

```
POST /users HTTP/1.1
Host: example.com

{
 "key1":"value1",
 "key2":"value2",
 "array1":["value3","value4"]
}
```

## Respuestas HTTP

Cueando el servidor web termine de procesar la solicitud HTTP, devolvera una respuesta HTTP.

```
HTTP/1.1 200 OK
```

### Codigos de estado HTTP

- 1XX Informational

| Código de estado | Frase de motivo           | Descripción                                                                                        |
| ---------------- | ------------------------- | -------------------------------------------------------------------------------------------------- |
| 100              | Continue                  | El servidor recibió los encabezados de solicitud y debe seguir enviando el cuerpo de la solicitud. |
| 101              | Protocolos de conmutación | El cliente ha solicitado al servidor que cambie de protocolo y el servidor ha accedido a hacerlo.  |

- 2XX Successful

| Código de estado | Frase de motivo | Descripción                                                                                           |
| ---------------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| 200              | OK              | Respuesta estándar devuelta por el servidor para indicar que ha procesado correctamente la solicitud. |
| 201              | Created         | El servidor ha procesado correctamente la solicitud y se ha creado un recurso.                        |
| 202              | Accepted        | El servidor aceptó la solicitud de procesamiento, pero el procesamiento aún no se ha realizado.       |
| 204              | No Content      | El servidor procesó correctamente la solicitud, pero no devuelve ningún contenido.                    |

- 3XX Redirection

| Código de estado | Frase de motivo   | Descripción                                                                  |
| ---------------- | ----------------- | ---------------------------------------------------------------------------- |
| 301              | Moved Permanently | Esta solicitud y todas las futuras deberán enviarse a la ubicación devuelta. |
| 302              | Found             | Esta solicitud debe enviarse a la ubicación devuelta.                        |

- 4XX Client Error

| Código de estado | Frase de motivo    | Descripción                                                                                                                                                                                                                                               |
| ---------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400              | Bad request        | El servidor no puede procesar la solicitud debido a un error del cliente, por ejemplo, una solicitud no válida o datos transmitidos demasiado grandes.                                                                                                    |
| 401              | Unauthorized       | El cliente que realiza la solicitud no está autorizado y debe autenticarse.                                                                                                                                                                               |
| 403              | Forbidden          | La solicitud era válida, pero el servidor se niega a procesarla. Normalmente se devuelve debido a que el cliente no tiene permisos suficientes para el sitio web, por ejemplo, solicita una acción de administrador, pero el usuario no es administrador. |
| 404              | Not found          | El servidor no encontró el recurso solicitado.                                                                                                                                                                                                            |
| 405              | Method Not Allowed | El servidor web no admite el método HTTP utilizado.                                                                                                                                                                                                       |

- 5XX Server Error

| Código de estado | Frase de motivo       | Descripción                                                                                                                        |
| ---------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 500              | Internal Server Error | Un código genérico de estado de error que se crea cuando se produce un error o una condición inesperados al procesar la solicitud. |
| 502              | Bad Gateway           | El servidor web ha recibido una respuesta no válida del servidor de aplicaciones.                                                  |
| 503              | Service unavaible     | El servidor web no puede procesar la solicitud.                                                                                    |

## Encabezados de respuesta HTTP

Depues de la linea de estado

```
Date: Fri, 11 Feb 2022 15:00:00 GMT+2
Server: Apache/2.2.14 (Linux)
Content-Length: 84
Content-Type: text/html
```

* El encabezado **Date** especifica la fecha y hora en que se generó la respuesta HTTP.

* El encabezado **Server** describe el software del servidor web utilizado para generar la respuesta.

* El encabezado **Content-Length** describe la longitud de la respuesta.

* El encabezado **Content-Type** describe el tipo de medio del recurso devuelto (por ejemplo, documento HTML, imagen, video).

# HTML, CSS Y JAVASCRIPT

- html: el cuerpo

- CSS: el estilo

- Javascript: El la Funcionalidad

<img src="file:///C:/Users/ferje/Downloads/Coursera/Meta-Back-End-Development/Introduction%20to%20Back-End%20Development/Images/4.html_css_java.png" title="" alt="4.html_css_java" style="zoom:50%;">

## Sitio Web VS Aplicacion Web

El sitio web muestra informacion y la aplicacion web tiene funcionalidad.

# API

Services Application Interface

<img src="file:///C:/Users/ferje/Downloads/Coursera/Meta-Back-End-Development/Introduction%20to%20Back-End%20Development/Images/5.api.png" title="" alt="5.api" style="zoom:67%;">

Mas utilizado como programador web:

<img src="file:///C:/Users/ferje/Downloads/Coursera/Meta-Back-End-Development/Introduction%20to%20Back-End%20Development/Images/6.apiweb.png" title="" alt="6.apiweb" style="zoom:67%;">


