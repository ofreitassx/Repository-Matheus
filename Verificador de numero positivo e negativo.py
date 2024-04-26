print (" Bem-vindo ao Verificador de números positivos e negativos. ")
n1 = float(input(" Digite um número: "))

if n1 > 0:
    if n1 % 2 == 0:
        print(" O número é POSITIVO E PAR  ")

    if n1 % 3 == 0:
        print(" O número é POSITIVO e MÚLTIPLO DE TRÊS ")

elif n1 < 0:
    if n1 % 2 != 0:
        print (" O número é NEGATIVO e ÍMPAR ")

    else:
        print(" O numero é NEGATIVO e PAR ")

else:
    print(" Erro na digitação, TENTE NOVAMENTE ")