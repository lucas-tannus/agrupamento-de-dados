import sys

from src.exceptions import ArgumentsError
from src.Managers.csv_manager import CsvManager
from src.Managers.text_manager import TextManager
from src.Algorithms.partitional_algorithms import KMeans

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise ArgumentsError()
        file_name = str(sys.argv[1])
        number_of_centroids = int(sys.argv[2])

        data_set = CsvManager().reader(file_name=file_name)
        data_set = list(map(lambda subject: list(map(lambda item: float(item), subject)), list(data_set)))
        groups = KMeans(data_set=data_set, number_of_centroids=number_of_centroids).execute()

        text_manager = TextManager()
        file_name = text_manager.create_file_name(file_name)
        for index, group in enumerate(groups):
            text_manager.builder(file_name, 'GRUPO {} - CENTROÍDE {}\n'.format(index, group['centroid']))
            for subject in group['group']:
                text_manager.builder(file_name, '{}\n\n'.format(''.join(str(subject))))
    except ValueError:
        raise ArgumentsError(message='Tipo de dado passado nos argumentos não são válidos. '
                                     'É esperado que o nome do arquivo seja do tipo texto e '
                                     'a quantidade de centróides seja do tipo inteiro')
