# Cores opostas no círculo cromático → alto contraste e destaque.
# Bom para chamar atenção para os valores extremos.
# Princípio: Contraste para evidenciar diferenças ou destaques.

import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
dados = {
    "Rede Social": ["Facebook", "Instagram", "Telegram", "TikTok", "WhatsApp"],
    "Contagem": [4, 14, 3, 6, 10]
}
df = pd.DataFrame(dados).sort_values("Contagem", ascending=False)

# Cores complementares (laranja e verde)
colors = ["#FF5722", "#4CAF50", "#FF5722", "#4CAF50", "#FF5722"]

plt.bar(df["Rede Social"], df["Contagem"], color=colors, edgecolor="black")
plt.title("Uso de Redes Sociais (Cores Complementares)")
plt.xlabel("Plataformas")
plt.ylabel("Contagem")
plt.show()