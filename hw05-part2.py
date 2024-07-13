import re
from typing import Callable


# функція аналізує текст, ідентифікує всі дійсні числа і повертати їх як генератор. 
def generator_numbers(text: str):
    numbers =  re.findall(r'\d+\.\d+', text)
    numbers = list(map(float, numbers))
    for i in range (len(numbers)):
        yield numbers[i]

# функція використовує generator_numbers для підсумовування чисел і повертає їх загальну суму.
def sum_profit(text: str, func: Callable):
    gen = func(text)
    total_sum = 0
    while True:
        try:
            total_sum += next(gen)
        except:
            return(total_sum)



if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
