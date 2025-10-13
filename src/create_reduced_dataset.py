import pandas as pd

# Cargar el dataset original
df = pd.read_csv("data/AI_Human.csv")

# Comprobar distribución
print(df["generated"].value_counts())

# Seleccionar una muestra balanceada
sample_size = 10000  # de cada clase
df_reduced = df.groupby("generated", group_keys=False).apply(lambda x: x.sample(sample_size, random_state=42))

# Guardar dataset reducido
df_reduced.to_csv("data/AI_Human_reduced.csv", index=False)

print("Dataset reducido guardado con forma:", df_reduced.shape)