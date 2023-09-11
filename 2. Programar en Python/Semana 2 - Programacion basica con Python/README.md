# 

# Preguntas del modulo: programacion basica con python

## 1. ¿Cuál de los siguientes no es un tipo de datos de secuencia en Python?

- Diccionario

```
Explicacion:
Los diccionarios tienen una estructura de objeto de clave-valor y no son secuencias.
```



## 2. Para una lista dada denominada new_list, ¿cuál de las siguientes opciones funcionará?:

- new_list.extend(new_list)

```
Explicacion:
Esto extenderá la lista para dar [1,2,3,4,1,2,3,4]
```

- new_list.insert(0, 0)

```
Explicacion:
Esto insertará 0 en el índice 0 dando: [0,1,2,3,4]
```

- new_list.append(5)

```
Explicacion:
Esto agregará el valor 5 a la lista que da: [1,2,3,4,5]

```

## 3. ¿Cuál de las siguientes opciones no es un tipo de ámbito variable en Python?



## 4. ¿Cuál de los siguientes es una estructura de datos integrada en Python?

- Set

```
Explicacion:
El conjunto es una estructura de datos integrada, como lista, tupla, etc. 
```

## 5. Para un archivo dado denominado 'names.txt', cuál de las siguientes NO es una sintaxis válida para abrir un archivo:

- ```python
  with open('names.txt', 'rw') as archivo:
  print(type(file))
  ```
  
  ```
  Explicacion:
  Debe ser el modo 'r' para lectura o 'w' para escritura. 
  ```
  
  

## 6. ¿Cuál de las siguientes no es una excepción válida en Python?

- LoopError

```
Explicacion:
No existe tal excepción definida en Python. 
```

## 7. Para un archivo denominado name.txt que contiene las siguientes líneas:

```
First line
Second line
And another !
```

Cuál será la salida del siguiente código:



```python
with open('names.txt', 'r') as file:
 lines = file.readlines()
print(lines))
```



- ```
  [‘First line\n’,
  ‘Second line\n’,
  ‘And another !’]
  ```
  
  ```
  Explicacion:
  "readlines()" devuelve una lista ordenada con líneas en el archivo de texto como elementos de la lista. 
  ```

## 8. Estado VERDADERO o FALSO:*los args pasados a las funciones pueden aceptar el par de clave-valor.

- Falso

```
Explicacion:

```


