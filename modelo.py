from sklearn.linear_model import LogisticRegression

def treinar_modelo(X, y):
    modelo = LogisticRegression()
    modelo.fit(X, y)
    return modelo


def prever_modelo(modelo, alimento):
    entrada = [[
        alimento["cor"],
        alimento["cheiro"],
        alimento["sabor"],
        alimento["temperatura"],
        alimento["textura"]
    ]]

    resultado = modelo.predict(entrada)[0]

    if resultado == 1:
        return "👍 Vai gostar"
    elif resultado == -1:
        return "👎 Não vai gostar"
    else:
        return "😐 Neutro"