import math

def intervalo_confianca_media(media_amostra, desvio_padrao_amostra, tamanho_amostra, valor_critico_t):
    erro_padrao = valor_critico_t * (desvio_padrao_amostra / math.sqrt(tamanho_amostra))
    intervalo_inferior = media_amostra - erro_padrao
    intervalo_superior = media_amostra + erro_padrao
    return intervalo_inferior, intervalo_superior

# Exemplo de uso
media_amostra = float(input("Digite a média da amostra: "))
desvio_padrao_amostra = float(input("Digite o desvio padrão da amostra: "))
tamanho_amostra = int(input("Digite o tamanho da amostra: "))
valor_critico_t = float(input("Digite o valor crítico t: "))

intervalo_inferior, intervalo_superior = intervalo_confianca_media(media_amostra, desvio_padrao_amostra, tamanho_amostra, valor_critico_t)
print(f"O intervalo de confiança para a média é:, {intervalo_inferior:.4f} {intervalo_superior:.4f}")
