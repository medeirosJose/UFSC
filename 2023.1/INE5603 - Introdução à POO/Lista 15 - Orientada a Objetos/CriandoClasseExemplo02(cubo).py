class Cubo:
    '''classe para calcular o cubo de um número'''
    def __init__(self,valor):
        self.x = valor
        print("Objeto criado")
    
    def calcula_cubo(self):
        cubo = self.x + self.x + self.x
        return "Cubo calculado: "+ str(cubo)

#main
print("oi")

#criando uma instância (objeto) da classe Cubo
teste1 = Cubo(10)
teste2 = Cubo(20)

#como mostrar o conteúdo de um atributo
print("Valor de x: ",teste1.x)
print("Valor de x: ", teste2.x)

#fazendo a invocação de um método
c = teste1.calcula_cubo()
print(c)

print(teste2.calcula_cubo())
