# Cuestionario del módulo: Modelos

## **1.**Pregunta 1

El comando ***sqlmigrate*** genera la consulta SQL que se ejecutará cuando finalice la migración.

- `R:` **Verdadero**
- **Falso**

```markup
Correcto.  **sqlmigrate** muestra el texto de la consulta SQL correspondiente que se va a ejecutar.
```

## **2.**Pregunta 2

¿Cuál de las siguientes frases sobre la clave principal es correcta? Seleccione todas las que correspondan.

- [x]  **El atributo de clave principal del modelo puede ser una cadena.**

```markup
Correcto. El tipo de datos del campo de clave principal puede ser **CharField** o TextField.
```

- [x]  **El atributo de clave principal del modelo debe ser único para cada instancia.**

```markup
Correcto. Para cada instancia del modelo, el valor de la clave principal debe ser único.
```

- [ ]  **El atributo de clave principal del modelo debe ser un número entero.**
- [x]  **El atributo de clave principal del modelo no debe ser nulo.**

```markup
Correcto. No se permite un valor nulo para la clave principal.
```

## **3.**Pregunta 3

Para utilizar MySQL con Django, ¿qué acciones deben tomarse?

- [x]  **Install mysqlclient**

```markup
Correcto. El controlador MySQL para Python debe estar instalado.
```

- [ ]  **Set 'USER': 'root'**
- [x]  **Set 'ENGINE': 'django.db.backends.mysql'**

```markup
Correcto. Esto permite que MySQL se utilice como *backend* para el proyecto actual.
```

- [ ]  **Set 'PORT': '8000'**

## **4.**Pregunta 4

¿Cuál de las siguientes afirmaciones sobre el tipo **ForeignKey (Clave foránea)**es correcta? Seleccione todas las que correspondan.

- [x]  **Un campo del tipo ForeignKey (Clave foránea)se utiliza para establecer una relación de uno a varios.**

```markup
Correcto. El atributo **ForeignKey (Clave foránea)** establece una relación de uno a varios entre dos modelos.
```

- [x]  **Un campo del tipo ForeignKey (Clave foránea) se utiliza para establecer una relación de varios a uno**

```markup
Correcto. Un campo del tipo **ForeignKey (Clave foránea)** se utiliza para establecer una relación de varios a uno.
```

- [ ]  **Se utiliza un campo del tipo ForeignKey (Clave foránea)para establecer una relación de varios a varios.**
- [ ]  **Se utiliza un campo del tipo ForeignKey (Clave foránea)para establecer una relación uno a uno.**

## **5.**Pregunta 5

¿Cuál de los siguientes tipos de campo integrados de un modelo almacena datos numéricos? Seleccione todas las que correspondan.

- [ ]  **CharField (Campo de caracteres)**
- [x]  **FloatField**

```markup
Correcto. Este campo almacena un número con una coma.
```

- [x]  **IntegerField**

```markup
Correcto. Este campo almacena un número entero.
```

- [ ]  **URLField**

## **6.**Pregunta 6

El formulario Django se representa de forma tabular con una etiqueta en la plantilla. Identifique la etiqueta correcta.

**{{ form.as_p }}**

**{{ form.as_div }}**

`R:` **{{ form.as_table }}**

**{{ form.as_ul }}**

```markup
Correcto. Esta etiqueta representa el formulario como una tabla HTML.
```

## **7.**Pregunta 7

¿Cuál de las siguientes expresiones extrae los datos en el formulario enviado por el usuario?

**form.is_valid**

`R:` **request.POST**

**request.GET**

**form.cleaned_data**

## **8.**Pregunta 8

¿Cuál de las siguientes afirmaciones sobre un usuario del personal es correcta? Seleccione todas las que corresponda.

- [ ]  **Un usuario de plantilla no puede modificar los permisos habilitados para un usuario.**
- [x]  **Un usuario del personal puede iniciar sesión en el sitio de administración**

```markup
Correcto. El usuario del personal tiene el privilegio de poder iniciar sesión en el sitio de administración.
```

- [x]  **Un usuario del personal puede crear un grupo**

```markup
Correcto. Un usuario de personal con privilegios puede crear un grupo.
```

- [ ]  **Un usuario de plantilla no puede crear un nuevo usuario**

## **9.**Pregunta 9

Verdadero o falso. A un superusuario se le asignan todos los permisos automáticamente para agregar, eliminar y cambiar los detalles de otros usuarios.

R: **Verdadero**

**Falso**

```markup
Correcto. A un superusuario se le asignan todos los permisos automáticamente para agregar, eliminar y cambiar los detalles de otros usuarios.
```

## **10.**Pregunta 10

¿Qué opción de comando del script ***manage.py*** se utiliza para crear un usuario administrador para el sitio *Django admin*?

**createuser**

`R:` **createsuperuser**

**runserver**

**shell**

```markup
Correcto. El comando **createsuperuser** crea un usuario con el nombre de usuario especificado.
```