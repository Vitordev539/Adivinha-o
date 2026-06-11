from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador pensar 
print("-=-" * 20)
print("Vou pensar em um número tente adivihar...")
print("-=-" * 20)
jogador = int(input("Em que número pensei? ")) #jogador tenta adivinhar 
print("Processando...")
sleep(2) #pausa o programa por 2 segundos
if jogador == computador:
    print("Parabéns você acertou!")
else: 
    print("Você errou! O número que pensei foi {} e não  {}".format(computador, jogador))