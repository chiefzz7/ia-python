import json

# carregar os dados
with open("dados.json") as f:
    dados = json.load(f)


print("Dados carregados:")
print(dados)

# separar os dados
X = []
y = []

for item in dados:
    X.append([
        item["cor"],
        item["cheiro"],
        item["sabor"],
        item["temperatura"],
        item["textura"]
    ])
    y.append(item["gostou"])


print("\n Entradas (X):")
print(X)

print("\n Saídas (y):")
print(y)


# analise simples
media_cor = sum([item[0] for item in X]) / len(X)
media_cheiro = sum([item[1] for item in X]) / len(X)
media_sabor = sum([item[2] for item in X]) / len(X)
media_temperatura = sum([item[3] for item in X]) / len(X)
media_textura = sum([item[4] for item in X]) / len(X)

print("\n Média de cor: ", media_cor)

if media_cor < -0.5:
    print("Forte rejeicão por cor")
elif media_cor > 0.5:
    print("Boa aceitacao por cor")
else:
    print("Neutro para cor")

