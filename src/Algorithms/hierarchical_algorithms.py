import copy

from src.utils import calculate_euclidean_distance


class SingleLink(object):

    def __init__(self, data_set):
        self.data_set = data_set
        self.distance_table_states = []
        self.min_value = float('inf')

        self._build_distance_table()

    def execute(self):
        while not self._exists_one_group():
            row_group, col_group = self._get_min_value()
            self._save_table_state()
            self._merge_groups(row_group, col_group)
        self._save_table_state()

        return self.distance_table_states

    def _build_distance_table(self):
        self.distance_table = []

        for row_index, subject in enumerate(self.data_set):
            subject_distances = []
            for col_index, other_subject in enumerate(self.data_set):
                distance = calculate_euclidean_distance(
                    subject_x=subject, subject_y=other_subject
                )
                subject_distances.append({'group': [col_index], 'distance': distance})
            self.distance_table.append({'group': [row_index], 'distances': subject_distances})

    def _exists_one_group(self):
        return len(self.distance_table) == 1

    def _get_min_value(self):
        self.min_value = float('inf')
        for r_index, row in enumerate(self.distance_table):
            for c_index, col in enumerate(row['distances']):
                if col['distance'] != 0 and col['distance'] < self.min_value:
                    self.min_value = col['distance']
                    row_index = r_index
                    col_index = c_index
        return row_index, col_index

    def _save_table_state(self):
        self.distance_table_states.append((self.min_value, copy.deepcopy(self.distance_table)))

    def _merge_groups(self, row_group, col_group):
        # Faz o recálculo das distancias da tabela
        for row_index, row in enumerate(self.distance_table):
            if row_index == row_group or row_index == col_group:
                continue
            for col_index, col in enumerate(row['distances']):
                if col_index == row_group and not col['distance'] == 0:
                    row['distances'][col_group]['distance'] = col['distance'] = (
                        col['distance'] if col['distance'] < row['distances'][col_group]['distance'] else
                        row['distances'][col_group]['distance'])
                    self.distance_table[col_group]['distances'][row_index]['distance'] = col['distance']
                    self.distance_table[row_group]['distances'][row_index]['distance'] = col['distance']

        # Faz o merge dos dois grupos de acordo com o menor valor
        self.distance_table[row_group]['group'].extend(self.distance_table[col_group]['group'])

        # Exclui as linhas da tabela
        self.distance_table.pop(col_group)
        for row in self.distance_table:
            row['distances'].pop(col_group)
