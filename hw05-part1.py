# функція створює та використовує кеш 
# для зберігання і повторного використання 
# вже обчислених значень чисел Фібоначчі.

def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        nonlocal cache
        if n in cache:
            return cache[n]
        if n <= 0:
            cache[0] = 0
        elif n == 1:
            cache[1] = 1
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci



if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(15))
