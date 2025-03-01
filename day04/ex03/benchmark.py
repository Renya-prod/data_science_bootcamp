#!/usr/bin/env python3
import timeit
import sys
from functools import reduce

def sum_of_squares_with_loop(n):
    """ Вычисляет квадрат каждого числа и добавляет его к общей сумме """
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def sum_of_squares_with_reduce(n):
    """ Вычисляет последовательное накопления суммы квадратов """
    return reduce(lambda acc, x: acc + x * x, range(1, n + 1))

def benchmark(func_name, iterations, n):
    """ Запускает указанный в аргументе метод и выводит результаты """
    functions = {
        "loop": lambda: sum_of_squares_with_loop(n),
        "reduce": lambda: sum_of_squares_with_reduce(n),
    }
    
    if func_name not in functions:
        print(f"Error: Function '{func_name}' is not recognized.")
        print("Available options: loop, reduce")
        return
    
    execution_time = timeit.timeit(functions[func_name], number=iterations)
    print(f"{func_name}: {execution_time:.9f}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 benchmark.py <function_name> <iterations> <number>")
        print("Available function names: loop, reduce")
    else:
        func_name = sys.argv[1]
        try:
            iterations = int(sys.argv[2])
            n = int(sys.argv[3])
            benchmark(func_name, iterations, n)
        except ValueError:
            print("Error: <iterations> and <number> must be integers.")
