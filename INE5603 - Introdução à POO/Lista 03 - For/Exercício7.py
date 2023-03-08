usuarios = int(input("Digite a quantidade de usuários: "))
media = 0
idadeNova = 0

for i in range(usuarios):
    idade = int(input("Informe a idade: "))
    idadeNova = idade + idadeNova
    
media = idadeNova / usuarios
if media >= 0 and media <= 25:
    print("A turma é jovem.")
elif media >= 26 and media <= 60:
    print("A turma é adulta.")
elif media > 60:
    print("A turma é idosa.")