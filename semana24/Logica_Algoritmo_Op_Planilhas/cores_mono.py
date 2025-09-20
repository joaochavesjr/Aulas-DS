# Transmitem simplicidade e coesão visual.
# Boa para quando o objetivo é só mostrar intensidade ou 
# valores sem confundir o leitor.
# Princípio: Tons mais claros = menor valor, tons mais escuros = maior valor.
import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
dados = {
    "Rede Social": ["Facebook", "Instagram", "Telegram", "TikTok", "WhatsApp"],
    "Contagem": [4, 14, 3, 6, 10]
}
df = pd.DataFrame(dados).sort_values("Contagem", ascending=False)

# Paleta monocromática (tons de azul)
colors = plt.cm.Blues([0.4, 0.5, 0.6, 0.7, 0.8])

plt.bar(df["Rede Social"], df["Contagem"], color=colors, edgecolor="black")
plt.title("Uso de Redes Sociais (Monocromático)")
plt.xlabel("Plataformas")
plt.ylabel("Contagem")
plt.show()