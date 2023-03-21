def vowel_filter(function):
    vowels = "AOUEIYaoueiy"

    def wrapper():
        letters = function()
        return [x for x in letters if x in vowels]

    return wrapper
