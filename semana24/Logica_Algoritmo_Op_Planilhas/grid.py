# Princípio: Clareza básica, mas ainda sem otimização visual.

import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
dados = {
    "Rede Social": ["Facebook", "Instagram", "Telegram", "TikTok", "WhatsApp"],
    "Contagem": [4, 14, 3, 6, 10]
}
df = pd.DataFrame(dados)

# Princípio: Ordenação ajuda na comparação visual.
df_sorted = df.sort_values("Contagem", ascending=False)

plt.bar(df_sorted["Rede Social"], df_sorted["Contagem"], color="green")
plt.title("Uso de Redes Sociais (Design Limpo)")
plt.xlabel("Plataformas")
plt.ylabel("Contagem")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()