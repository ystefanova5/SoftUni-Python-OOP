class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = []

        for index, letter in enumerate(value):
            letter_value = roman_letters[letter]

            if index == 0:
                result.append(letter_value)
                continue

            if index != len(value) - 1:
                next_letter_value = roman_letters[value[index + 1]]
                if next_letter_value > letter_value:
                    letter_value *= -1

            result.append(letter_value)

        return cls(sum(result))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(float(value)))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("CXIV")
print(second_num.value)
