def prever_heuristica(alimento):
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