def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

texto = input("Digite um texto: ")
print(f"Texto invertido: {inverter_string(texto)}")
