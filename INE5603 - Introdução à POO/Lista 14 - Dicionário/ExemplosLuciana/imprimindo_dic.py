#imprimindo um dicionário
produtos = [{'nome': 'mamao' , 'preco': 2.19},
            {'nome': 'cebola', 'preco': 3.10},
            {'nome': 'tomate', 'preco': 2.80},
            {'nome': 'uva', 'preco': 2.73}]

for e in produtos:
    for v in e.values():
        print(v, end=' ')
    print()