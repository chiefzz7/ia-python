import json
from sklearn.model_selection import train_test_split

from logica import prever_heuristica
from modelo import treinar_modelo, prever_modelo

# ========================
# 📊 CARREGAR DADOS
# ========================
with open("dados.json") as f:
    dados = json.load(f)

print("📊 Dados carregados:")
print(dados)

# ========================
# 🧠 SEPARAR X e y
# ========================
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

# ========================
# 📈 ANÁLISE SIMPLES
# ========================
media_cor = sum([item["cor"] for item in dados]) / len(dados)

print("\n📈 Média de cor:", media_cor)

if media_cor < -0.5:
    print("🚫 Forte rejeição por cor")
elif media_cor > 0.5:
    print("✅ Boa aceitação por cor")
else:
    print("😐 Neutro para cor")

# ========================
# 🧪 TESTE HEURÍSTICA
# ========================
brocolis = {"cor": -1, "cheiro": -1, "sabor": -1, "temperatura": 1, "textura": 0}
banana = {"cor": 1, "cheiro": 1, "sabor": 1, "temperatura": 0, "textura": 1}

print("\n🧪 HEURÍSTICA:")
print("🥦 Brócolis:", prever_heuristica(brocolis))
print("🍌 Banana:", prever_heuristica(banana))

# ========================
# 🤖 TREINAR IA
# ========================
print("\n🤖 Treinando modelo...")

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = treinar_modelo(X_treino, y_treino)

acuracia = modelo.score(X_teste, y_teste)
print(f"🎯 Acurácia: {acuracia:.2f}")

# ========================
# 🔮 TESTE IA
# ========================
print("\n🔮 IA:")
print("🥦 Brócolis:", prever_modelo(modelo, brocolis))
print("🍌 Banana:", prever_modelo(modelo, banana))