soma = 0
print ("DIGITE 0 PARA FECHAR")
while True:
    n1 = int(input("DIGITE UM NUMERO POSITIVO: "))
    if n1 == 0:
        break
    soma += n1

print("A soma de todos os números digitados é:", soma)