soma = 0
contador = 0
n1 = int(input("DIGITE UM NUMERO INTEIRO: " ))
if n1 >= 0:
      while contador < 9:
            numero = int(input("DIGITE UM NUMERO INTEIRO: "))
            soma += numero
            contador += 1
            print (soma + n1)

else:
      print("O NUMERO NÃO É POSITIVO")