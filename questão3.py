import json

faturamentoMensal = """
{
    "faturamento_diario": [200, 300, 0, 0, 400, 500, 0, 150, 250, 0, 0, 450, 700, 0, 0, 350, 0, 300, 0, 0, 600, 750, 0, 200, 0, 0, 0, 500, 400, 300]
}
"""

dados = json.loads(faturamentoMensal)
faturamento = [valor for valor in dados["faturamento_diario"] if valor > 0] #ignorando valores 0


menorFaturamento = min(faturamento)
maiorFaturamento = max(faturamento)


mediaMensal = sum(faturamento) / len(faturamento)


diasAcimaDaMedia = len([valor for valor in faturamento if valor > mediaMensal])

print(f"Menor valor de faturamento: R${menorFaturamento:.2f}")
print(f"Maior valor de faturamento: R${maiorFaturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {diasAcimaDaMedia}")