def get_primes(integers: list):
    for number in integers:
        divisions = 0

        for num in range(2, number):
            if number % num == 0:
                divisions += 1

        if divisions == 0 and number >= 2:
            yield number
