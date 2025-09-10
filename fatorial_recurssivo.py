import time


def fatorial_recurssivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recurssivo(n - 1)


if __name__ == "__main__":
    start = time.time()
    print(fatorial_recurssivo(int(input())))
    end = time.time()
    print("Tempo de execução:", end - start)
