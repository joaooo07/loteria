bandit =  [2,4,6,9,10,11,12,13,15,18,19,21,23,24,25]
mike = [2,4,5,6,9,10,11,12,13,15,18,19,21,24,23,]
duke = [1,2,4,6,11,12,13,14,15,19,18,21,23,24,25]
contador = 0
contador2 = 0
contador3 = 0
for i in range(15):
    num = int(input("Digite um número para comparar: "))
    if num in bandit:
        contador += 1
    if num in mike:
         contador2 += 1
    if num in duke:
        contador3 += 1

print("""O JOGO BANDIT TEM {} ACERTOS
 O JOGO MIKE TEM {} ACERTOS
 O JOGO DUKE TEM {} ACERTOS """.format(contador,contador2,contador3))

if contador == 11:
    print("Parabêns você ganhou 6,00 reais")
if contador == 12:
    print("Parabêns você ganhou 12,00 reais")
if contador == 13:
    print("Parabêns você ganhou tantos reais")
if contador == 14:
    print("Parabêns você ganhou muitos reais")
if contador == 15:
    print("voce ta rico")
if contador <= 10:
    print("nao teve premio no seu jogo")
if contador2 == 11:
    print("Parabêns você ganhou 6,00 reais")
if contador2 == 12:
    print("Parabêns você ganhou 12,00 reais")
if contador2 == 13:
    print("Parabêns você ganhou tantos reais")
if contador2 == 14:
    print("Parabêns você ganhou muitos reais")
if contador2 == 15:
    print("voce ta rico")
if contador2 <= 10:
    print("nao teve premio no seu jogo")
if contador3 == 11:
    print("Parabêns você ganhou 6,00 reais")
if contador3 == 12:
    print("Parabêns você ganhou 12,00 reais")
if contador3 == 13:
    print("Parabêns você ganhou tantos reais")
if contador3 == 14:
    print("Parabêns você ganhou muitos reais")
if contador3 == 15:
    print("voce ta rico")
if contador3 <= 10:
    print("nao teve premio")