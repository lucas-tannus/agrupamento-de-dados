import sys

from src.exceptions import ArgumentsError
from src.Managers.csv_manager import CsvManager
from src.Managers.text_manager import TextManager
from src.Algorithms.partitional_algorithms import KMeans
from src.Algorithms.cluster_validation import Purity


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ArgumentsError()
        file_name = str(sys.argv[1])
        data_set = CsvManager().reader(file_name=file_name)

        parsed_data_set = []
        subjects_class = {}
        for subj in data_set:
            subj_class = subj.pop(len(subj)-1)
            parsed_subj = list(map(lambda item: float(item), subj))
            subjects_class[str(parsed_subj)] = subj_class

            parsed_data_set.append(parsed_subj)

        text_manager = TextManager()
        file_name = text_manager.create_file_name(file_name)

        for centroid_number in range(2, 5):
            text_manager.builder(file_name, '\nK={}\n'.format(centroid_number))
            groups = KMeans(data_set=parsed_data_set, number_of_centroids=centroid_number).execute()

            clusters_purity = Purity(clusters=groups, subjects_class=subjects_class).clusters_purity

            for index, cluster_purity in enumerate(clusters_purity):
                text_manager.builder(file_name, 'GRUPO {} - CENTROÍDE {} - PURITY: {}%\n'.format(
                    index, cluster_purity['centroid'], cluster_purity['purity'] * 100))
    except ValueError:
        raise ArgumentsError(message='Tipo de dado passado nos argumentos não são válidos. '
                                     'É esperado que o nome do arquivo seja do tipo texto')
