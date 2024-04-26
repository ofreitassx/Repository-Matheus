print ("Bem-vindo ao conversor de tamanhos ")              #varivavel qt = Qual Tamanho
print ("1 - centímetros")
print ("2 - metros")
print ("3 - polegadas")
print ("4 - quilômetros")
print ("5 - milhas")
print ("6 - pés")

qt = float(input("Digite qual a unidade de tamanho voce deseja usar: "))
if qt == 1:
    cm = float(input("Digite os centimetros: "))
    cmk = cm / 100000  #cmk  = centimetros para quilometros
    cmm = cm / 160900  #cmm  = centimetros para milhas
    cmp = cm / 30,48   #cmp  = centimetros para pes
    cmt = cm / 100     #cmt  = centimetros para metros
    cmp1 = cm / 2,54   #cmp1 = centimetros para polegadas

    print ("Centimetros para Quilometros: ", cmk) 
    print ("Centimetros para Milhas: ", cmm)
    print ("Centimetros para Pés: ", cmp)
    print ("Centimetros para Metros: ", cmt)
    print ("Centimetros para Polegadas: ", cmp1)

elif qt == 2:
    metros = float(input("Digite os metros: "))
    mc = metros * 100     # variavel mc = metros para centimetros
    mpl = metros * 39,37  # variavel mpl = metros para polegadas
    mq = metros / 1000    # variavel mq = metros para quilometros
    mm = metros / 1609    # variavel mm = metros para milhas
    mp = metros * 3,281   # variavel mp = metros para pes

    print ("Metros para Centimetros: ", mc)
    print ("Metros para Polegadas: ", mpl)
    print ("Metros para Quilometros: ", mq)
    print ("Metros para Milhas: ", mm)
    print ("Metros para Pés: ", mp)

elif qt == 3:
    polegadas = float(input("Digite as polegadas: "))
    pc = polegadas * 2,54      # variavel pc = polegadas para centimetros
    pm = polegadas / 39,37     # variavel pm = polegadas para metros
    pq = polegadas / 39370     # variavel pq = polegadas para quilometros
    pmm = polegadas / 63360    # variavel pmm = polegadas para milhas
    pp = polegadas / 12        # variavel pp = polegadas para pes

    print ("Polegadas para Centimetros: ", pc)
    print ("Polegadas para Metros: ", pm)
    print ("Polegadas para Quilometros: ", pq)
    print ("Polegadas para Milhas: ", pmm)
    print ("Polegadas para Pes: ", pp)

elif qt == 4:
    km = float(input("Digite os Quilometros: "))
    kc = km * 100000   # variavel kc = Quilometros para Centimetros
    km1 = km * 1000    # variavel km1 = Quilometros para Metros
    kmp = km * 39370   # variavel kmp = Quilometros para Polegadas
    kmm = km * 1,609   # variavel kmm = Quilometros para Milhas
    kpp=  km * 3281    # variavel kpp = Quilometros para Pes

    print ("Quilometros para Centimetros: ", kc)
    print ("Quilometros para Metros: ", km1)
    print ("Quilometros para Polegadas: ", kmp)
    print ("Quilometros para Milhas: ", kmm)
    print ("Quilometros para Pés: ", kpp)

elif qt == 5:
    milhas = float(input("Digite as Milhas: "))
    mc2 = milhas * 160900    # variavel mc2 = Milhas para Centimetros
    mm2 = milhas * 1609      # variavel mm2 = Milhas para Metros
    mp2 = milhas * 63360     # variavel mp2 = Milhas para Polegadas
    mk2 = milhas * 1,609     # variavel mk2 = Milhas para Quilometros 
    mp1 = milhas * 5280      # variavel mp1 = Milhas para Pes

    print ("Milhas para Centimetros: ", mc2)
    print ("Milhas para Metros: ", mm2)
    print ("Milhas para Polegadas: ", mp2)
    print ("Milhas para Quilometros: ", mk2)
    print ("Milhas para Pes: ", mp1)

elif qt == 6:
    pes = float(input("Digite o tamanho em pés: "))
    pcm = pes * 30,48    # variavel pcm = Pes para Centimetros
    pmt = pes / 3,281    # variavel pmt = Pes para Metros
    ppl = pes / 12       # variavel ppl = Pes para Polegadas
    pkm = pes / 3281     # variavel pkm = Pes para Quilometros
    pml = pes / 5280     # variavel pml = Pes para Milhas

    print ("Pes para Centimetros: ", pcm)
    print ("Pes para Metros: ", pmt)
    print ("Pes para Polegadas: ", ppl)
    print ("Pes para Quilometros: ", pkm)
    print ("Pes para Milhas: ", pml)

else:
    print ("Erro, TENTE NOVAMENTE ")
    print ("Erro, TENTE NOVAMENTE ")