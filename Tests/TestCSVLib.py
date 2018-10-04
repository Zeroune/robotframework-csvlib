from CSVLib import CSVLibrary
import unittest


class TestCSVLib(unittest.TestCase):

    def test_read_csv_as_dictionary(self):
        expected = {'Bird': '2', 'Cat': '4', 'Cow': '4', 'Dog': '4', 'Fish': '0', 'Pig': '4', 'Sheep': '4'}
        self.assertEqual(expected, CSVLibrary.read_csv_as_dictionary(CSVLibrary(),
                                                                     'data/test_dict.csv', 'Animal', 'Legs', ','))

    def test_read_csv_as_list(self):
        expected = [['Cat'], ['Dog'], ['Fish'], ['Bird'], ['Cow'], ['Pig'], ['Sheep']]
        self.assertEqual(expected, CSVLibrary.read_csv_as_list(CSVLibrary(), 'data/test.csv'))

    def test_read_csv_as_single_list(self):
        expected = ['Cat', 'Dog', 'Fish', 'Bird', 'Cow', 'Pig', 'Sheep']
        self.assertEqual(expected, CSVLibrary.read_csv_as_single_list(CSVLibrary(), 'data/test.csv'))


if __name__ == '__main__':
    unittest.main()
