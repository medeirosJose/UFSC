# Exerc 2 - Aula 21

from funcionario import Funcionario

f1 = Funcionario('Carla',5000)
f2 = Funcionario('Ronaldo',2500)
f3 = Funcionario('Maria', 1500)

#exemplo 1
#invocando método sem passagem de parâmetro
f1.aumento_salarial2()

#exemplo2
#invocando o método com passagem de parâmetro
f2.aumento_salarial1(f2.salarioAtual)
f3.aumento_salarial1(f3.salarioAtual)

print('='*40)
f1.info_funcionario()
print('='*40)
f2.info_funcionario()
print('='*40)
f3.info_funcionario()
print('='*40)