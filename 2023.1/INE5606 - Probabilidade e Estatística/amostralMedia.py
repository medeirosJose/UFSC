import math

def intervalo_confianca_media(media_amostra, desvio_padrao_amostra, tamanho_amostra, nivel_confianca):
    valor_critico_z = 0.0

    # Verifica o valor crítico Z baseado no nível de confiança
    if nivel_confianca == 0.90:
        valor_critico_z = 1.645
    elif nivel_confianca == 0.95:
        valor_critico_z = 1.96
    elif nivel_confianca == 0.99:
        valor_critico_z = 2.576
    else:
        raise ValueError("Nível de confiança inválido. Os valores aceitos são 0.90, 0.95 ou 0.99.")

    erro_padrao = valor_critico_z * (desvio_padrao_amostra / math.sqrt(tamanho_amostra))
    intervalo_inferior = media_amostra - erro_padrao
    intervalo_superior = media_amostra + erro_padrao

    return intervalo_inferior, intervalo_superior

# Exemplo de uso
media_amostra = float(input("Digite a média da amostra: "))
desvio_padrao_amostra = float(input("Digite o desvio padrão da amostra: "))
tamanho_amostra = int(input("Digite o tamanho da amostra: "))
nivel_confianca = float(input("Digite o nível de confiança (0.90, 0.95 ou 0.99): "))

intervalo_inferior, intervalo_superior = intervalo_confianca_media(media_amostra, desvio_padrao_amostra, tamanho_amostra, nivel_confianca)
print("O intervalo de confiança para a média é:", intervalo_inferior, "-", intervalo_superior)
