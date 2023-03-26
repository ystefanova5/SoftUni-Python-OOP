from project.team import Team
from unittest import TestCase, main


class Tests(TestCase):
    def test_01_init(self):
        team = Team("Bulls")

        self.assertEqual("Bulls", team.name)
        self.assertEqual({}, team.members)

    def test_02_incorrect_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("Bulls2")

        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

        team = Team("Bulls")
        with self.assertRaises(ValueError) as ex:
            team.name = "Bulls_"

        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_03_add_member_adds_correctly(self):
        team = Team("Bulls")

        result = team.add_member()
        expected_result = "Successfully added: "

        self.assertEqual({}, team.members)
        self.assertEqual(expected_result, result)

        team.add_member(John=20)

        self.assertEqual({"John": 20}, team.members)

        result = team.add_member(Mark=19, Tom=22, John=21)
        expected_result = "Successfully added: Mark, Tom"

        self.assertEqual({"John": 20, "Mark": 19, "Tom": 22}, team.members)
        self.assertEqual(expected_result, result)

    def test_04_remove_valid_member(self):
        team = Team("Bulls")
        team.add_member(John=20, Mark=19, Tom=22)

        result = team.remove_member("Tom")
        self.assertEqual("Member Tom removed", result)
        self.assertEqual({"John": 20, "Mark": 19}, team.members)

    def test_05_remove_invalid_member(self):
        team = Team("Bulls")
        team.add_member(John=20, Mark=19, Tom=22)

        result = team.remove_member("Sam")
        self.assertEqual("Member with name Sam does not exist", result)
        self.assertEqual({"John": 20, "Mark": 19, "Tom": 22}, team.members)

    def test_06_greater_than_returns_true(self):
        team = Team("Bulls")
        team.add_member(John=20, Mark=19, Tom=22)

        other_team = Team("Hawks")
        other_team.add_member(Sam=20)

        result = team > other_team

        self.assertEqual(True, result)
        self.assertTrue(team > other_team)
        self.assertFalse(team < other_team)

    def test_07_greater_than_returns_false(self):
        team = Team("Bulls")
        team.add_member(John=20)

        other_team = Team("Hawks")
        other_team.add_member(Sam=20, Don=23)

        result = team > other_team

        self.assertEqual(False, result)
        self.assertFalse(team > other_team)
        self.assertTrue(team < other_team)

        other_team.remove_member("Sam")
        result = team > other_team

        self.assertEqual(False, result)
        self.assertFalse(team > other_team)
        self.assertFalse(other_team > team)

    def test_08_len(self):
        team = Team("Bulls")
        team.add_member(John=20, Mark=19, Tom=22)

        result = len(team)
        self.assertEqual(3, result)

    def test_09_add(self):
        team = Team("Bulls")
        team.add_member(John=20, Mark=19, Tom=22)

        other_team = Team("Hawks")
        other_team.add_member(Sam=20, Tom=21)

        merged_team = team + other_team

        self.assertEqual("BullsHawks", merged_team.name)
        self.assertEqual({"John": 20, "Mark": 19, "Tom": 22, "Sam": 20}, merged_team.members)

    def test_10_str(self):
        team = Team("Bulls")
        team.add_member(John=20, Mark=19, Tom=22)

        result = str(team)
        expected_result = "Team name: Bulls\n" \
                          "Member: Tom - 22-years old\n" \
                          "Member: John - 20-years old\n" \
                          "Member: Mark - 19-years old"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
