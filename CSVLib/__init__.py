import csv


class CSVLib(object):

    """ Reads a given CSV file and returns it as a dictionary. """
    def read_csv_as_dictionary(self, filename, key_column, value_columns, delimiter='\n'):
        file = open(filename, 'r')
        csvfile = csv.DictReader(file, delimiter=delimiter)
        output = {}
        for row in csvfile:
            if type(value_columns) == str:
                output[row[key_column]] = row[value_columns]
            elif type(value_columns) == list:
                valueList = []
                for value in value_columns:
                    valueList.append(row[value])
                output[row[key_column]] = valueList

        file.close()
        return output

    """ Reads a given CSV file and returns it as a list containing all rows as list. """
    def read_csv_as_list(self, filename, delimiter='\n'):
        file = open(filename, 'r')
        csvfile = csv.reader(file, delimiter=delimiter)
        output = []
        for row in csvfile:
            output.append(row)
        file.close()
        return output

    """ Reads a given CSV file and returns it as a single list containing all values. """
    def read_csv_as_single_list(self, filename, delimiter='\n'):
        file = open(filename, 'r')
        csvfile = csv.reader(file, delimiter=delimiter)
        output = []
        for row in csvfile:
            for value in row:
                output.append(value)
        file.close()
        return output
