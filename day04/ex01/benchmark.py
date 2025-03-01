#!/usr/bin/env python3
import timeit

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

def benchmark():
    """ Запускает сравнительный анализ и выводит результаты """
    number_runs = 900000
    emails = create_email_list()
    loop_time = timeit.timeit(lambda: get_gmails_with_loop(emails), number=number_runs)
    comprehension_time = timeit.timeit(lambda: get_gmails_with_comprehension(emails), number=number_runs)
    map_time = timeit.timeit(lambda: get_gmails_with_map(emails), number=number_runs)

    if map_time <= comprehension_time and map_time <= loop_time:
        print("it is better to use a map")
    elif comprehension_time <= loop_time:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")

    times = sorted([("map", map_time), ("list comprehension", comprehension_time), ("loop", loop_time)])
    for method, time in times:
        print(f"{method} is {time:.6f}")

if __name__ == "__main__":
    benchmark()