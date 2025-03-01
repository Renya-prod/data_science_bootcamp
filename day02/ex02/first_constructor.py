import sys
import os

class Research():
    file_path = None
    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        self.file_path = file_path
    
    def file_reader(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
        except Exception as e:
            raise RuntimeError(f"Error reading the file: {e}")

        if len(lines) < 2:
            raise ValueError("File must contain a header and at least one line of data.")
        
        header = lines[0].strip()
        if ',' not in header or len(header.split(',')) != 2:
            raise ValueError("Header must contain exactly two strings delimited by a comma.")

        for line in lines[1:]:
            line = line.strip()
            if line not in {"0,1", "1,0"}:
                raise ValueError("Each data line must be either '0,1' or '1,0'.")

        return ''.join(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        research = Research(file_path)
        print(research.file_reader())
    except Exception as e:
        print(f"Error: {e}")

    