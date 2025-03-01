import sys
import os

class Research:
    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        self.file_path = file_path

    def file_reader(self, has_header=True):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
        except Exception as e:
            raise RuntimeError(f"Error reading the file: {e}.")
        
        if len(lines) < 1:
            raise ValueError("File must contain at least one line of data.")

        if has_header:
            header = lines[0].strip()
            if ',' not in header or len(header.split(',')) != 2:
                raise ValueError("Header must contain exactly two strings.")
            lines = lines[1:]
        
        data = []
        for line in lines:
            line = line.strip()
            if line not in {"0,1", "1,0"}:
                raise ValueError("Each data line must be either '0,1' or '1,0'.")
            data.append(list(map(int, line.split(','))))

        return data
    
    class Calculations:
        @staticmethod
        def counts(data):
            heads = sum(row[0] for row in data)
            tails = sum(row[1] for row in data)
            return heads, tails
        @staticmethod
        def fractions(heads, tails):
            total = heads + tails
            if total == 0:
                return 0, 0
            return (heads / total) * 100, (tails / total) * 100

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Useage: python3 first_nest.py file.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        research = Research(file_path)
        data = research.file_reader(has_header=True)
        print(data)

        calculations = Research.Calculations()
        heads, tails = calculations.counts(data)
        print(heads, tails)

        head_frac, tail_frac = calculations.fractions(heads, tails)
        print(head_frac, tail_frac)
    except Exception as e:
        print(f"Error: {e}.")