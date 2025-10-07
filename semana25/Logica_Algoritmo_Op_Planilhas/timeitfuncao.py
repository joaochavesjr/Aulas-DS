import timeit

# Defina sua função
def minha_funcao():
    soma = 0
    for i in range(1000):
        soma += i
    return soma

# Configure o ambiente e o código principal
# `setup` é executado uma vez para configurar o ambiente (importar a função)
# `stmt` é o código principal a ser medido (chamar a função)
setup_code = "from __main__ import minha_funcao"
statement_code = "minha_funcao()"

# Crie um objeto Timer
timer = timeit.Timer(stmt=statement_code, setup=setup_code)

# Execute o timer para medir o tempo
# O parâmetro `number` define quantas vezes o `statement_code` será executado
tempo_execucao = timer.timeit(number=1000)

print(f"O tempo de execução da função foi de: {tempo_execucao} segundos")
