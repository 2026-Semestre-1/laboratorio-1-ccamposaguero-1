def calculadora(op, op1, op2):
    if not isinstance(op, int):
        return "Error"
    elif not isinstance(op1, int):
        return "Error"
    elif not isinstance(op2, int):
        return "Error"
    elif not (op > 0 and op < 5):
        return "Error"
    elif not (op == 4 and op2 == 0):
        return "Error"
    else:
        return calculadora_Aux(op, op1, op2)

def calculadora(op, op1, op2):
    if op == 1:
        return op1 + op2
    elif op == 2:
        return op1 - op2
    elif op == 3:
        return op1 * op2
    else:
        return op1 // op2


def contadorDigitos(num, digito):
    if not isinstance(num, int):
        return "Error"
    elif not isinstance(digito, int):
        return "Error"
    elif not (digito >= 0 and digito < 10):
        return "Error"
    else:
        return contadorDigitos_Aux(num, digito)

def contadorDigitos_Aux(num, digito):
    resultado = 0

    while num != 0:
        if (num%10) == digito:
            resultado += 1

        num //= 10

    return resultado


def sumatoria_V2(inicio, fin, distancia, excepcion):
    if not isinstance(inicio, int):
        return "Error"
    elif not isinstance(fin, int):
        return "Error"
    elif not isinstance(distancia, int):
        return "Error"
    elif not isinstance(excepcion, int):
        return "Error"
    elif not (distancia >= 0 and distancia < 10):
        return "Error"
    elif not (excepcion >= 0 and excepcion < 10):
        return "Error"
    else:
        return sumatoria_V2_Aux(inicio, fin, distancia, excepcion)

def sumatoria_V2_Aux(inicio, fin, distancia, excepcion):

    resultado = 0

    while inicio > fin:
        if excepcion == 0:
            resultado += inicio
        else:
            if ((inicio % excepcion) != 0):
                resultado += inicio

        inicio += distiancia
