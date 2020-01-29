from random import randrange


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = randrange(1, 101)
    max_tentativas = 0
    pontos = 1000

    nivel_str = input('Qual o nível de dificuldade? (1) Fácil (2) Médio (3) Difícil => ')
    nivel = int(nivel_str)

    if (nivel == 1):
        max_tentativas = 20
    elif (nivel == 2):
        max_tentativas = 10
    else:
        max_tentativas = 5

    for tentativa in range(1, max_tentativas + 1):
        print("Tentativa {} de {}".format(tentativa, max_tentativas))
        chute_str = input("Digite um número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            print()
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!!!")
            break
        else:
            if (maior):
                print("Errou!!! Chutou pra cima")
            elif (menor):
                print("Errou!!! Chutou pra baixo")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

        print()

    print("Total de Pontos: {}".format(pontos))
    print("Número Secreto: {}".format(numero_secreto))

    print("-- Fim de Jogo --")


if __name__ == '__main__':
    jogar()
