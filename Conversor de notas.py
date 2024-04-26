print (" Bem-vindo ao Conversor de Nota em Conceito ")
n1 = float(input(" Digite sua nota: "))

if n1 >= 9:
    print (" Sua nota é A ")

elif n1 >= 7.5:
    print (" Sua nota é B ")

elif n1 >= 6:
    print (" Sua nota é C ")

elif n1 >= 4:
    print (" Sua nota é D ")

elif n1 <= 4:
    print (" Sua nota é F ")

else:
    print(" Erro na digitação, TENTE NOVAMENTE ")