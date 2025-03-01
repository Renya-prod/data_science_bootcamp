#!/usr/bin/env python3
import timeit
import sys

def create_email_list():
    """ Создает и возвращает список электронных адресов с дубликатами """
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
              'anna@live.com', 'philipp@gmail.com'] * 5
    return emails

def get_gmails_with_loop(email_list):
    """ Получает Gmail адреса используя цикл и append """
    gmail_adresses = []
    for email in email_list:
        if email.endswith('@gmail.com'):
            gmail_adresses.append(email)
    return gmail_adresses

def get_gmails_with_comprehension(email_list):
    """ Получает Gmail адреса используя list comprehension """
    return [email for email in email_list if email.endswith('@gmail.com')]

def extract_gmail(email):
    """ Функция для извлечения gmail адресов """
    return email if email.endswith('@gmail.com') else None

def get_gmails_with_map(email_list):
    """ Получает gmail адреса используя map """
    return list(filter(None, map(extract_gmail, email_list)))

def get_gmails_with_filter(email_list):
    return list(filter(lambda email: email.endswith('@gmail.com'), email_list))

def benchmark(func_name, iterations):
    """ Запускает указанный в аргументе метод и выводит результаты """
    emails = create_email_list()
    functions = {
        "loop": get_gmails_with_loop(emails),
        "list_comprehension": get_gmails_with_comprehension(emails),
        "map": get_gmails_with_map(emails),
        "filter": get_gmails_with_filter(emails),
    }
    
    if iterations <= 0:
        raise ValueError(f"Number of calls must be positive, got: {iterations}")

    if func_name not in functions:
        raise ValueError(f"Function '{func_name}' not found. Available functions: loop, list_comprehension, map, filter")
    
    execution_time = timeit.timeit(lambda: functions[func_name], number=iterations)

    # print(functions[func_name])
    print(f"{func_name}: {execution_time:.6f}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 benchmark.py <function_name> <iterations>")
        print("Available function names: loop, list_comprehension, map, filter")
    else:
        func_name = sys.argv[1]
        try:
            iterations = int(sys.argv[2])
            benchmark(func_name, iterations)
        except ValueError:
            print("Error: <iterations> must be an integer.")