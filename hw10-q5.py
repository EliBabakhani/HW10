class Indenter:
    def __init__(self):
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.level -= 1

    def print(self, text):
        print("    " * self.level + text)


with Indenter() as indent:
    indent.print('Hi')
    with indent:
        indent.print('Talk is cheap!')
        with indent:
            indent.print('Show me the code...')
    indent.print('Torvalds')
