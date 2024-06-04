print (" BEM VINDO A MARICA INTERNET & FIBRA OPTICA ")
preco1 = 0.20 # quando a conta vem abaixo de 200 minutos
preco2 = 0.18 # quando a conta vem entre 200 e 400 minutos
preco3 = 0.15 # quando a conta vem acima de 400 minutos
minutos = int(input("DIGITE QUANTOS MINUTOS VOCE USOU DE INTERNET DISCADA: "))
if minutos < 200:
    print ("SUA CONTA DE INTERNET DISCADA VEIO ", minutos * preco1)
elif minutos >= 200 or minutos <= 400:
    print ("SUA CONTA DE INTERNET DISCADA VEIO ", minutos * preco2 )
elif minutos > 400:
    print (" SUA CONTA DE INTERNET DISCADA VEIO ", minutos * preco3)
else:
    print (" ERRO DE DIGITACAO ")