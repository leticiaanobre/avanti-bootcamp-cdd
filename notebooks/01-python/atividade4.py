import random

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0

print(" ual o nivel de dificuldade?")
print("1 - Fácil, 2- Médio, 3 - Difícil")
nivel = int(input("Digite o nível: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5

for rodada in eange(1, total_de_tentativas +1):
    print(f"Tentativas {rodada} de {total_de_tentativas}")
    valor_escolhido_str = input("Digite um numero de 1 a 100")
    print("Você digitou ", valor_escolhido_str)
    valor_escolhido = int(valor_escolhido_str)

    if valor_escolhido < 1 or valor_escolhido > 100:
        print("Numero invalido, o numero deve estar entre 1 e 100")
        continue

    acertou = valor_escolhido == numero_secreto
    maior = valor_escolhido > numero_secreto
    menor = valor_escolhido < numero_secreto

    if acertou:
        print("Parabens, voce acertou!")
        break
    else:
        if maior:
            print("Voce errou, seu numero foi maior que o numero secreto.")
        elif menor:
            print("Voce errou, seu numero foi menor que o numero secreto")

print("Fim de jogo!")