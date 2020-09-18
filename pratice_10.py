import sys

from src.exceptions import ArgumentsError
from src.Managers.csv_manager import CsvManager
from src.Managers.text_manager import TextManager
from src.Algorithms.hierarchical_algorithms import SingleLink


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ArgumentsError()
        file_name = str(sys.argv[1])
        data_set = CsvManager().reader(file_name=file_name)

        levels = SingleLink(data_set=list(data_set)).execute()

        text_manager = TextManager()
        file_name = text_manager.create_file_name(file_name)
        for level in levels:
            groups = []
            for group in level[1]:
                groups.append('{group}'.format(group=str(group['group'])).replace('[', '{').replace(']', '}'))
            text_manager.builder(file_name, '{}\n'.format(', '.join(groups)))
    except ValueError:
        raise ArgumentsError(message='Tipo de dado passado nos argumentos não são válidos. '
                                     'É esperado que o nome do arquivo seja do tipo texto')
