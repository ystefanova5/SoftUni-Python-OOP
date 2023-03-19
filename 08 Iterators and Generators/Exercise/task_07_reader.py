def read_next(*args):
    index = 0

    while index < len(args):
        for item in args[index]:
            yield item
        index += 1
