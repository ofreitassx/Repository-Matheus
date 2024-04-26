print (" Bem vindo a calculadora de triangulo ")

n1 = float(input(" Digite o primeiro tamanho: "))
n2 = float(input(" Digite o segundo tamanho: "))
n3 = float(input(" Digite o terceiro tamanho: "))

if n1 == n2 == n3:
    print (" Este é um triângulo do tipo equilátero. ")

elif n1 == n2 != n3:
    print(" Este é um triângulo do tipo isósceles. ")

elif n1 != n2 != n3:
    print (" Este é um triângulo do tipo escaleno ")

else:
    print (" Não foi possível formar um triângulo ") 