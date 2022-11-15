import csv
import json


class FileReader:

    def __init__(self, input_file):
        self.file = open(input_file)

    def close(self):
        self.file.close()


class FileWriter:

    def __init__(self, output_file):
        self.output_file = output_file

    def write_data(self, data):
        file = open(self.output_file, 'w')
        file.write(data)
        file.close()


class CsvToJsonConverter:

    def convert(self, file_reader: FileReader) -> str:
        data_csv = csv.DictReader(file_reader.file)
        data_json = [json.dumps(d, indent=4) for d in data_csv]
        return str(data_json)


def main():

    reader = FileReader('input.csv')
    converter = CsvToJsonConverter()
    data = converter.convert(reader)
    reader.close()
    writer = FileWriter('output.json')
    writer.write_data(data)


if __name__ == "__main__":
    main()
