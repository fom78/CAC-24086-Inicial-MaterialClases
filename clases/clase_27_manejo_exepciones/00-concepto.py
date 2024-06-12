'''
info: https://docs.python.org/es/3/tutorial/errors.html

Nuestro codigo puede estar perfecto, pero incluso podemos tener errores en tiempo de ejecucion, puede darse al ingreso de un valor que sea no esperado y nos rompa el codigo.

Para manejar desde codigo estos errores predecibles podemos usar los bloques try y except.

Veamos algunos mensajes de error tipicos:

- int("hola") --> ValueError: invalid literal for int() with base 10: 'hola'

- "4" + 3 --> TypeError: can only concatenate str (not "int") to str
- "34" >= 45
- 3 / 0 --> ZeroDivisionError: division by zero


- [1,2,"a"][4] --> IndexError: list index out of range
'''

int("34")
# int("hola")

[1,2,"a"][4]