# Cuestionario del módulo: Entornos de producción

**1.**Question 1

¿Se puede dividir una base de datos en varios fragmentos y luego almacenarlos en varios servidores de bases de datos?

1 / 1 point

- [ ]  **No, esto no es posible.**
- [ ]  **Esto es posible y se llama agrupación.**
- [x]  **Sí, esto es posible y se llama particionamiento.**

Correct

Correcto.Mediante el particionamiento, las tablas de la base de datos se pueden dividir en varios fragmentos y distribuirse en varios servidores.

- [ ]  **Sí, esto es posible y se llama replicación maestro-esclavo.**

**2.**Question 2

Un equilibrador de carga de distribución equilibrada distribuye el tráfico entrante por igual en todos los servidores.

1 / 1 point

**`Verdadero`**

**Falso**

Correct

Correcto. En el equilibrio de carga de distribución equilibrada, la carga se distribuye por igual entre varios servidores. Pero este proceso es menos eficiente que el equilibrio de carga basado en el estado.

**3.**Question 3

¿Cuál de los siguientes servidores se puede usar para proporcionar archivos estáticos y también puede actuar como un equilibrador de carga?

1 / 1 point

**Equilibrador de carga dedicado**

**`Proxy inverso`**

**Proxy de reenvío**

**Servidor web**

Correct

Correcto. Se puede configurar un proxy inverso que se encuentra frente a los servidores web para proporcionar los archivos estáticos y también distribuir las solicitudes entrantes a los servidores web de una manera basada en el estado o de distribución equilibrada.

**4.**Question 4

El proveedor de la nube administra la escalabilidad de la base de datos en un modelo informático en la nube IaaS.

1 / 1 point

**Verdadero**

**`Falso`**

Correct

Correcto. Cuando utiliza IaaS, usted mismo es responsable de crear la infraestructura y equilibrar la carga. El proveedor solo administra la escalabilidad de la base de datos si está utilizando su base de datos administrada o soluciones PaaS.

**5.**Question 5

¿Cuál de los siguientes es un hipervisor de tipo 2?

1 / 1 point

**KVM**

**Docker**

**Windows**

**`VirtualBox`**

Correct

Correcto. VirtualBox es un hipervisor multiplataforma de tipo 2 muy conocido que es de código abierto y gratuito.

**6.**Question 6

¿Cuáles de los siguientes términos se utilizan en la contenedorización? Elija todas las que correspondan.

1 / 1 point

- [ ]  **Hipervisores**
- [x]  **Docker**

Correct

Correcto. Docker es un motor de contenedores que puede ejecutar los contenedores.

- [x]  **Contenedor**

Correct

Correcto. Un contenedor es un bloque de construcción de este tipo de virtualización.

- [x]  **Kubernetes**

Correct

Correcto. Kubernetes es un sistema de gestión u orquestación de contenedores.

- [x]  **Pods**

Correct

Correcto. La colección de contenedores estrechamente acoplados se llama pod.

**7.**Question 7

Cada vez que cambia un archivo estático, la push CDN recopila automáticamente el archivo actualizado del servidor web.

1 / 1 point

**Verdadero**

**`Falso`**

Correct

Correcto. Debe cargar manualmente los archivos modificados en un servidor push CDN. Por otro lado, un servidor pull CDN recopila el archivo modificado automáticamente desde el servidor.

**8.**Question 8

¿Cuáles de los siguientes puntos son verdaderos acerca de la escalabilidad? Elija todas las que correspondan.

1 / 1 point

- [ ]  **En el escalado vertical, sigue agregando más unidades informáticas en la red.**
- [x]  **En el escalado horizontal, puede seguir agregando más unidades informáticas en la red.**

Correct

Correcto. Cuando se configura correctamente, la capacidad de su infraestructura se puede aumentar o disminuir agregando nodos o unidades informáticas en el escalado horizontal.

- [ ]  **En el escalado horizontal, sigue agregando núcleos de procesamiento, RAM y almacenamiento en el servidor.**
- [x]  **En el escalado vertical, puede seguir agregando núcleos de procesamiento, RAM y almacenamiento en el servidor.**

Correct

Correcto. El escalado vertical es una solución fácil para gestionar la carga agregando recursos de hardware al servidor.

- [x]  **En el escalado automático, el proveedor de la nube administra la escalabilidad y la capacidad aumenta o disminuye según la carga.**

Correct

Correcto. Cuando el proveedor de la nube admite el escalado automático, se encarga de todo mediante el escalado vertical y horizontal automático o usando una combinación de ambos tipos de escalado.

**9.**Question 9

Con una firma de URL, puede hacer que un archivo esté disponible públicamente durante cierto tiempo.

1 / 1 point

**`Verdadero`**

**Falso**

Correct

Correcto. La firma de URL es una política popular que se utiliza para hacer que un archivo esté disponible públicamente durante un cierto tiempo. HMAC es un mecanismo de firma de URL conocido utilizado por los desarrolladores de todo el mundo.

**10.**Question 10

¿Cuáles de las siguientes afirmaciones sobre un modelo informático sin servidor son verdaderas?

1 / 1 point

- [x]  **Bloqueado por el proveedor**

Correct

Correcto. Se bloquea el proveedor cuando usa un proveedor sin servidor, porque el código de su aplicación usa los servicios proporcionados por el proveedor sin servidor. Para alojar su aplicación con un proveedor diferente, es necesario un cambio de código.

- [x]  **Totalmente administrado**

Correct

Correcto. La plataforma y los servicios están totalmente gestionados por el proveedor. Simplemente escriba el código y envíelo al sistema de control de versiones. Los proveedores sin servidor toman el código actualizado y lo implementan automáticamente en la plataforma.

- [ ]  **No se requiere servidor.**
- [x]  **Puede ser costoso con el tiempo.**

Correct

Correcto. Los proveedores sin servidor le cobran de acuerdo a su uso. Cualquier uso no supervisado, código no optimizado o uso inadecuado pueden provocar un fuerte aumento en las facturas mensuales. Además, puede ser costoso a medida que su aplicación continúa creciendo.