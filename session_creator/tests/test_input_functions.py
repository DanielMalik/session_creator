import context
import unittest
from input_functions import *


class TestGetColumnAndCells(unittest.TestCase):  # konwencja, klasy CamelKejsem

    def test_valid_value(self):
        self.assertEqual(get_column_and_cells('A23:150'), ('a', ('23', '150')))

    def test_wrong_row_range(self):
        with self.assertRaises(ValueError):
            get_column_and_cells('A1000:5')

    def test_random_data(self):
        with self.assertRaises(ValueError):
            get_column_and_cells('stefan')


class TestParseCliArguments(unittest.TestCase):

    def test_empty_input(self):
        with self.assertRaises(SystemExit) as se:
            parse_cli_arguments([])
        self.assertEqual(se.exception.code, 2)

    def test_less_than_three_parameters(self):  # jak nie ma 'test' w nazwie, to nie robi
        with self.assertRaises(SystemExit) as se:
            parse_cli_arguments(['a', 'b'])
        self.assertEqual(se.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
