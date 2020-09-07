import csv

from .file_manager import FileManager


class CsvManager(FileManager):

    def __init__(self):
        super().__init__(file_extension='csv')

    def reader(self, file_name):
        csv_file = open(self._build_file_name(file_name), newline='')
        return csv.reader(csv_file, delimiter=',')

    def builder(self, file_name, data_list):
        with open(self.create_file_name(file_name), 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            for row in data_list:
                writer.writerow(row)
