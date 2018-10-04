import csv


class CSVLibrary(object):

    def read_csv_file_as_single_list(self, filename, delimiter='\n'):
        """ Reads a given CSV file and returns it as a single list containing all values. """
        file = open(filename, 'r')
        csvfile = csv.reader(file, delimiter=delimiter)
        output = []
        for row in csvfile:
            for value in row:
                print(value)
                output.append(value)
        file.close()
        return output