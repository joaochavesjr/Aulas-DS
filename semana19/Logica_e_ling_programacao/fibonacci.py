def fibonacci(n):
    """
    Calcula o n-ésimo número de Fibonacci usando um loop (iterativo).
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        print("Antes valor de b", b, 'Valor de a+b', a+b)
        a, b = b, a + b
        print("Depois, valor de a", a,'Valor de b', b)

    return b

while 1:
    numero = input('Numero:')
    try:
        print(fibonacci(int(numero)))
    except:
        print(f'{numero} e invalido')
