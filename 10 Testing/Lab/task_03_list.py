class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def test_class_initializes_correctly(self):
        int_list = IntegerList(10, "asd", 2.2, 4, 0)
        self.assertEqual([10, 4, 0], int_list._IntegerList__data)

        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)

    def test_add_method_with_correct_data_type(self):
        int_list = IntegerList(10, 4, 0)
        self.assertEqual([10, 4, 0], int_list._IntegerList__data)

        result = int_list.add(5)
        self.assertEqual([10, 4, 0, 5], result)

        result = int_list.add(-2)
        self.assertEqual([10, 4, 0, 5, -2], result)

    def test_add_method_with_incorrect_data_type_raises(self):
        int_list = IntegerList(10, 4, 0)
        self.assertEqual([10, 4, 0], int_list._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            int_list.add("A")
        [10, 4, 0], int_list._IntegerList__data
        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            int_list.add(2.5)

        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            int_list.add([2, 5])

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_with_valid_index(self):
        int_list = IntegerList(10, 4, 0)

        result = int_list.remove_index(0)

        self.assertEqual(10, result)
        self.assertEqual([4, 0], int_list._IntegerList__data)

    def test_remove_index_with_invalid_index_raises(self):
        int_list = IntegerList(10, 4, 0)

        with self.assertRaises(IndexError) as ex:
            int_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_returns_correct_element_with_valid_index(self):
        int_list = IntegerList(10, 4, 0)

        result = int_list.get(2)
        self.assertEqual(0, result)

    def test_get__with_invalid_index_raises(self):
        int_list = IntegerList(10, 4, 0)

        with self.assertRaises(IndexError) as ex:
            int_list.get(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_with_valid_data_type_and_valid_index(self):
        int_list = IntegerList(10, 4, 0)

        int_list.insert(2, 5)
        self.assertEqual([10, 4, 5, 0], int_list._IntegerList__data)

    def test_insert_with_invalid_index_raises(self):
        int_list = IntegerList(10, 4, 0)

        with self.assertRaises(IndexError) as ex:
            int_list.insert(3, 5)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_with_invalid_data_type(self):
        int_list = IntegerList(10, 4, 0)

        with self.assertRaises(ValueError) as ex:
            int_list.insert(2, "5")

        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            int_list.insert(2, 3.3)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_returns_correct_value(self):
        int_list = IntegerList(10, 4, 0, 44, -5, 1)

        result = int_list.get_biggest()
        self.assertEqual(44, result)

    def test_get_index(self):
        int_list = IntegerList(10, 4, 0, 44, -5, 1)

        result = int_list.get_index(-5)
        self.assertEqual(4, result)

        result = int_list.get_index(10)
        self.assertEqual(0, result)


if __name__ == "__main__":
    main()
