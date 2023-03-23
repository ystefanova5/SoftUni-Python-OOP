from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
    def test_01_class_initializes_correctly(self):
        mammal = Mammal("Leo", "lion", "roarrr")

        self.assertEqual("Leo", mammal.name)
        self.assertEqual("lion", mammal.type)
        self.assertEqual("roarrr", mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_02_make_sound_returns_message(self):
        mammal = Mammal("Leo", "lion", "roarrr")

        result = mammal.make_sound()
        self.assertEqual("Leo makes roarrr", result)

    def test_03_get_kingdom_returns_correct_data(self):
        mammal = Mammal("Leo", "lion", "roarrr")

        result = mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_04_info_returns_correct_message(self):
        mammal = Mammal("Leo", "lion", "roarrr")

        result = mammal.info()
        self.assertEqual("Leo is of type lion", result)


if __name__ == "__main__":
    main()
