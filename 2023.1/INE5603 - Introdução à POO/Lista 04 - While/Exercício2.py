from random import randrange

num = randrange(11)
cont = 1

teclado = int(input('Digite um número entre 0 e 10: '))
while num != teclado:
  teclado = int(input('Não era esse número. Digite novamente... '))
  cont += 1
print("Você acertou! O número era {} e você realizou {} tentativas!".format(num, teclado))