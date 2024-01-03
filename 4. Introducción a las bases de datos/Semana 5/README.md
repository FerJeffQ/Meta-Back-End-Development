# Evaluación calificada: Introducción a las bases de datos

**Esta evaluación consta de dos partes: bloque de código y un cuestionario.**

## **1.**Pregunta 1

Escriba una sentencia SQL para crear una base de datos llamada “SportsClub"”

### R: `CREATE DATABASE SportsClub;`

## **2.**Pregunta 2

En el campo de texto que se encuentra a continuación, ingrese la palabra clave faltante (___) para crear una tabla llamada "Players".

```sql
CREATE ____ Players (playerID INT, playerName VARCHAR(50), age INT, PRIMARY KEY(playerID));
```

Ejecute la sentencia SQL completa en MySQL para crear la tabla en la base de datos del club.

### R: `TABLE`

## **3.**Pregunta 3

En el campo de texto que se encuentra a continuación, ingrese la palabra clave faltante (___) para ingresar datos a la tabla "Players"

```sql
INSERT INTO Players (playerID, playerName, age) ____ (1, "Jack", 25);
```

### R: `VALUES`

## **4.**Pregunta 4

Inserte tres registros más en la tabla “Players” que contengan los siguientes datos:

- (2, "Karl", 20)
- (3, "Mark", 21)
- (4, "Andrew", 22)

Una vez que haya ejecutado la sentencia INSERT INTO para ingresar estos tres registros de datos, ejecute la siguiente sentencia SQL:

```sql
SELECT playerName FROM Players WHERE playerID = 2;
```

¿Cuál es el nombredeljugador que aparece en la pantalla?

### R: `Karl`

## **5.**Pregunta 5

Escriba una sentencia SQL que dé como resultado todos los nombres de los jugadores en la tabla “Players”. Cuando ejecuta la consulta SQL correcta, debe obtener el siguiente resultado:

### R: `SELECT playerName FROM Players;`

## **6.**Pregunta 6

La siguiente tabla llamada “Players”, contiene cuatro registros de datos. Escriba una sentencia SQL que actualice la edad del jugador con ID = 3. El valor de la nueva edad debería ser '22'.

![Untitled](Evaluacio%CC%81n%20calificada%20Introduccio%CC%81n%20a%20las%20bases%20d%20539a6900f95848508d3749b80463b2bc/Untitled.png)

### R: `UPDATE Players SET age = 22 WHERE playerID = 3;`

## **7.**Pregunta 7

La siguiente tabla llamada “Players” contiene cuatro registros de datos. Escriba una sentencia SQL que elimine el registro del jugador con ID = 4.

![Untitled](Evaluacio%CC%81n%20calificada%20Introduccio%CC%81n%20a%20las%20bases%20d%20539a6900f95848508d3749b80463b2bc/Untitled%201.png)

### R: `DELETE FROM Players WHERE playerID = 4;`

## **8.**Pregunta 8

Escriba una sentencia SQL que evalúe si el IDdeljugador en la siguiente tabla “Players” es par o impar.

**Pista:** Supongamos que X es un número. Si el resto de X dividido por 2 es 0, entonces X es un número par; de lo contrario, X es un número impar. Recuerde utilizar el símbolo “%” para obtener el resto.

| PlayerID | Name |
| --- | --- |
| 1 | Karl |
| 2 | Adam |
| 3 | Anas |

### R: `SELECT PlayerID % 2 FROM Players;`

## **9.**Pregunta 9

Escriba una sentencia SQL que genere todos los nombres de los jugadores en la siguiente tabla de “Players” que sean mayores de 25 años.

| Age | Name |
| --- | --- |
| 38 | Karl |
| 25 | Adam |
| 22 | Anas |

### R: `SELECT Name FROM Players WHERE Age > 25;`

## **10.**Pregunta 10

Revise el siguiente diagrama de ER. Escriba la parte que falta de la sentencia SQL para definir una clave externa que vincule la tabla del curso con la tabla de departamento.

![Untitled](Evaluacio%CC%81n%20calificada%20Introduccio%CC%81n%20a%20las%20bases%20d%20539a6900f95848508d3749b80463b2bc/Untitled%202.png)

```sql
CREATE TABLE Course( 
 courseID int NOT NULL, courseName VARCHAR(50), PRIMARY KEY (courseID), 
   ____ ____(____) ____ ____ (____) 
);
```

**Pista:** escriba solo la parte que falta en su respuesta.

### R: `FOREIGN KEY(departmentID) REFERENCES Department (departmentID);`

# **Part 2 - Quiz**

## **11.**Pregunta 11

¿Qué es una fila de información sobre un miembro específico del personal en una tabla de base de datos de la universidad a la que se hace referencia?

    - **Una columna**

    - **Una clave**

R: - **`Un registro`**

## **12.**Pregunta 12

Una base de datos de club deportivos incluye una tabla llamada “Miembros” con dos columnas:

- Una columna 'número de miembro' que contiene el número de teléfono de cada miembro
- Y una columna 'nombre completo' que contiene el nombre completo de cada miembro.

Elija el tipo de datos adecuado para cada columna. Seleccione todas las respuestas correctas.

- [x]  **El tipo de datos de columna Nombre completo es VARCHAR**
- [ ]  **El tipo de datos de columna Nombre completo es CHAR.**
- [x]  **El tipo de datos de columna Número de jugador es INT.**
- [ ]  **El tipo de datos de la columna Número de jugador es DECIMAL.**

## **13.**Pregunta 13

En un club de fútbol, el nivel de habilidad de todos los jugadores nuevos se debe establecer de forma automática en el nivel predeterminado 1. ¿Qué sintaxis SQL se utiliza para establecer este nivel predeterminado mediante el uso de la palabra clave DEFAULT?

- **DEFAULT level INT 1;**
- R: `**level INT DEFAULT 1;**`

## **14.**Pregunta 14

Las restricciones de la base de datos se utilizan para limitar el tipo de valor de datos que se pueden almacenar en una tabla

- **Falso**
- R: **`Verdadero`**

## **15.**Pregunta 15

El resultado de la siguiente sentencia SQL son los datos de todos los clientes de Italia.

```sql
SELECT * FROM customers WHERE Country = "Italy";
```

- R: **`Verdadero`**
- **Falso**

## **16.**Pregunta 16

El resultado de la siguiente sentencia SQL devuelve los registros de todos los clientes de la India en orden alfabético de la A a la Z.

```sql
SELECT * FROM students WHERE country = "India" ORDER BY FirstName DESC;
```

- **Verdadero**
- R: **`Falso`**

```sql
¡Correcto! El resultado de esta sentencia SQL muestra los registros de todos los clientes de la India en orden alfabético inverso de la Z a la A. Esto se debe a que la palabra clave DESC ordena los registros en orden descendente
```

## **17.**Pregunta 17

¿Qué hace la siguiente sentencia SQL?

```sql
SELECT * FROM Players ORDER BY Country, PlayerName;
```

- **Ordena el resultado por país e ignora el nombre del personal.**
- R: **`Muestra los resultados ordenados, primero, por país y, luego, por el nombre del jugador.`**

## **18.**Pregunta 18

La siguiente tabla de datos cumple con la primera forma normal.

| ID del departamento | Nombre del departamento | Jefe del departamento | ID del curso | Nombre del curso |
| --- | --- | --- | --- | --- |
| D1 | Computing | Dr Karl | C1 | Database |
| D1 | Computing | Dr Karl | C2 | Python |
| D1 | Computing | Dr Karl | C3 | Web |
| D1 | Computing | Dr Karl | C4 | Java |
| D2 | Math | Dr Mosa  | C5 | Math |
- R: **`Falso`**
- **Verdadero**

```sql
¡Correcto! Esta tabla contiene grupos de datos repetitivos innecesarios en las columnas ID del departamento, nombre de departamento y jefe del departamento. Estas columnas infringen la regla de primera forma normal.
```

## **19.**Pregunta 19

¿Cuál de los siguientes representa el diagrama correcto que vincula la tabla de cursos con la tabla de departamentos?

![Untitled](Evaluacio%CC%81n%20calificada%20Introduccio%CC%81n%20a%20las%20bases%20d%20539a6900f95848508d3749b80463b2bc/Untitled%203.png)

- **Diagrama 1**
- R: **`Diagrama 2`**

```sql
¡Correcto! La clave externa IDdeldepartamento conecta la tabla Curso con la tabla Departamento.
```

## **20.**Pregunta 20

Identifique la relación entre las tablas en el diagrama.

![Untitled](Evaluacio%CC%81n%20calificada%20Introduccio%CC%81n%20a%20las%20bases%20d%20539a6900f95848508d3749b80463b2bc/Untitled%204.png)

- **Relación de uno a uno.**
- **Relación de muchos a muchos.**
- R: **`Relación de muchos a uno.`**

```sql
¡Correcto! Estos diagramas muestran un ejemplo de una relación de muchos a uno, ya que varios cursos pueden pertenecer a un departamento
```