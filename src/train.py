import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Carregar a nova base de dados simulada
df = pd.read_csv("../data/tasks.csv")

# Preprocessamento: gerar variáveis dummy para 'tipo' e 'prioridade'
# Se preferir, remova uma categoria (drop_first=True) para evitar multicolinearidade.
df_encoded = pd.get_dummies(df, columns=["tipo", "prioridade"], drop_first=False)

# Aqui, vamos treinar o modelo usando apenas as features que estarão disponíveis no momento de previsão.
# Ou seja, não usaremos "horas_reais". Usamos somente a "estimativa" e as dummies.
X = df_encoded[[
    'estimativa_horas',
    'tipo_bug', 'tipo_feature', 'tipo_melhoria',
    'prioridade_baixa', 'prioridade_média', 'prioridade_alta'
]]
y = df_encoded["foi_atrasada"]

# Separar treino e teste com estratificação
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Treinar modelo - usando RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Salvar o modelo treinado
joblib.dump(model, "../model/modelo_atraso.pkl")
