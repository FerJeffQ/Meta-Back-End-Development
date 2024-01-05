# Cuestionario de Modulo vistas

## **1.** Pregunta 1

Para agregar un patrón de URL con *regex*, utilice la función re_path()<1} en lugar de la función **path()**.

`R:` **Verdadero**

- **Falso**

```markup
Correcto

Correcto. Si el convertidor de ruta necesita un patrón de coincidencia complejo, debe utilizar la función **re_path()**. Aquí, "re" significa *regex.*
```

## **2.** Pregunta 2

¿Cuál de las siguientes oraciones sobre la función {1>*path()* (ruta)<1} es correcta? Seleccione todas las que correspondan.

- [x]  **La función path() (ruta) se utiliza para definir un patrón de URL.**

```markup
Correcto

Correcto. Agrega una URL asignada a una vista a la lista de patrones de URL.
```

- [ ]  **La path() (ruta) devuelve la ruta de la aplicación Django.**
- [x]  **La función path() (ruta) se define en el módulo django.urls.**

```markup
Correcto

Correcto. Las funciones *path* (ruta) e *include* (incluir), utilizadas para crear la lista de patrones de URL, se definen en el módulo **django.urls**
```

- [ ]  **El parámetro de cadena de URL de la función path() (ruta) captura los parámetros de consulta de la URL.**

## **3.** Pregunta 3

Complete la oración. Los convertidores de ruta capturan _____ de la URL.

**URL parameters**

**Parámetros del cuerpo**

**Parámetros de consulta**

`R:` **Parámetros de ruta**

```markup
Correcto

Correct. Los convertidores del formato **<type:variable>** mencionados en el argumento de cadena URL a la función **path() (ruta)** contienen los parámetros incluidos en la URL.
```

## **4.** Pregunta 4

El atributo **request.user** contiene la información del usuario actual.

`R:` **Verdadero**

**Falso**

```markup
Correcto

Correcto. La función de vista puede acceder a la información sobre el usuario actual, como el nombre de usuario y si está autenticado, con el atributo **request.user**.
```

## **5.** Pregunta 5

Complete la siguiente declaración. El código de estado HTTP que comienza con 5 significa que:

**Existe un error del lado del cliente.**

`R:` **El servidor ha encontrado un error.**

**La acción se ha completado con éxito.**

**Se recibió la solicitud y está en proceso.**

```markup
Correcto

Correcto. Para un error del lado del servidor, el código de estado comienza con 5.
```

## **6.**Pregunta 6

¿Cuáles son las características importantes de una vista basada en clases? Seleccione todas las que corresponden.

- [x]  **El método as_view() asigna una dirección URL a una vista basada en clases.**

```markup
Correcto

Correcto. Este método conecta una clase de vista con un patrón de cadena de URL.
```

- [x]  **Las vistas basadas en clases son reutilizables.**

```markup
Correcto

Correcto. El principio de Python de herencias múltiples permite que las vistas basadas en clases de Django sean reutilizables.
```

- [x]  **Una vista basada en clases subclasifica la clase base django.view.View.**

```markup
Correcto

Correcto. Todas las clases de vista heredan la clase **django.view.View**
```

- [x]  **Una vista basada en clases implementa diferentes métodos para cada método HTTP.**

```markup
Correcto

Correcto. La clase de vista definida por el usuario anula los métodos **get() (obtener)** y **post() (publicar)** para definir la lógica de procesamiento de los métodos de solicitud correspondientes..
```

## **7.**Pregunta 7

La respuesta **Http404** es una alternativa conveniente para una respuesta **HttpResponse**.

`R:` **Verdadero**

**Falso**

```markup
Correcto

Correcto. Es una subclase de **HttpResponse** para tener una página de error 404 consistente en diferentes páginas de la aplicación
```

## **8.**Pregunta 8

El nombre de la URL es _________. Seleccione las que correspondan.

- [x]  **an optional parameter passed inside the path() function.**

```markup
Correcto

Correcto. Un parámetro opcional pasado dentro de la función **path() (ruta).**
```

- [x]  **pasado como el parámetro name en la función path()(ruta).**

```markup
Correcto

Correcto. La **path()(ruta**) cuenta con un parámetro de **nombre** opcional además de la cadena de patrón de URL y la función de vista.
```

- [x]  **utilizada para definir el espacio de nombre URL.**

```markup
Correcto

Correcto. Puede obtener la URL con una sintaxis como **reverse(namespace:view)**.
```

- [x]  **utilizada por la función reverse()(inversa) para obtener la URL asignada con la función de vista.**

```markup
Correcto

Correcto. La función **reverse()(inversa)** se define en el módulo **django.urls** obtiene la URL asignada con la función de vista.
```

## **9.**Pregunta 9

¿Se pueden definir vistas en el archivo ***views.py*** de la carpeta de proyectos?

`R:` **Sí.**

**No**

```markup
Correcto

Correcto. Puede definir vistas en el archivo **views.py** de la carpeta proyectos. Se usa cuando desea anular las vistas de error predeterminadas.
```

## **10.**Pregunta 10

Complete la siguiente oración. Para anular la vista de error predeterminada, __________. Seleccione las que correspondan.

- [ ]  **No es necesario anular las vistas de error predeterminadas.**
- [x]  **especifique el controlador adecuado en URLConf del proyecto.**

```markup
Correcto

Correcto. Existen controladores predefinidos para personalizar vistas de error, como  **Handler404 for page_not_found()**.
```

- [ ]  **Debe definir la vista de controlador de errores personalizada en el archivo views.py de la aplicación.**
- [x]  **Defina la vista personalizada en la carpeta del proyecto**

```markup
Correcto

Correcto. El controlador se refiere a la función de vista definida en el archivo **view.py** de la carpeta del proyecto.
```