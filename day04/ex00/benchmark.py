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

def benchmark():
    """ Запускает сравнительный анализ и выводит результаты """
    number_runs = 900000 
    emails = create_email_list()
    loop_time = timeit.timeit(lambda: get_gmails_with_loop(emails), number=number_runs)
    comprehension_time = timeit.timeit(lambda: get_gmails_with_comprehension(emails), number=number_runs)

    if comprehension_time <= loop_time:
        print("It is better to use a list comprehension")
    else:
        print("It is better to use a loop")

    print(f"{comprehension_time:.6f} vs {loop_time:.6f}")

if __name__ == "__main__":
    benchmark()