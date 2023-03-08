'''
Exerc 2 - Aula 21

Implementar um programa que calcule o aumento de salário dos funcionários de uma empresa.
 O aumento está condicionado ao atual salário de cada funcionário.
Regras:
para abaixo ou igual a R$2.000,00 : aumento de 15%;
para 2.000,00 < salarioAtual < = 3.000,00: aumento de 10%;
para acima de 3.000,00: aumento igual a 5%.

Calcular o aumento de 3 funcionários;

A cada cálculo efetuado imprimir as seguintes informações:
nome do funcionário,
salário atual e
salário com reajuste. 

Devem ser implementadas 2 arquivos (.py):
Um arquivo contendo uma classe Funcionário que conterá os métodos para calcular
o aumento de salário e o construtor. 
Um arquivo contendo o controle_do_Funcionário (main), onde serão feitas chamadas
para criar instâncias da classe Funcionário e também acessar  os métodos que pertencem
a classe Funcionário.  
'''

from lista_funcionario import Funcionario
funcionarios = []

'''
f1 = Funcionario("Patrick",5000)
f2 = Funcionario("Renato", 4500)
f3 = Funcionario("Matheus",1500)
f4 = Funcionario("Josefina",2500)
f5 = Funcionario("Pedro", 1000)
f1.aumento_salario()
f1.info_funcionario()
f2...
'''

for i in range(2):
    func = Funcionario(input("Digite o nome:"),float(input("Digite o salário: ")))
    funcionarios.append(func)


for f in funcionarios:
    f.aumento_salarial()
    print('='*40)
    f.info_funcionario()
    print('='*40)

nome = input("Digite o nome:")
for f in funcionarios:
    if nome == f.getNome():
        f.info_funcionario()
