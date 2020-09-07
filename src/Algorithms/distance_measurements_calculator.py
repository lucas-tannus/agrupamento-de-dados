import sys

from pandas import DataFrame

from ..Managers.csv_manager import CsvManager
from ..exceptions import ArgumentsError, DatasetError
from ..utils import (
    calculate_euclidean_distance,
    calculate_manhattan_distance
)
from ..const import DistanceMeasurementTypeConst
from ..Managers.text_manager import TextManager


class DistanceMeasurement(object):

    def execute(self):
        self.__validate_arguments()
        self.__define_data_set()
        self.__calculate_distance_between_subjects()
        self.__send_result_to_file()

    def __validate_arguments(self):
        try:
            if len(sys.argv) != 4:
                raise ArgumentsError()

            self.file_name = str(sys.argv[1])
            self.features_size = int(sys.argv[2])
            self.distance_measurement_type = str(sys.argv[3])

            if self.distance_measurement_type not in \
                    [DistanceMeasurementTypeConst.euclidean, DistanceMeasurementTypeConst.manhattan]:
                raise ArgumentsError(message='Tipo de medida de distância passada não é válida. '
                                             'Deve ser "euclidean" ou "manhattan" ')
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

    def __calculate_distance_between_subjects(self):
        self.distance_calculation = []

        for idx, subject_x in self.data_set.iterrows():
            parcial_calculation = []
            subject_x = subject_x.values.tolist()

            for idy, subject_y in self.data_set.iterrows():
                subject_y = subject_y.values.tolist()

                if self.distance_measurement_type == DistanceMeasurementTypeConst.euclidean:
                    parcial_calculation.append(str(calculate_euclidean_distance(subject_x, subject_y)))

                if self.distance_measurement_type == DistanceMeasurementTypeConst.manhattan:
                    parcial_calculation.append(str(calculate_manhattan_distance(subject_x, subject_y)))

            self.distance_calculation.append(parcial_calculation)

    def __send_result_to_file(self):
        text_manager = TextManager()
        file_name = text_manager.create_file_name(self.file_name)

        for distance in self.distance_calculation:
            text_manager.builder(file_name, '{}\n'.format(', '.join(distance)))
