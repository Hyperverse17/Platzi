
def fibo():
    a, b, counter = 1, 1, 0
    while True:
        counter += 1
        if counter < 3:
            c = 1
        else :
            c = a + b
            a = b
            b = c
        yield c

serie = fibo()

for _ in range(1,11):
    print(next(serie))