class FileReader:

    def __init__(self, input_file):
        self.input_file = input_file

    def read_data(self):
        file = open(self.input_file)
        content = file.readlines()
        file.close()
        return content


class FileWriter:

    def __init__(self, output_file):
        self.output_file = output_file

    def write_data(self, data):
        file = open(self.output_file, 'w')
        file.write(data)
        file.close()


class CsvToJsonConverter:

    def __init__(self, data):
        self.data = data
        self.title = None
        self.prepare_data()

    def convert(self):
        result = [self.convert_row_to_pretty_json(row) for row in self.data]
        return str(result)

    def prepare_data(self):
        self.title = self.data.pop(0).strip().split(',')

    def convert_row_to_pretty_json(self, row):
        values = row.strip().split(',')
        dict(zip(self.title, values))

        pretty_row = """{{
        "id": {},
        "name": {},
        "birth": {},
        "salary": {},
        "department": {}\n}}""".format(*values)

        return pretty_row


def main():
    reader = FileReader('input.csv')
    data = reader.read_data()
    converter = CsvToJsonConverter(data)
    result = converter.convert()
    writer = FileWriter('output.json')
    writer.write_data(result)


if __name__ == "__main__":
    main()
