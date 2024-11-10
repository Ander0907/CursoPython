def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(numero):
    return [n for n in range(0, numero + 1) if es_primo(n)]

print(contar_primos(30))