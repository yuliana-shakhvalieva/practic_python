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
        self.title = self.data.pop(0).strip().split(',')

    def convert(self):
        result = [self.convert_row_to_pretty_json(dict(zip(self.title, row.strip().split(',')))) for row in self.data]
        return "[{}]".format(", ".join(result))

    def convert_row_to_pretty_json(self, data):
        formatted_values = ", ".join(["""{}: {}""".format(key, value) for key, value in data.items()])
        return """{{{}}}""".format(formatted_values)


def main():
    reader = FileReader('input.csv')
    data = reader.read_data()
    if not data:
        print('File is empty.')
        return
    converter = CsvToJsonConverter(data)
    result = converter.convert()
    writer = FileWriter('output.json')
    writer.write_data(result)


if __name__ == "__main__":
    main()
