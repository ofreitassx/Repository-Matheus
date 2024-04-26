print (" Bem-vindo à Calculadora de Juros Simples ")
valor = float(input(" Digite seu Valor Inicial: "))
taxa = float(input(" Digite sua taxa de Juros: "))
periodo = float(input(" Periodo de Juros (em meses): "))

print ( "O valor dos seus Juros é: ", valor * (taxa / 100) * periodo )

