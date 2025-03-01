def convert_csv_to_tsv(input_file, output_file):
    try:
        with open(input_file, mode='r') as csv_file, open(output_file, mode='w') as tsv_file:
            counter = 0
            while True:
                ch = csv_file.read(1)
                if not ch:
                    break
                if ch == '"':
                    counter +=1
                    tsv_file.write(ch)
                elif (ch == ',') and (counter % 2 == 0):
                    tsv_file.write('\t')
                else:
                    tsv_file.write(ch)
    except FileNotFoundError:
        print(f"Error: file {input_file} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    input_csv = "ds.csv"
    output_tsv = "ds.tsv"
    convert_csv_to_tsv(input_csv, output_tsv)