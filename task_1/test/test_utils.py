CONTENT_FILENAME = 'resources/content.py'
RESULT_SINGLE_FILENAME = 'resources/result_single.md'
RESULT_SINGLE_EXISTING_FILENAME = 'resources/result_single_existing.md'
RESULT_CONCAT_FILENAME = 'resources/result_concat.md'
TEST_RESULT_FILENAME = 'resources/test_result.md'


def get_file_data(filename):
    with open(filename) as f:
        return f.read()


def clear_test_result():
    write_to_test_result('')


def write_to_test_result(text):
    with open(TEST_RESULT_FILENAME, 'w') as f:
        f.write(text)


def get_md_titles():
    return 'Any title', 'Any description'


def get_source_code():
    return '''def body():
    pass'''
