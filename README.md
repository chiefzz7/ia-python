# 🧠 IA de Recomendação Alimentar 

Este projeto tem como objetivo desenvolver um sistema inteligente capaz de **analisar o comportamento sensorial de pessoas** e **sugerir alimentos com maior probabilidade de aceitação**.

---

## 🚀 Tecnologias utilizadas

* Python
* scikit-learn
* JSON (dataset inicial)

---

## 📊 Como funciona

O sistema é dividido em duas abordagens:

### 🟢 Heurística (lógica manual)

Regras baseadas em pesos para cada atributo sensorial:

* cor
* cheiro
* sabor
* temperatura
* textura

👉 Gera uma previsão inicial baseada em score.

---

### 🔴 Inteligência Artificial (Machine Learning)

Um modelo de classificação é treinado com base nos dados:

* Entrada: atributos sensoriais
* Saída: reação da pessoa (`gostou`, `neutro`, `não gostou`)

O modelo aprende padrões e faz previsões automaticamente.

---

## 📁 Estrutura do projeto

```
.
├── dados.json        # Dataset inicial
├── main.py           # Execução principal
├── logica.py         # Heurística (regras manuais)
└── modelo.py         # Modelo de IA
```

---

## ⚙️ Como executar

### 1. Criar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Instalar dependências

```bash
pip install scikit-learn
```

---

### 3. Rodar o projeto

```bash
python main.py
```

---

## 📌 Exemplo de saída

```
🥦 Brócolis: 👎 Não vai gostar
🍌 Banana: 👍 Vai gostar
```

---

## 🧠 Objetivo do projeto

Criar um sistema de apoio para responsáveis, permitindo:

* identificar padrões sensoriais
* entender preferências alimentares
* sugerir alimentos com maior aceitação

---

## 🚀 Próximos passos

* Integrar com banco de dados (PostgreSQL / Supabase)
* Criar API com FastAPI
* Conectar com backend em Node.js
* Melhorar dataset com dados reais
* Implementar sistema de recomendação avançado

---

## 👨‍💻 Autor

Projeto desenvolvido para fins educacionais (TCC) com foco em Inteligência Artificial aplicada à saúde infantil.
