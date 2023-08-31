class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def nome(self):
        return self.nome

    def novoNome(self, nome):
        self.nome = nome

    def idade(self):
        return self.idade

    def altura(self):
        return self.altura

    # função __str__ é chamada quando o objeto é passado como parâmetro para a função print()
    # def __str__(self) -> str:
    #    return f"{self.nome} tem {self.idade} anos e {self.altura} de altura."

    def get_all(self):
        # return f"{self.nome}, {self.idade} anos, {self.altura} de altura."
        return self.nome, self.idade, self.altura


p1 = Pessoa("João", 20, 1.80)
print(p1.get_all())
p2 = Pessoa("Maria", 25, 1.70)
p1.novoNome("Naldo")
print(p1.get_all())
print("antes", p2.get_all())
p2 = p1
print(p2.get_all())
