from contextlib import contextmanager

@contextmanager
def file_opener(file_path: str, mode: str):
    file = open(file_path, mode)
    try:
        yield file
    finally:
        file.close()

def process(data: str):
    modified_data = []
    for line in data:
        sentences = line.split('.')
        modified_data.extend(sentences)
    return modified_data

input_file_path = input("Enter input file path: ")
output_file_path = input("Enter output file path: ")

with file_opener(input_file_path, 'r') as handle:
    data = handle.readlines()
    modified_data = process(data)

with file_opener(output_file_path, 'w') as p:
    p.writelines(modified_data)
