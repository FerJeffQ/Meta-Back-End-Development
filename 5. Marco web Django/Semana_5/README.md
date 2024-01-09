# Cuestionario final con calificacion: Marco web Django

## **1.**Pregunta 1

Al utilizar la etiqueta **include** (incluir) no existe ningún estado compartido entre las plantillas incluidas.

**`Verdadero`**

**Falso**

## **2.**Pregunta 2

¿Cuáles de las siguientes etiquetas en el lenguaje de plantilla Django son relevantes para la herencia de plantillas?

- [ ]  **csrf_token**
- [x]  **include  (incluir)**

```markup
¡Correcto! La etiqueta *include* (incluir) se utiliza para representar subplantillas junto con el HTML.
```

- [x]  **extends (extender)**

```markup
¡Correcto! La etiqueta *extends* (extender) le permite reemplazar bloques o contenido de una plantilla principal.
```

- [ ]  **static**

## **3.**Pregunta 3

Si ejecuta el código siguiente, ¿cuál será el resultado generado para la vista especificada en la página web?

```markup
def home(request): 
...
return HttpResponse("Hello") 
return HttpResponse("World")
```

**`Hello (Hola)`**

**Hello World (Hola mundo)**

**World (mundo)**

```markup
¡Correcto! Django usará la primera sentencia *return* (devolver) y saldrá de la función.
```

## **4.**Pregunta 4

¿Cuáles de las siguientes son las ventajas de usar vistas basadas en funciones?

- [ ]  **Reutilización del código**
- [ ]  **El código se puede ampliar para incluir más funcionalidades.**
- [x]  **Flujo de código explícito**

```markup
¡Correcto! Las vistas basadas en funciones proporcionan un flujo explícito, lo que significa que la autenticación en dos pasos se omite automáticamente.
```

- [x]  **Uso de decoradores**

```markup
¡Correcto! Los decoradores '@' son tipos de funciones auxiliares y se pueden utilizar para ampliar la funcionalidad de las vistas basadas en funciones.
```

## **5.**Pregunta 5

¿Cuál de los siguientes NO es un comando que se puede ejecutar en la línea de comandos mediante el *script*  **manage.py**?

**shell**

**runserver**

**`settings`**

**showmigrations**

```markup
¡Correcto! Si bien se puede acceder a la configuración de Django desde el archivo **settings.py,** no existe tal comando declarado para la configuración de palabras clave dentro del *script* de **manage.py**.
```

## **6.**Pregunta 6

Complete la siguiente oración: Jinja2 es un tipo de ______

**funcionalidad para habilitar la herencia de plantillas.**

**`Motor de plantilla.`**

**Etiqueta de seguridad agregada dentro de las plantillas.**

**Un protocolo alternativo para la comunicación web.**

```markup
¡Correcto! Jinja2 es un motor de plantillas popular utilizado en Python y se puede utilizar para ampliar las funcionalidades del lenguaje de plantillas Django mientras se usa Django.
```

## **7.**Pregunta 7

¿Django usa el lenguaje de plantillas Django para separar la lógica para qué dos capas? Seleccione todas las que crea correctas.

- [ ]  **boolean**
- [x]  **slug**

```markup
¡Correcto! *Slug* coincide con cualquier cadena de *slug* que consista en letras o números ASCII, más los caracteres de guión y subrayado.
```

- [x]  **str**

```markup
¡Correcto! Str coincide con cualquier cadena no vacía, sin incluir al separador de ruta, , '/'. Este es el valor predeterminado si no se incluye un convertidor en la expresión.
```

- [x]  **path**

```markup
¡Correcto! La ruta coincide con cualquier cadena que no esté vacía, incluido el separador de ruta, '/'.
```

- [ ]  **float**

## **8.**Pregunta 8

Un usuario de Personal no puede acceder a la interfaz de administración, pero está autorizado de forma predeterminada a cambiar los permisos para crear, leer, actualizar y eliminar.

**Verdadero**

**`Falso`**

```markup
¡Correcto! El usuario del personal tiene acceso a la interfaz de administración, pero no puede modificar los permisos de forma predeterminada.
```

## **9.**Pregunta 9

Complete la siguiente oración. Las variables se pasan de la vista a la plantilla pasándolas dentro de la función *render()* (renderizar) en forma de objetos _______.

**dynamic**

**tuple**

**`diccionario`**

**list**

```markup
¡Correcto! Los objetos diccionario en Python son similares a los objetos JSON que tienen una estructura de par clave-valor y se usan comúnmente en aplicaciones web para pasar datos.
```

## **10.**Pregunta 10

Con respecto a la experiencia del usuario al crear un sitio web, la información del menú debe estar presente en todas las páginas.

¿Cuáles son algunas de las ventajas de colocar ese menú dentro de la sección de encabezado dentro de una plantilla?

- [x]  **Buena interfaz de usuario**

```markup
¡Correcto! Una barra de menú con un buen estilo dentro de la plantilla de cabecera garantizará una mejor consistencia y presentación para el usuario final.
```

- [x]  **Consistencia**

```markup
¡Correcto! La consistencia de la barra de menús en todas las páginas hace que sea fácil de encontrar y acceder
```

- [ ]  **Gestión eficiente de la memoria**
- [x]  **Navegación sencilla**

```markup
¡Correcto! La barra de menú en la cabecera es accesible en todas las páginas y proporciona una navegación sencilla.
```

- [ ]  **Hace que la página web sea más segura**