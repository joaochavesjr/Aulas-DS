# Princípio: Clareza básica, mas ainda sem otimização visual.

import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
dados = {
    "Rede Social": ["Facebook", "Instagram", "Telegram", "TikTok", "WhatsApp"],
    "Contagem": [4, 14, 3, 6, 10]
}
df = pd.DataFrame(dados)
df_sorted = df.sort_values("Contagem", ascending=False)

# Gráfico de barras simples
bars = plt.bar(df_sorted["Rede Social"], df_sorted["Contagem"], color="purple")
plt.title("Uso de Redes Sociais (Com Rótulos)")
plt.xlabel("Plataformas")
plt.ylabel("Contagem")

# Adicionando os valores acima das barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval), ha='center', va='bottom')

plt.show()
