import csv
import matplotlib.pyplot as plt

accessed_count = 0
never_accessed_count = 0

with open("frequencia.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    # Ignorar a primeira linha (cabeçalho)
    next(leitor_csv)

    for linha in leitor_csv:
        curso = linha[0]
        nome = linha[1]
        ultimo_acesso = linha[2]

        if ultimo_acesso != "Nunca" and nome != "":
            accessed_count += 1
        elif ultimo_acesso == "Nunca" and nome != "":
            never_accessed_count += 1

# Configuração do gráfico de pizza
labels = ["Acessaram", "Nunca Acessaram"]
sizes = [accessed_count, never_accessed_count]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
plt.title("Análise de Frequência de Acesso ao Curso")

plt.show()
