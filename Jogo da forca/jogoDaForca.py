import random

#palavra a ser acertada
palavraSecreta = ["PERA", "MACA", "UVA", "BANANA", "MELANCIA", "CAQUI", "KIWI", "ABACATE", "TOMATE", "MARACUJA", "ABACAXI", "AMORA", "CACAU", "CARAMBOLA", "CEREJA", "COCO", "FRAMBOESA"]

#variaveis
tentativas = 8
posicao = 0
indice = 0
#randomizar a palavra a ser acertada
palavra = random.choice(palavraSecreta)

#palavra censsurada
palavraCenssurada = ['*']*len(palavra)



#verificacao das letras no vetor e sistema de tentativas e substuicao de * da palavra censsurada

while True:
    print("////JOGO DA FORCA////")
    print(f"\nVocê ainda tem {tentativas} tentativas\n")
    print(" ".join(palavraCenssurada))

    L = input("\nDigite uma letra maiuscula e sem acento: ")

    if L in palavra:
        
        for letra in range(len(palavra)):
            
            if L == palavra[letra]:
                palavraCenssurada[letra] = L
                posicao += 1
            
            else:
                posicao += 1

    else:
        print("\nEssa letra nao esta na palavra -1 tentativa\n")
        tentativas -= 1
    
    if tentativas == 0:
        print("Você PERDEU\n")
        break
    if '*' not in palavraCenssurada:
        print("\nParabéns Você acertou a palavra\n")
        break