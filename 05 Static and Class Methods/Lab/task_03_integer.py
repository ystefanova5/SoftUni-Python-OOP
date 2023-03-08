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

        result = 0
        for idx in range(len(value)):
            current_letter = value[idx]
            previous_letter = value[idx - 1]

            if idx != 0 and roman_letters[current_letter] > roman_letters[previous_letter]:
                result += roman_letters[current_letter] - (roman_letters[previous_letter] * 2)
            else:
                result += roman_letters[current_letter]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(float(value)))
