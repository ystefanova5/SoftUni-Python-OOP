def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []

        for num in range(n):
            result.append(next(seq))

        return result

    return (take, halves, integers)
