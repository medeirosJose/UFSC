
clientes = {"Pedro","Maria","Francisco"}
clientes2={"Pedro", "ana","francisco"}
print(clientes)
print(clientes2)


print(" interseção entre o conjunto cliente e clientes2")
print(clientes.intersection(clientes2))
print("não altera o original:", clientes)


print("atualiza o original:")
clientes.intersection_update(clientes2)
print(clientes)












