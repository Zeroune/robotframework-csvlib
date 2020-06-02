from CSVLib import CSVLib
import unittest


class TestCSVLib(unittest.TestCase):

    def test_read_csv_as_dictionary(self):
        expected = {'Bird': '2', 'Cat': '4', 'Cow': '4', 'Dog': '4', 'Fish': '0', 'Pig': '4', 'Sheep': '4'}
        self.assertEqual(expected, CSVLib.read_csv_as_dictionary(CSVLib(),
                                                                 'data/test_dict.csv', 'Animal', 'Legs', ','))

        expected = {'Bird': ['2', '2'], 'Cat': ['4', '2'], 'Cow': ['4', '2'], 'Dog': ['4', '2'],
                    'Fish': ['0', '2'], 'Pig': ['4', '2'], 'Sheep': ['4', '2']}
        self.assertEqual(expected, CSVLib.read_csv_as_dictionary(CSVLib(),
                                                                 'data/test_dict1.csv', 'Animal', ['Legs', 'Eyes'], ','))

    def test_read_csv_as_list(self):
        expected = [['Cat'], ['Dog'], ['Fish'], ['Bird'], ['Cow'], ['Pig'], ['Sheep']]
        self.assertEqual(expected, CSVLib.read_csv_as_list(CSVLib(), 'data/test.csv'))

    def test_read_csv_as_list_for_multiple_column(self):
        expected = [['Animal','Legs'], ['Cat','4'], ['Dog','4'], ['Fish','0'], ['Bird','2'], ['Cow','4'], ['Pig','4'], ['Sheep','4']]
        self.assertEqual(expected, CSVLib.read_csv_as_list(CSVLib(), 'data/test_dict.csv'))

    def test_read_csv_as_single_list(self):
        expected = ['Cat', 'Dog', 'Fish', 'Bird', 'Cow', 'Pig', 'Sheep']
        self.assertEqual(expected, CSVLib.read_csv_as_single_list(CSVLib(), 'data/test.csv'))

    if __name__ == '__main__':
        unittest.main()
