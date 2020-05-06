import csv


class reader:
    input_file = dict()

    # Construtor for File Reader
    def file_reader(self):
        self.input_file = csv.DictReader(open("products.csv"))
        return self.input_file
