# Cada categoria com uma cor única → ideal para comparação clara entre grupos.
# Princípio: Facilita a distinção entre categorias sem confusão visual.

import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
dados = {
    "Rede Social": ["Facebook", "Instagram", "Telegram", "TikTok", "WhatsApp"],
    "Contagem": [4, 14, 3, 6, 10]
}
df = pd.DataFrame(dados).sort_values("Contagem", ascending=False)

colors = plt.cm.Set2(range(len(df)))

plt.bar(df["Rede Social"], df["Contagem"], color=colors, edgecolor="black")
plt.title("Uso de Redes Sociais (Paleta Categórica)")
plt.xlabel("Plataformas")
plt.ylabel("Contagem")
plt.show()