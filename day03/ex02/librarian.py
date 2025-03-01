#!/usr/bin/env python3

import os
import subprocess

if __name__ == '__main__':
    try:
        res = os.environ.get("VIRTUAL_ENV")
        if not res or "monroeju" not in res:
            raise ValueError("Script must run in the 'monroeju' virtual environment")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(['pip', 'install', 'beautifulsoup4', 'pytest'], check=True)

        result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True, check=True)
        print(result.stdout)

        with open('requirements.txt', 'w') as f:
            f.write(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        exit(1)
