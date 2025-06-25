import joblib
import numpy as np

model = joblib.load("../model/modelo_atraso.pkl")

def prever_atraso(estimativa_horas, tipo, prioridade):
    tipo_bug = 1 if tipo == "bug" else 0
    tipo_melhoria = 1 if tipo == "melhoria" else 0
    tipo_feature = 1 if tipo == "feature" else 0
    prioridade_baixa = 1 if prioridade == "baixa" else 0
    prioridade_média = 1 if prioridade == "média" else 0
    prioridade_alta = 1 if prioridade == "alta" else 0

    entrada = np.array([[
        estimativa_horas,
        tipo_bug, tipo_melhoria, tipo_feature,
        prioridade_baixa, prioridade_média, prioridade_alta
    ]])

    return model.predict(entrada)[0]

# prever_atraso(10, 14, "bug", "alta")
