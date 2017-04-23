print("O primeiro jogador sempre começa.\n")

jogador1=input("Digite o nome do PRIMEIRO jogador\n")

jogador2=input("Digite o nome do SEGUNDO jogador\n")

num=input("jogador1, digite o primeiro numero para seu adversario adivinhar\n")
num2=input("jogador1, digite o primeiro numero para seu adversario adivinhar\n")

if num>num2:
    maior=num
    menor=num2
    
else:
    maior=num2
    menor=num
contLinha=0
contChute=0
acertos=0

while contLinha<50:
    print("\n")
    contLinha=contLinha+1

while contChute<3 and acertos!=2:
    
    print(jogador2,"Tente adivinhar os numeros que ",jogador1, "escolheu")
    chute=input()
    
    if chute>maior:
        print("Seu chute foi maior que os numeros escolhido por", jogador1)
        contChute=contChute+1
        
    elif chute<menor:
        print("Seu chute foi menor que os numeros escolhido por", jogador1)
        contChute=contChute+1
    
    elif menor<chute<maior:
        print("Seu chute esta entre o maior e o menor numero escolhido por", jogador1)
        contChute=contChute+1
        
    elif chute==maior:
        print("Parabens!! Você Acertou o MAIOR numero")
        acertos=acertos+1
        contChute=contChute+1
        
    elif chute==menor:
        print("Parabens!! Você Acertou o MENOR numero")
        acertos=acertos+1
        contChute=contChute+1
if acertos==2:
    print("VOCE ACERTOU OS DOIS NUMEROOOOS PARABEEENS!!")
else:
    print("Você usou todas as suas chances")
