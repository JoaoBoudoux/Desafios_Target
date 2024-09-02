def inverterString(s):
    inverted = ""
    for i in range(len(s)-1, -1, -1):
        inverted += s[i]
    return inverted


stringOriginal = input("Digite uma string para inverter: ")#palavra que vai ser invertida


stringInvertida = inverterString(stringOriginal)
print(f"String invertida: {stringInvertida}")