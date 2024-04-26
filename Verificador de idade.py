print (" Bem-vindo ao Verificador de Idade ")
n1 = float(input(" Digite sua idade: "))

if n1 >= 60 :
    print (" Você está na faixa etária IDOSO ")

elif n1 >= 18:
    print (" Você está na faixa etária ADULTO" )

elif n1 >= 14 :
    print (" Você está na faixa etária ADOLESCENTE ")

elif n1 <= 13 :
    print (" Você está na faixa etária CRIANÇA ")

else:
    print(" Erro de Digitação, tente NOVAMENTE ")