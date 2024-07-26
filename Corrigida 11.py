notas = []
for i in range(5):
    nota = float(input(f"Digite a nota do exame {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if all(nota >= 7 for nota in notas):
    classificacao = "A - passou em todos os exames"
elif notas[0] >= 7 and notas[1] >= 7 and notas[3] >= 7:
    if notas[2] < 7 or notas[4] < 7:
        classificacao = "B - passou em I, II e IV, mas não em III ou V"
elif notas[0] >= 7 and notas[1] >= 7:
    if (notas[2] >= 7 or notas[3] >= 7) and notas[4] < 7:
        classificacao = "C - passou em I e II, III ou IV, mas não em V"
else:
    classificacao = "Reprovado - outras situações"

print(f"Média: {media:.2f}")
print(f"Classificação: {classificacao}")
