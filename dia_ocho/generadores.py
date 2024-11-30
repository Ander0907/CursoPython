def numeros_pares():
    num = 0
    while True:
        yield num
        num += 2

pares = numeros_pares()
for _ in range(10):
    print(next(pares))