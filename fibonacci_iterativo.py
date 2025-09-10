import time


def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    start = time.time()
    print(fibonacci_iterativo(int(input())))
    end = time.time()
    print("Tempo de execução:", end - start)
