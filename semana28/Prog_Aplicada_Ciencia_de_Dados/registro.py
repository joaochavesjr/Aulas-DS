# Tipos de gráficos que não foram utilizados na primeira aula: kde, hexbin

# Exemplos destes tipos de gráficos (kind)

#
# Exemplo utilizando o hexbin
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando um DataFrame com dados aleatórios
np.random.seed(0)
df = pd.DataFrame({
    'x': np.random.randn(1000),
    'y': np.random.randn(1000) + np.random.randn(1000) * 0.5
})

# Gerando o gráfico hexbin
df.plot(kind='hexbin', x='x', y='y', gridsize=25, cmap='viridis')

plt.title('Exemplo de gráfico hexbin')
plt.show()

#
# Exemplo utilizando o tipo kde
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando uma série de dados aleatórios
dados = pd.Series(np.random.randn(1000))

#print(dados)

# Gerando o gráfico de densidade
dados.plot(kind='kde', title='Gráfico de densidade')

plt.show()
