# Evaluacion Final

## 1. Python es un lenguaje interpretado. ¿Cuál de las siguientes afirmaciones describe correctamente un lenguaje interpretado?

El código fuente está prediseñado y compilado antes de ejecutarse.

- El código fuente se convierte en bytecode que luegomáquina virtual Python lo ejecuta.  

Python guardará todo el código primero antes de ejecutarse.  

Python necesita construirse antes de ejecutarse.

## 2. ¿Por qué es importante la identación en Python?

El código se compilará más rápido con indentación.  

- Python utilizó indentación para determinar qué bloque de código comienza y termina.  

Hace el código más legible.  

El código se leerá de manera secuencial.

## 3. ¿Cuál será la salida del siguiente código?

```python
names = ["Anna", "Natasha", "Mike"]
names.insert(2, "Xi")
print(names)
```

[“Anna”, “Natasha”, “Xi”, “Mike”]

## 4. ¿Cuál será la salida del siguiente código?

```python
for x in range(1, 4):
    print(int((str((float(x))))))
```

R: 

Dará un error

```
 El flotante primero se convertirá en cadena y salida, como <class 'float'>, que no se puede convertir en  ‘int’.
```

## 5. ¿Cuál será la salida del siguiente código?

```python
sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict:
    print(x)
```

R: 1 2 3

```
Los valores predeterminados impresos desde un diccionario son claves.
```

## 6. ¿Cuál será la salida del código recursivo a continuación?

```python
def recursion(num):
    print(num)
    next = num - 3
    if next > 1:
        recursion(next)

recursion(11)
```

R: 11 8 5 2

```
Los valores impresos tienen diferencia de 3, pero impresos en orden opuesto.
```

## 7. ¿Cuál será el tipo de complejidad de tiempo para la siguiente pieza de código?

```python
def bigo(numbers):
    for i in numbers:
        print(numbers)

bigo([1, 7, 13, 19])
```

## 8. ¿Cuál será la salida del siguiente código?

```python
str = 'Pomodoro'
for l in str:
if l == 'o':
    str = str.split()
    print(str, end=", ")
```

R: Generará un error

```
La primera función ‘split()’ que utiliza, la variable ‘str’ se convertirá en una lista sobre la cual no se puede utilizar ‘split()’ y dará un error.
```

## 9 . Encuentre la salida del código a continuación:

```python
def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()
```

R: yellow

```

```

## 10. Encuentre la salida del codigo a continuacion

```python
num = 9
class Car:
    num = 5
    bathrooms = 2

def cost_evaluation(num):
    num = 10
    return num

class Bike():
    num = 11

cost_evaluation(num)
car = Car()
bike = Bike()
car.num = 7
Car.num = 2
print(num)
```

R: 9

```
El valor de la variable global se mantendrá sin cambios.
```

## 11. ¿Cuál de las siguientes es la implementación correcta que devolverá Verdadero si hay una clase padre P, con un objeto p y una subclase denominada C, con un objeto c?

R: print(issubclass(C,P))

```
 Se puede leer como C es subclase de P.
```

## 12. Django es un tipo de:

R: Marco fullstack

```
Django es un marco fullstack.
```

## 13. ¿Cuál de los siguientes no es cierto sobre las pruebas de integración?

R: Es donde se prueba la aplicación en su conjunto.

```
This is the case with system testing.
```

## 14. Al utilizar pytest para pruebas, es necesario ejecutar el archivo que contiene el código principal antes de ejecutar el archivo de prueba que contiene nuestras pruebas de unidad.

R: Falso

```
El archivo principal debe guardarse para mantenerlo actualizado pero no es necesario para ejecutarlo. Tenemos que importarlo a nuestro archivo de pruebas.
```

## 15. ¿Cuál será la salida del siguiente código?

```python
class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a())
```

R: Funcion dentro de A

```
 La clase A viene antes de la clase B en términos de las clases principales de la clase D.
```


