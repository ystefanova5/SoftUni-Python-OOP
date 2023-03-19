from itertools import permutations


def possible_permutations(collection: list):
    result = permutations(collection)

    for permutation in result:
        yield list(permutation)
