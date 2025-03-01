import sys

def names_extractor(input_file):
    with open(input_file, mode = 'r') as input_txt, open('employees.tsv', mode = 'a') as output_tsv:
        lines = input_txt.readlines()
        output_tsv.write("Name\tSurname\tE-mail\n")
        for email in lines:
            email = email.strip()
            part1, rest = email.split('.', 1)
            part2, part3 = rest.split('@', 1)
            tsv_line = f"{part1.capitalize()}\t{part2.capitalize()}\t{email}"
            output_tsv.write(tsv_line + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error, example of using: python names_extractor.py <file.txt>")
        sys.exit(1)

    email_file_path = sys.argv[1]
    names_extractor(email_file_path)
    print("Script executed successfully")