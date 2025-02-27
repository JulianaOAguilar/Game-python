import random
randomNumber = random.randrange(1, 10)

print("usuário, tente advinhar o numero!")
guess = int(input("Digite um numero entre 1 e 10: "))

while guess != randomNumber:
    guess = int(input("Errado, tente novamente: "))
print("Parabéns, você acertou!")
