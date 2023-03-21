def vowel_filter(function):
    vowels = ["a", "o", "u", "i", "e", "y"]

    def wrapper():
        letters = function()
        return [x for x in letters if x in vowels]

    return wrapper
