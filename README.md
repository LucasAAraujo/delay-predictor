# ⏳ IA para Previsão de Atraso em Tarefas 

Este projeto demonstra o uso de Machine Learning para prever, com base apenas em informações do backlog, se uma tarefa ágil tem alta chance de ser entregue com atraso.

---

## 💡 Objetivo

Desenvolver um modelo de IA capaz de prever o atraso de tarefas **antes de sua execução**, utilizando apenas:

- Estimativa de esforço (em horas)
- Tipo da tarefa (feature, bug ou melhoria)
- Prioridade (baixa, média ou alta)

---

## 🔍 Visão Geral

O sistema foi dividido em três partes principais:

1. **Geração e Treinamento do Modelo (`train.py`)**
2. **Predição com entrada do usuário (`predict.py`)**
3. **Interface interativa com Streamlit (`streamlit_app.py`)**

---

## 📊 Base de Dados Simulada

Para treinamento, foi utilizada uma base de 1000 tarefas simuladas (`tasks.csv`) com as seguintes colunas:

- `estimativa_horas`: Horas previstas para a tarefa
- `horas_reais`: Horas reais (geradas com ruído sobre a estimativa)
- `tipo`: feature, bug ou melhoria
- `prioridade`: baixa, média ou alta
- `foi_atrasada`: 1 se `horas_reais > estimativa`, 0 caso contrário

> Embora `horas_reais` seja usada na geração dos dados, **não é usada como input no modelo**, garantindo que a predição seja feita **antes da execução**.

---

## 🧠 Treinamento do Modelo

O modelo foi treinado usando `RandomForestClassifier`, com as seguintes features:

- `estimativa_horas`
- `tipo_bug`, `tipo_feature`, `tipo_melhoria` (dummies)
- `prioridade_baixa`, `prioridade_média`, `prioridade_alta` (dummies)

Após o treinamento, o modelo é salvo em `model/modelo_atraso.pkl`.

---

## 🔎 Predição (Sem Horas Reais)

A função `prever_atraso()` recebe:

- `estimativa_horas` (int)
- `tipo` (str)
- `prioridade` (str)

E retorna:

- `1`: se a IA prevê que a tarefa irá atrasar
- `0`: se a IA prevê que a tarefa será entregue no prazo

---

## 🖥 Interface com Streamlit

Execute com:

```bash
streamlit run streamlit_app.py
