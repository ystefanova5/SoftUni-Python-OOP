from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class Tests(TestCase):
    def test_01_init(self):
        card = StudentReportCard("Boris", 1)

        self.assertEqual("Boris", card.student_name)
        self.assertEqual(1, card.school_year)
        self.assertEqual({}, card.grades_by_subject)

    def test_02_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = StudentReportCard("", 1)

        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_03_invalid_school_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = StudentReportCard("Boris", 0)

        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            card = StudentReportCard("Boris", 13)

        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

        card = StudentReportCard("Boris", 12)
        self.assertEqual(12, card.school_year)

    def test_04_add_grade(self):
        card = StudentReportCard("Boris", 1)

        card.add_grade("Math", 6)
        self.assertEqual({"Math": [6]}, card.grades_by_subject)

        card.add_grade("Math", 5)
        self.assertEqual({"Math": [6, 5]}, card.grades_by_subject)

        card.add_grade("Music", 6)
        self.assertEqual({"Math": [6, 5], "Music": [6]}, card.grades_by_subject)

    def test_05_average_grade_by_subject(self):
        card = StudentReportCard("Boris", 1)
        card.grades_by_subject = {"Math": [5, 6, 5], "Music": [6, 4], "English": [5, 6]}

        result = card.average_grade_by_subject()
        expected_result = "Math: 5.33\nMusic: 5.00\nEnglish: 5.50"

        self.assertEqual(expected_result, result)

    def test_06_average_grade_for_all_subjects(self):
        card = StudentReportCard("Boris", 1)
        card.grades_by_subject = {"Math": [5, 6, 5], "Music": [6, 4], "English": [5, 6]}

        result = card.average_grade_for_all_subjects()
        expected_result = "Average Grade: 5.29"

        self.assertEqual(expected_result, result)

    def test_07_repr(self):
        card = StudentReportCard("Boris", 1)
        card.grades_by_subject = {"Math": [5, 6, 5], "Music": [6, 4], "English": [5, 6]}

        result = repr(card)
        expected_result = "Name: Boris\n" \
                          "Year: 1\n" \
                          "----------\n" \
                          "Math: 5.33\n" \
                          "Music: 5.00\n" \
                          "English: 5.50\n" \
                          "----------\n" \
                          "Average Grade: 5.29"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
