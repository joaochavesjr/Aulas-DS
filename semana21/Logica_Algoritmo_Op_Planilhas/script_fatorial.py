def fatorial(n):
    if n == 1:
        fat = 1
    else:
        fat = n * fatorial(n-1)
    
    print("calculo do fatorial", fat)
    return fat

print("resultado", fatorial(6))