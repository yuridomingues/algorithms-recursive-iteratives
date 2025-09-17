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


def fibonacci_top_down(n):
    if n == 1 or n == 0:
        return n
    
    try:
        return tabela[n]
    except:
        tabela[n] = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)
        return tabela[n]
        
def fibonacci_bottom_up(n):
    tabela = {}
    tabela[0] = 0
    tabela[1] = 1
    
    for i in range(2, n + 1):
        tabela[i] = tabela[i - 1] + tabela[i - 2]
    
if __name__ == "__main__":
    tabela = {}
    
    n = [0, 5, 10, 77, 1000]
    
    for i in range(len(n)):
        instancia = n[i]
        print(fibonacci_top_down(n = instancia))
