# Cores vizinhas no círculo cromático → harmonia e suavidade.
# Ex.: Verde, azul e ciano transmitem tranquilidade.
# Princípio: Boa para mostrar dados relacionados sem gerar conflito visual.
import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
dados = {
    "Rede Social": ["Facebook", "Instagram", "Telegram", "TikTok", "WhatsApp"],
    "Contagem": [4, 14, 3, 6, 10]
}
df = pd.DataFrame(dados).sort_values("Contagem", ascending=False)

# Paleta monocromática (tons de azul)
colors = ["#4CAF50", "#2196F3", "#00BCD4", "#8BC34A", "#03A9F4"]

plt.bar(df["Rede Social"], df["Contagem"], color=colors, edgecolor="black")
plt.title("Uso de Redes Sociais (Cores Análogas)")
plt.xlabel("Plataformas")
plt.ylabel("Contagem")
plt.show()