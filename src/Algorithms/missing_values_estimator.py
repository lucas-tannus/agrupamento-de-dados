import sys
import numpy as np

from ..Managers.csv_manager import CsvManager
from ..exceptions import ArgumentsError, DatasetError
from pandas import DataFrame


class MissingValuesEstimator(object):

    def execute(self):
        self.__validate_arguments()
        self.__define_data_set()
        self.__build_data_set_without_missing_data()
        self.__replace_mode_values(self.__calculate_mode())
        CsvManager().builder(self.file_name, self.estimated_data_set)

    def __validate_arguments(self):
        try:
            if len(sys.argv) != 3:
                raise ArgumentsError()
            self.file_name = str(sys.argv[1])
            self.features_size = int(sys.argv[2])
        except ValueError:
            raise ArgumentsError(message='Tipo de dado passado nos argumentos não são válidos. '
                                         'É esperado que o nome do arquivo seja do tipo texto e '
                                         'a quantidade de atributos seja do tipo inteiro')

    def __define_data_set(self):
        self.data_set = CsvManager().reader(self.file_name)
        self.__validate_data()

    def __validate_data(self):
        self.data_set = DataFrame(filter(lambda subject: len(subject) == self.features_size, self.data_set))

        if not len(self.data_set):
            raise DatasetError(message='Dataset está vazio. Não é possível continuar '
                                       'executando... verifique a quantidade de atributos passados')

    def __build_data_set_without_missing_data(self):
        self.set_without_missing_data = self.data_set.replace(['?'], np.nan)

    def __calculate_mode(self):
        return self.set_without_missing_data.mode()

    def __replace_mode_values(self, mode_list):
        self.estimated_data_set = []
        for index, subject in self.data_set.iterrows():
            subject = subject.to_list()
            for idx, attr in enumerate(subject, start=0):
                if subject[idx] == '?':
                    subject[idx] = mode_list.loc[0, idx]
            self.estimated_data_set.append(subject)
