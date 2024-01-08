# Cuestionario del módulo: Plantillas

## **1.**Pregunta 1

¿Cuál de las siguientes frases sobre plantillas es verdadera? Seleccione todas las que crea correctas

- [x]  **Una plantilla es una página web que tiene bloques de sintaxis de lenguaje de plantilla dentro del *script* HTML.**

```markup
¡Correcto! Los bloques de lenguaje de plantilla Django representan contenido dinámico en la página web
```

- [x]  **Una plantilla extrae los datos de un modelo y genera una página dinámica.**
- [x]  **Una plantilla ayuda a incluir lógica de procesamiento condicional en una página web.**

```markup
¡Correcto! La etiqueta **{% if %}** } permite colocar una lógica condicional en el *script* HTML.
```

- [ ]  **Una plantilla es la capa de datos de la aplicación.**

## **2.**Pregunta 2

La función de vista carga una plantilla y completa los datos de contexto que contiene.

**`True`**

**Falso**

```markup
¡Correcto! La función de vista carga la plantilla llamando a la función  **render()** (renderizar)
```

## **3.**Pregunta 3

¿Cuál de las siguientes etiquetas se usa para implementar la herencia de plantillas?

- [x]  **{% extends %}**

```markup
¡Correct! La etiqueta **{% extends %}** utiliza la plantilla con nombre como plantilla base.
```

- [ ]  **{% include %}**
- [ ]  **{% block %}**
- [ ]  **{% endfor %}**

## **4.**Pregunta 4

Verdadero o falso. Para implementar la herencia de plantillas, la plantilla principal debe tener el nombre  **base.html**.

**Verdadero**

**`Falso`**

```markup
¡Correcto! La plantilla principal puede tener cualquier nombre y debe usarse en la etiqueta **{% extends %}**de la plantilla secundaria.
```

## **5.**Pregunta 5

¿En qué módulo se define la función **render()** (renderizar)?

**django.urls**

**`django.shortcuts`**

**django.db**

**django.contrib**

```markup
¡Correcto! La función **render()** se define en el módulo **django.shortcuts**.
```

## **6.**Pregunta 6

¿Cuál de los siguientes filtros de plantilla devuelve una **representación de mayúsculas y minúsculas** de una cadena?

**Sugerencia:** **titlecase** hace que las palabras comiencen con un carácter en mayúsculas y los caracteres restantes en minúsculas.

**upper**

**lower**

**`title`**

**length**

```markup
¡Correcto! La etiqueta *title* (título) devuelve la cadena *titlecased*.
```

## **7.**Pregunta 7

Poner un bucle dentro de otro se denomina anidamiento de bucles. ¿Se pueden usar bucles anidados en una plantilla?

**`Sí`**

**No**

```markup
¡Correcto! Los bucles anidados *for* se pueden usar en una plantilla.
```

## **8.**Pregunta 8

La función de vista pasa un ______ como datos de contexto a una plantilla.

**Lista de Python**

**Cadena de Python**

**`Diccionario de Python`**

**Tupla de Python**

```markup
¡Correcto! El contexto pasado a la plantilla debe ser un objeto **diccionario.**
```

## **9.**Pregunta 9

¿Cuáles son las ventajas de una vista basada en clases? Seleccione todas las que crea posibles

- [x]  **Reutilización del código**

```markup
¡Correcto! Las vistas basadas en clases implementan el principio DRY.
```

- [x]  **Código extensible**

```markup
Con el principio de herencia de clases, se puede ampliar la funcionalidad de vista basada en clases
```

- [ ]  **Las vistas basadas en clases son fáciles de implementar**
- [ ]  **Flujo de código implícito**

## **10.**Pregunta 10

Supongamos que una aplicación de Django denominada  **myapp** tiene el modelo Empleado. ¿Cuáles de las siguientes instrucciones sobre la clase genérica **ListView** son correctas?

- [x]  **Una lista ListView genérica debe denominarse EmployeeList**

```markup
¡Correcto! El nombre de clase se compone del nombre del modelo anexado por el nombre de vista genérico.
```

- [ ]  **Una clase ListView genérica debe establecer el atributo de modelo en myapp_Employee**
- [x]  **Una clase ListView genérica enumera todas las filas de la tabla Empleado**

```markup
¡Correcto! The **ListView**se utiliza para representar la lista de todos los registros de una tabla
```

- [x]  **Una clase ListView genérica necesita una plantilla denominada *EmployeeList.html***

```markup
¡Correcto! La plantilla con el nombre <name-of-model>Lista.html debe estar disponible en la carpeta de plantillas.
```