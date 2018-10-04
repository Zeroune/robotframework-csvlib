from CSVLib import CSVLibrary
import unittest


class TestCSVLib(unittest.TestCase):

    def test_read_csv_as_single_list(self):
        expected = ['Cat', 'Dog', 'Fish', 'Bird', 'Cow', 'Pig', 'Sheep']
        self.assertEqual(expected, CSVLibrary.read_csv_file_as_single_list(CSVLibrary(), 'data/test.csv'))


if __name__ == '__main__':
    unittest.main()
