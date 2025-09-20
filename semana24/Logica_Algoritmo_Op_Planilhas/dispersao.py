import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Gerando dados fictícios
np.random.seed(42)
notas_matematica = np.random.randint(50, 100, 20)
notas_ciencias = notas_matematica + np.random.randint(-10, 10, 20)

# Criando DataFrame
df = pd.DataFrame({
    "Matemática": notas_matematica,
    "Ciências": notas_ciencias
})

# Criando gráfico de dispersão
plt.figure(figsize=(7, 5))
plt.scatter(df["Matemática"], df["Ciências"], s=70, alpha=0.7, edgecolor='k')
plt.title("Relação entre notas de Matemática e Ciências")
plt.xlabel("Notas de Matemática")
plt.ylabel("Notas de Ciências")
plt.grid(True)
plt.show()