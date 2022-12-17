import unittest
from csv_to_json_manual import CsvToJsonConverter


class TestConverterCsvToJson(unittest.TestCase):

    def test_init(self):
        data = ['id,name,birth,salary,department\n', '1,Ivan,1980,150000,1\n', '2,Alex,1960,200000,5\n', '3,Ivan,,'
                                                                                                         '130000,8']
        title = ['id', 'name', 'birth', 'salary', 'department']
        cv = CsvToJsonConverter(data)

        self.assertEqual(data, cv.data)
        self.assertEqual(title, cv.title)

    def test_convert(self):
        data = ['id,name,birth,salary,department\n', '1,Ivan,1980,150000,1\n', '2,Alex,1960,200000,5\n',
                '3,Ivan,,130000,8']
        cv = CsvToJsonConverter(data)
        expected = '[{id: 1, name: Ivan, birth: 1980, salary: 150000, department: 1}, {id: 2, name: Alex, ' \
                   'birth: 1960, salary: 200000, department: 5}, {id: 3, name: Ivan, birth: , salary: 130000, ' \
                   'department: 8}] '

        actual = cv.convert()

        self.assertEqual(expected, actual)

    def test_convert_row_to_pretty_json(self):
        data = ['id,name,birth,salary,department\n', '1,Ivan,1980,150000,1\n', '2,Alex,1960,200000,5\n',
                '3,Ivan,,130000,8']
        cv = CsvToJsonConverter(data)
        expected = '{id: 1, name: Ivan, birth: 1980, salary: 150000, department: 1}'

        actual = cv.convert_row_to_pretty_json({'id': '1', 'name': 'Ivan', 'birth': '1980', 'salary': '150000', 'department': '1'})

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    TestConverterCsvToJson()
