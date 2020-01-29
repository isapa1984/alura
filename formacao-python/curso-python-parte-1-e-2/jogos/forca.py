from random import randrange


def mostrar_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def obter_palavra_secreta():
    # Obtém as palavras secretas do arquivo de palavras
    with open("palavras.txt") as arquivo:
        palavras_secretas = [linha for linha in arquivo]

    # Seleciona uma palavra aleatoriamente
    ind_palavra = randrange(0, len(palavras_secretas))
    return palavras_secretas[ind_palavra].strip().upper()


def obter_chute():
    chute = input("Qual a letra? ")
    return chute.strip().upper()


def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mostrar_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mostrar_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def jogar():
    mostrar_abertura()
    palavra_secreta = obter_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta]
    acertou = False
    enforcou = False
    num_erros = 0
    max_tentativas = 7

    print(letras_acertadas)
    while (not acertou and not enforcou):
        chute = obter_chute()

        if (chute in palavra_secreta):
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            num_erros += 1
            desenha_forca(num_erros)

        enforcou = num_erros == max_tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    print()

    if (acertou):
        mostrar_mensagem_vitoria()
    else:
        mostrar_mensagem_derrota(palavra_secreta)

    print()
    print("-- Fim de Jogo --")


if __name__ == '__main__':
    jogar()
