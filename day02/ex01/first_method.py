class Research:
    def file_reader(self):
        with open('../data.csv', 'r') as file:
            file_out = file.read()
        return file_out

if __name__ == "__main__":
    print(Research().file_reader())