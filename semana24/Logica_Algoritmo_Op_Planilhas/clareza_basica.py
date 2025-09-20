# Princípio: Clareza básica, mas ainda sem otimização visual.

import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
dados = {
    "Rede Social": ["Facebook", "Instagram", "Telegram", "TikTok", "WhatsApp"],
    "Contagem": [4, 14, 3, 6, 10]
}
df = pd.DataFrame(dados)

# Gráfico de barras simples
plt.bar(df["Rede Social"], df["Contagem"])
plt.title("Uso de Redes Sociais")
plt.show()


