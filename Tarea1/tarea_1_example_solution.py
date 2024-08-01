def operation_selector(num1, num2, op):
    """
    Realiza una operación aritmética o bit a bit entre dos números enteros.

    Parámetros:
    num1 (int): El primer número entero.
    num2 (int): El segundo número entero.
    op (str): El operador que define la operación a realizar.
              Puede ser '+', '-', '*', '&'.

    Retorna:
    tuple: Un código de estado (0 para éxito, otro valor para error)
           y el resultado de la operación o None en caso de error.

    Objetivo de la función: Verifica que los parámetros sean del tipo correcto.
    Realiza la operación correspondiente según el operador proporcionado.
    """

    # Verificar que num1 y num2 sean enteros y no sean True, False o None
    if not isinstance(num1, int) or not isinstance(num2, int) or \
       num1 in [True, False] or num2 in [True, False]:
        return -50, None  # Código de error único para parámetros no enteros

    # Verificar que op sea un string y no sea None
    if not isinstance(op, str) or op is None:
        return -60, None  # Código de error único para op no string

    # Verificar que op sea una de las opciones permitidas
    if op not in ['+', '-', '*', '&']:
        return -70, None  # Código de error único para op no válido

    # Realizar la operación según el carácter op
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '&':
        result = num1 & num2

    return 0, result  # Código de éxito y resultado de la operación


def calculo_promedio(lista_valores):
    """
    Calcula el promedio de una lista de valores numéricos.

    Parámetros:
    lista_valores (list): Lista de valores numéricos (int o float)
                          con un máximo de 10 elementos.

    Retorna:
    tuple: Un código de estado (0 para éxito, otro valor para error)
           y el promedio de los valores o None en caso de error.

    Objetivo de la función: Verifica que el parámetro sea una lista.
    Verifica que la lista no tenga más de 10 elementos.
    Verifica que todos los elementos de la lista sean números.
    Calcula el promedio de los valores en la lista.
    """
    # Verificar que lista_valores sea una lista
    if not isinstance(lista_valores, list):
        return 1, None  # Código de error único para parámetro no lista

    # Verificar que el tamaño de la lista no sea mayor a 10 elementos
    # Código de error único para lista con más de 10 elementos
    if len(lista_valores) > 10:
        return -90, None

    # Verificar que todos los elementos de la lista sean números
    # Código de error único para elementos no numéricos
    for valor in lista_valores:
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            return -80, None

    # Calcular el promedio de los valores en la lista
    promedio = sum(lista_valores) / len(lista_valores)

    return 0, promedio  # Código de éxito y resultado de la operación
