start_file_name = 'compress.py'
final_file_name = 'string.md'


def main():
    start_file = open(start_file_name)
    content = start_file.read()
    start_file.close()

    content = content.split('# ---end---')
    title = description = None

    for line in content[0].split('\n'):
        if line.startswith('# title'):
            title = line.replace('# title ', '')
        elif line.startswith('# description'):
            description = line.replace('# description ', '')

    format = ['+ [{}](#{})\n\n## {}\n\n'.format(title, '-'.join(title.lower().split()), title),
                  description, '\n```python', content[1].split('\n', 1)[1], '\n```']

    final_file = open(final_file_name, 'w')
    for el in format:
        final_file.write(el)


if __name__ == "__main__":
    main()
