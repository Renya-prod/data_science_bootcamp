#!/usr/local/bin/python3.12

import os

def main():
    venv_name = os.getenv('VIRTUAL_ENV')
    if venv_name:
        print(f"Your current virtual env is {venv_name}")
    else:
        print("No virtual environment is currently activated")

if __name__ == "__main__":
    main()
