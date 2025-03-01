#!/usr/bin/env python3
import sys
import resource
import time

def read_lines_generator(file_path):
    """ Читает файл построчно """
    with open(file_path, 'r') as file:
        for line in file:
            yield line

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generator.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.process_time()
    start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024

    for line in read_lines_generator(file_path):
        pass

    end_time = time.process_time()
    end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024

    print(f"Peak Memory Usage = {end_memory - start_memory:.3f} Mb")
    print(f"User Mode Time + System Mode Time = {end_time - start_time:.2f}s")
