import time


def fibonacci_recurssivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recurssivo(n - 1) + fibonacci_recurssivo(n - 2)


if __name__ == "__main__":
    start = time.time()
    print(fibonacci_recurssivo(int(input())))
    end = time.time()
print("Tempo de execução:", end - start)
