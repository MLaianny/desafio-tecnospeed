import json

dados = {
    "faturamento": [100, 200, 300, 0, 400, 500, 0, 1000]  # Exemplo de dados
}

# Ignorando dias sem faturamento (dias com 0)
valores_validos = [valor for valor in dados["faturamento"] if valor > 0]

# Menor e maior faturamento
menor = min(valores_validos)
maior = max(valores_validos)

# Média dos valores válidos
media = sum(valores_validos) / len(valores_validos)

# Dias acima da média
dias_acima_media = sum(1 for v in valores_validos if v > media)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
