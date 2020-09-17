import numpy as np
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

    def _build_distance_table(self):
        self.distance_table = []

        for index, subject in enumerate(self.data_set):
            subject_distances = []
            for other_subject in self.data_set[:index + 1]:
                subject_distances.append(calculate_euclidean_distance(
                    subject_x=subject, subject_y=other_subject
                ))
            self.distance_table.append({'group': {index}, 'distances': subject_distances})

    def _exists_one_group(self):
        return len(self.distance_table) == 2

    def _get_min_value(self):
        self.min_value = float('inf')
        for row_index, row in enumerate(self.distance_table):
            for col_index, distance in enumerate(row['distances']):
                if distance != 0 and distance < self.min_value:
                    self.min_value = distance
                    row_group = row_index
                    col_group = col_index
        return row_group, col_group

    def _save_table_state(self):
        self.distance_table_states.append((self.min_value, copy.deepcopy(self.distance_table)))

    def _merge_groups(self, row_group, col_group):
        print(self.distance_table)
        for row_index, row in enumerate(self.distance_table):
            for col_index, col in enumerate(row['distances']):
                if row_group == row_index:


