print ("BEM VINDO A VAGA DE EMPREGO")
idade = float(input("DIGIA A SUA IDADE: "))
nacionalidade = str(input("DIGITE A SUA NACIONALIDADE: "))
experiencia = float(input("DIGITE QUANTOS ANOS DE EXPERIENCIA VOCE TEM: "))
if idade >= 18:
    if nacionalidade == "brasileiro" or nacionalidade == "Brasileira" :
        if experiencia >= 2:
            print ("VOCE FOI APROVADO PARA A VAGA DE EMPREGO")

else:
    print ("/////           VOCE NAO TEM TODOS OS REQUISITOS PARA PASSAR NA VAGA DE EMPREGO           /////")
