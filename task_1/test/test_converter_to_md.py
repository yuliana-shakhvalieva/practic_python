import unittest
import converter_to_md as cv
import test_utils as ut


class TestConverterToMd(unittest.TestCase):

    def test_read_data(self):
        expected = ut.get_file_data(ut.CONTENT_FILENAME)

        actual = cv.read_data(ut.CONTENT_FILENAME)

        self.assertEqual(expected, actual)

    def test_convert_data(self):
        test_content = ut.get_file_data(ut.CONTENT_FILENAME)
        expected = ut.get_file_data(ut.RESULT_SINGLE_FILENAME)

        actual = cv.convert_data(test_content)

        self.assertEqual(expected, actual)

    def test_prepare_md_titles(self):
        test_content = ut.get_file_data(ut.CONTENT_FILENAME)
        expected = ut.get_md_titles()

        actual = cv.prepare_md_titles(test_content)

        self.assertEqual(expected, actual)

    def test_prepare_md_format(self):
        source_code = ut.get_source_code()
        title, description = ut.get_md_titles()
        expected = ut.get_file_data(ut.RESULT_SINGLE_FILENAME)

        actual = cv.prepare_md_format(title, description, source_code)

        self.assertEqual(expected, actual)

    def test_write_to_md_when_nothing_exists(self):
        ut.clear_test_result()
        data = ut.get_file_data(ut.RESULT_SINGLE_FILENAME)
        try:
            cv.write_to_md(ut.TEST_RESULT_FILENAME, data)

            self.assertEqual(data, ut.get_file_data(ut.TEST_RESULT_FILENAME))
        finally:
            ut.clear_test_result()

    def test_write_to_md_when_content_exists(self):
        existing_text = ut.get_file_data(ut.RESULT_SINGLE_EXISTING_FILENAME)
        ut.write_to_test_result(existing_text)
        data = ut.get_file_data(ut.RESULT_SINGLE_FILENAME)
        try:
            cv.write_to_md(ut.TEST_RESULT_FILENAME, data)

            self.assertEqual(ut.get_file_data(ut.RESULT_CONCAT_FILENAME), ut.get_file_data(ut.TEST_RESULT_FILENAME))
        finally:
            ut.clear_test_result()

    def test_md_concat(self):
        existing_text = ut.get_file_data(ut.RESULT_SINGLE_EXISTING_FILENAME)
        data = ut.get_file_data(ut.RESULT_SINGLE_FILENAME)

        result = cv.md_concat(existing_text, data)

        self.assertEqual(ut.get_file_data(ut.RESULT_CONCAT_FILENAME), result)

    def test_change_data(self):
        data = ut.get_file_data(ut.RESULT_SINGLE_FILENAME)

        result = cv.change_data(ut.RESULT_SINGLE_EXISTING_FILENAME, data)

        self.assertEqual(ut.get_file_data(ut.RESULT_CONCAT_FILENAME), result)


if __name__ == "__main__":
    TestConverterToMd()
