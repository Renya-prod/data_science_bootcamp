#!/usr/bin/env python3
import sys
import resource
import time

def read_all_lines(file_path):
    """ Читает весь файл и загружает его в память """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 ordinary.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.process_time()
    start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024 /1024

    lines = read_all_lines(file_path)
    for line in lines:
        pass

    end_time = time.process_time()
    end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024 /1024

    print(f"Peak Memory Usage = {end_memory - start_memory:.3f} Gb")
    print(f"User Mode Time + System Mode Time = {end_time - start_time:.2f}s")
