import sys

def searcher_name(email):
    try:
        with open('employees.tsv', 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:
                name, surname, dotcom = line.strip().split('\t')
                if dotcom == email:
                    return name
    except FileNotFoundError:
        print("File employees.tsv not found.")
        return None

def main(email):
    name = searcher_name(email)
    if name:
        print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
    else:
        print("Error. Email adress is wrong.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error, example of using: letter_starter.py <email>")
        sys.exit(1)

    email = sys.argv[1]
    main(email)