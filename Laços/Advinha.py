print('*'*34)
print("Bem vindo ao jogo de Adivinhação!")
print('*'*34)
numero_secreto = 42
total_de_tentativas = 3
rodada = 0

while(total_de_tentativas > 0):
    rodada +=1
    print('Rodada {}'.format(rodada))
    chute = int(input("Digite o seu número: "))
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if (acertou):
      print("Voce Acertou!\n")
      break
    else:
        if(maior):
            print("Voce errou! Seu chute é maior que o número secreto\n")
        elif(menor):
            print("Voce errou! Seu chute é menor que o número secreto\n")
    total_de_tentativas -= 1

print("Fim de jogo!")