import random

score = 1
num_random = random.randint(0,10)
print("Sou seu computaodor...\nAcabei de pensar em um número entre 0 e 10.")
print("Sera que você consegue advinhar qual foi?")

user = int(input("Qual seu palpite? "))
while user != num_random:
    score += 1 
    if user > num_random:
        print("Menos... Tente mais uma vez.")
        user = int(input("Qual seu palpite? "))
    else:
        print("Mais... Tente mais uma vez.")
        user = int(input("Qual seu palpite? "))

if score == 1:
    print("Parabéns!!! Acertou você primeira!!!")
else:
    print(f"Você acertou com {score} tentativas. Parabéns!")