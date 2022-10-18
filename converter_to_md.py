from os.path import exists


INPUT_CODE_DELIMITER = '# ---end----'


def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def write_to_md(file_name, data):
    if exists(file_name):
        data = change_data(file_name, data)
    write_data(file_name, data)


def change_data(file_name, new_content):
    exist_content = read_data(file_name)
    return md_concat(exist_content, new_content)


def md_concat(exist_content, new_content):
    str_list = exist_content.split('\n')
    new_link = new_content.split('\n')[0]

    for index, line in enumerate(str_list):
        if not line.startswith('+ ['):
            str_list.insert(index, new_link)
            return '\n'.join(str_list) + '\n' + new_content[len(new_link) + 1:]


def prepare_md_titles(data):
    title, description = None, None

    for line in data.split('\n'):
        if line.startswith('# title'):
            title = line.replace('# title ', '')
        elif line.startswith('# description'):
            description = line.replace('# description ', '')

    return title, description


def prepare_md_format(title, description, source_code):
    md_link = '-'.join(title.lower().split())

    template = """+ [{}](#{})

    ## {}

    {}

    ```python
    {}
    ```"""

    return template.format(title, md_link, title, description, source_code.lstrip())


def convert_data(data):
    titles, source_code = data.split(INPUT_CODE_DELIMITER)
    title, description = prepare_md_titles(titles)
    result_md = prepare_md_format(title, description, source_code)
    return result_md


def main():
    content = read_data('diagonal_sum.py')
    result = convert_data(content)
    write_to_md('matrix.md', result)


if __name__ == "__main__":
    main()

