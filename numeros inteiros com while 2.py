soma = 0
print ("DIGITE 0 PARA FECHAR")
while True:
    numero = int(input("DIGITE UM NUMERO POSITIVO: "))
    if numero == 0:
        break
    soma += numero

print("A soma de todos os números digitados é:", soma)