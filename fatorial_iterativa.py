import time


def fatorial_interativo(n):
    fatorial = 1

    for i in range(1, n + 1):
        fatorial = fatorial * i

    return fatorial


if __name__ == "__main__":
    start = time.time()
    print(fatorial_interativo(int(input())))
    end = time.time()
    print("Tempo de execução:", end - start)
