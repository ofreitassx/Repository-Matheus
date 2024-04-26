print (" Bem-vindo ao Verificador de Ano Bissexto ")
n1 = int (input(" Digite o ano que você quer verificar: "))

if n1 % 4 == 0 and ( n1 % 100 != 0 or n1 % 400 == 0):
    print (" Este é um ano bissexto ")

else :
    print (" Este não é um ano bissexto ")

