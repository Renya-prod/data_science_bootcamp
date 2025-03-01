#!/usr/bin/env python3
import timeit
import random
from collections import Counter

random_numbers = [random.randint(0, 100) for _ in range(1000000)]

def count_with_dict(numbers):
    """ Считает вхождения чисел (без Counter) """
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts

def top_10_with_dict(numbers):
    """ Возвращает топ-10 чисел (без Counter) """
    counts = count_with_dict(numbers)
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

def count_with_counter(numbers):
    """ Считает вхождения чисел (с Counter) """
    return Counter(numbers)

def top_10_with_counter(numbers):
    """ Возвращает топ-10 чисел (с Counter) """
    counter = Counter(numbers)
    return counter.most_common(10)

def benchmark():
    """ Выводит результаты """
    dict_count_time = timeit.timeit(lambda: count_with_dict(random_numbers), number=1)
    counter_count_time = timeit.timeit(lambda: count_with_counter(random_numbers), number=1)
    
    dict_top_time = timeit.timeit(lambda: top_10_with_dict(random_numbers), number=1)
    counter_top_time = timeit.timeit(lambda: top_10_with_counter(random_numbers), number=1)
    
    print(f"My function count: {dict_count_time:.7f}")
    print(f"Counter: {counter_count_time:.7f}")
    print(f"My top: {dict_top_time:.7f}")
    print(f"Counter's top: {counter_top_time:.7f}")

if __name__ == "__main__":
    benchmark()
