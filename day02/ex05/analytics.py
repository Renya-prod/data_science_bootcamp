import os
from random import randint

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
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            if total == 0:
                return 0, 0
            return (heads / total) * 100, (tails / total) * 100

    class Analytics(Calculations):
        def predict_random(self, steps):
            predictions = []
            for _ in range(steps):
                if randint(0, 1) == 0:
                    predictions.append([0, 1])
                else:
                    predictions.append([1, 0])
            return predictions

        def predict_last(self):
            if not self.data:
                raise ValueError("No data available to predict the last observation.")
            return self.data[-1]

        def save_file(self, data, file_name, extension='txt'):
            file_path = f"{file_name}.{extension}"
            try:
                with open(file_path, 'w') as file:
                    file.write(data)
            except Exception as e:
                raise RuntimeError(f"Error saving file: {e}")