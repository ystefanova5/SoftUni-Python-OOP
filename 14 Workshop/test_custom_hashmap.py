from unittest import TestCase, main
from custom_hashmap import HashTable


class TestCustomHashTable(TestCase):

    def setUp(self) -> None:
        self.table = HashTable()

    def test_init(self):
        assert self.table._HashTable__max_capacity == 4
        assert self.table._HashTable__keys == [None] * 4
        assert self.table._HashTable__values == [None] * 4

    def test__get__item_valid_key(self):
        self.table["name"] = "Peter"
        assert self.table["name"] == "Peter"

    def test__get__item__invalid_key_raises(self):
        with self.assertRaises(KeyError) as ke:
            result = self.table["invalid"]

        expected_message = "'invalid is not a valid key!'"
        self.assertEqual(expected_message, str(ke.exception))

    def test_value_is_updated_for_existing_key(self):
        self.table["name"] = "Peter"
        self.table["name"] = "Thomas"
        assert self.table["name"] == "Thomas"

    def test_reaching_max_capacity_resizes_array(self):
        self.table["name"] = "Peter"
        self.table["age"] = 20
        self.table["student"] = "Yes"
        self.table["active"] = "Yes"

        self.assertEqual(4, len(self.table._HashTable__keys))
        self.assertEqual(4, len(self.table._HashTable__values))

        self.table["is_married"] = "No"
        self.assertEqual(8, len(self.table._HashTable__keys))
        self.assertEqual(8, len(self.table._HashTable__values))

    def test_calc_index(self):
        pass

    # TODO
    # Write additional tests


if __name__ == "__main__":
    main()