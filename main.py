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

def prever_alimento(alimento):
    score = (
        alimento["cor"] * 0.2 +
        alimento["cheiro"] * 0.1 +
        alimento["sabor"] * 0.3 +
        alimento["temperatura"] * 0.1 +
        alimento["textura"] * 0.3
    )

    if score > 0:
        return "👍 Provável que goste"
    elif score < 0:
        return "👎 Provável que não goste"
    else:
        return "😐 Neutro"


# testar alimentos
brocolis = {"cor": -1, "cheiro": -1, "sabor": -1, "temperatura": 1, "textura": 0}
banana = {"cor": 1, "cheiro": 1, "sabor": 1, "temperatura": 0, "textura": 1}

print("\n🥦 Brócolis:", prever_alimento(brocolis))
print("🍌 Banana:", prever_alimento(banana))