with Indenter() as indent:
    indent.print('Hi')
    with indent:
        indent.print('Talk is cheap!')
        with indent:
            indent.print('Show me the code...')
    indent.print('Torvalds')