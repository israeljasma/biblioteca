def contar_vocales_recursivo(cadena):
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # Caso base: si la cadena está vacía, no hay vocales
    if not cadena:
        return 0

    # Obtener el primer carácter de la cadena
    primer_caracter = cadena[0]

    # Definir un conjunto de vocales (puedes agregar más si es necesario)
    

    # Si el primer carácter es una vocal, incrementar el contador en 1
    if primer_caracter in vocales:
        
        print(contar_vocales_recursivo(cadena[1:]))
        return 1 + contar_vocales_recursivo(cadena[1:])
    else:
        # Si el primer carácter no es una vocal, continuar con el resto de la cadena
        # print(contar_vocales_recursivo(cadena[1:]))
        return contar_vocales_recursivo(cadena[1:])

# Ejemplo de uso:
# texto = "Hola, ¿cómo estás?"
# contador_vocales = contar_vocales_recursivo(texto)
# print("El número de vocales en la cadena es:", contador_vocales)


def invertir_string(cadena):
    return cadena[::-1]


print(contar_vocales_recursivo("hola"))