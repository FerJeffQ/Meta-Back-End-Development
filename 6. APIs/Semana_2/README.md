# Cuestionario del módulo: Marco REST de Django

**1.Pregunta 1**

¿Cómo se acepta una llamada **GET**, **POST** y **PUT** a una vista basada en funciones utilizando un decorador de API?

**An API endpoint cannot accept multiple HTTP methods**

**`@api_view(['GET','POST','PUT'])`**

**@api_view('GET','POST','PUT')**

**api_view(['GET','POST','PUT'])**

```markup
Correcto. Una función de decorador de vista de API necesita una @ delante y puede pasar todos los nombres de métodos de HTTP necesarios como una lista dentro de esta.
```

**2.Pregunta 2**

¿Cuáles son las ventajas de utilizar un serializador? Marque todas las opciones que correspondan.

- [ ]  **Puede convertir automáticamente datos a JSON o XML.**
- [x]  **Puede validar los datos.**

```markup
Correcto. Antes de guardar los datos en la base de datos, un serializador puede validarlos siguiendo las reglas de validación especificadas en el archivo serializers.py para asegurarse de que los datos sean correctos y suficientes.
```

- [x]  **Puede guardar los datos en una base de datos.**

```markup
Correcto. Los serializadores pueden guardar los datos en la base de datos con la ayuda de modelos.
```

- [x]  **Puede convertir las entradas del usuario y asignarlas a los modelos.**

```markup
Correcto. Esta es una funcionalidad incorporada de los serializadores en DRF, y se llama deserialización.
```

- [x]  **Puede convertir instancias del modelo en tipos de datos nativos de Python.**

```markup
Correcto. Puede convertir rápidamente instancias del modelo en tipos de datos nativos de Python utilizando serializadores. Estos tipos de datos nativos de Python pueden mostrarse posteriormente como JSON y XML utilizando representadores.
```

- [ ]  **Ayuda a autenticar las llamadas de API.**

**3.Pregunta 3**

¿Cuáles de las siguientes son clases de serializadores válidas en DRF? Marque todas las opciones que correspondan.

- [ ]  **RelationshipSerializer**
- [ ]  **PrimaryKeySerializer**
- [x]  **HyperLinkModelSerializer**

```markup
Correcto. Puede utilizar esta clase de serializador para crear rápidamente relaciones con hipervínculos entre modelos relacionados y mostrarlas como hipervínculos.
```

- [x]  **ModelSerializer**

```markup
Correcto. Los serializadores de modelos se utilizan para serializar rápidamente los modelos y sus relaciones.
```

- [x]  **Serializer**

```markup
Correcto. Esta es la clase de serializadores base en DRF que se puede utilizar para serializar instancias del modelo y objetos independientes.
```

**4.Pregunta 4**

Puede acceder al atributo de datos de una clase de serializador en cualquier momento.

**Verdadero**

**`Falso`**

```markup
Correcto. Solo se puede acceder al atributo de datos de una clase de serializador después de que se haya realizado la validación en el serializador.
```

**5.**Pregunta 5

¿Cuál de los siguientes representadores viene con DRF por defecto? Marque todas las opciones que correspondan.

- [ ]  **YAML Renderer**
- [x]  **JSON Renderer**

```markup
Correcto. El representador JSON viene como un paquete integrado en el marco REST de Django.
```

- [x]  **HTML Renderer**

```markup
Correcto. DRF incluye varios representadores HTML para ayudarlo a representar el contenido HTML estático y dinámico.
```

- [ ]  **XML Renderer**

**6.Pregunta 6**

¿Cuál de las siguientes afirmaciones es verdadera sobre el DRF?

**El DRF no funciona con diferentes motores de bases de datos.**

**El DRF es un marco independiente.**

**Aprender DRF es difícil.**

**`El DRF está diseñado para el desarrollo de API.`**

```markup
Correcto. Aunque puede utilizar el DRF para crear contenido HTML estándar, está específicamente diseñado para que los desarrolladores creen proyectos de API con gran rapidez. Viene con todas las clases y módulos necesarios como ViewSets, vistas genéricas, serializadores, clases de autenticación y permisos y mucho más que los desarrolladores de API requieren con frecuencia en sus proyectos. El DRF también tiene una documentación excelente y una enorme comunidad de desarrolladores, por lo que obtener ayuda o soporte es más fácil.
```

**7.**Pregunta 7

¿Cuáles de los siguientes paneles están disponibles en la barra de herramientas de depuración de DDT o Django? Marque todas las opciones que correspondan.

- [x]  **SQL**

```markup
Correcto. En este panel se muestran todas las consultas de SQL ejecutadas para la solicitud actual.
```

- [ ]  **Red**
- [x]  **Perfil**

```markup
Correcto. En este panel se muestra toda la pila de llamadas de la solicitud actual.
```

- [ ]  **Limitación**
- [x]  **Encabezados**

```markup
Correcto. En el panel de encabezados figuran todos los encabezados de la solicitud y la respuesta actuales.
```

**8.Pregunta 8**

Para serializar un queryset que devuelve más de un elemento, ¿cuál de los siguientes argumentos es necesario para la clase del serializador?

**`many=True`**

**related=True**

**multiple_items=True**

```markup
Correcto. Debe pasar many=True a la clase del serializador cuando se trata de un queryset que devuelve más de un elemento.
```

**9.Pregunta 9**

¿Cuál de las siguientes afirmaciones es verdadera sobre el uso de representadores? Marque todas las opciones que correspondan.

- [x]  **Los representadores pueden convertir automáticamente el resultado.**

```markup
Correcto. Cuando carga estas clases de representadores en el archivo settings.py, funcionarán automáticamente en función del encabezado Accept que haya enviado un cliente de la API. No es necesario escribir código adicional para ello.
```

- [x]  **Los representadores necesitan un encabezado Accept para funcionar correctamente.**

```markup
Correcto. Sobre la base de estos encabezados Accept, DRF invoca al representador correspondiente para mostrar el resultado correctamente.
```

- [x]  **Si no hay ningún encabezado Accept, DRF utiliza el representador JSON por defecto.**

```markup
Correcto. Si no hay ningún encabezado accept, DRF muestra el resultado en JSON utilizando la clase JSONRenderer incorporada.
```

- [ ]  **No se pueden utilizar varios representadores en un proyecto.**
- [ ]  **No se puede forzar el uso de un único representador.**

**10.Pregunta 10**

¿Cómo se muestran los campos del modelo relacionados como hipervínculos? Marque todas las opciones que correspondan.

- [ ]  **Un ModelSerializer puede hacerlo automáticamente.**
- [ ]  **Al usar RelationshipSerializer**
- [x]  **Al usar HyperlinkedRelatedField**

```markup
Correcto. Un campo del serializador HyperlinkedRelatedField puede mostrar modelos relacionados como hipervínculos.
```

- [x]  **Al usar HyperlinkedModelSerializer**

```markup
Correcto. Existe una clase de serializador especial llamada HyperlinkedModelSerializer que también puede mostrar los modelos relacionados como hipervínculos.
```