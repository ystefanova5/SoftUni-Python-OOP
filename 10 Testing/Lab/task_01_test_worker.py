class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_worker_is_initialized_correctly(self):
        worker = Worker("Name", 1000, 10)
        self.assertEqual("Name", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_after_calling_rest_method(self):
        # Arrange
        worker = Worker("Name", 1000, 10)
        self.assertEqual(10, worker.energy)

        # Act
        worker.rest()

        # Assert
        self.assertEqual(11, worker.energy)

    def test_if_worker_with_zero_energy_raises(self):
        worker = Worker("Name", 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_worker_with_negative_energy_raises(self):
        worker = Worker("Name", 1000, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_money_is_increased_after_work(self):
        worker = Worker("Name", 1000, 10)
        self.assertEqual(0, worker.money)

        worker.work()
        self.assertEqual(1000, worker.money)

        worker.work()
        self.assertEqual(2000, worker.money)

    def test_worker_energy_decreased_after_work(self):
        worker = Worker("Name", 1000, 10)
        self.assertEqual(10, worker.energy)

        worker.work()
        self.assertEqual(9, worker.energy)

        worker.work()
        self.assertEqual(8, worker.energy)

    def test_get_info_returns_correct_values(self):
        worker = Worker("Name", 1000, 10)

        worker.work()
        result = worker.get_info()
        self.assertEqual("Name has saved 1000 money.", result)


if __name__ == "__main__":
    main()
