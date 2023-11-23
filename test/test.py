import unittest

from src.main import group_by_tribe, read_file, count_possible_pairs

class TestPossiblePairs(unittest.TestCase):
    def test_scenario_1(self):
        input_file = "input_1.txt"
        expected_output = 4

        tribes, boys, girls = read_file(input_file)
        tribe_groups = group_by_tribe(tribes, boys, girls)
        count = count_possible_pairs(tribe_groups)

        self.assertEqual(count, expected_output)

    def test_scenario_2(self):
        input_file = "input_2.txt"
        expected_output = 6

        tribes, boys, girls = read_file(input_file)
        tribe_groups = group_by_tribe(tribes, boys, girls)
        count = count_possible_pairs(tribe_groups)

        self.assertEqual(count, expected_output)


if __name__ == "__main__":
    unittest.main()