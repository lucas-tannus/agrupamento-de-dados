import random
import copy
import numpy as np

from src.const import KMeansConst
from src.utils import (
    calculate_euclidean_distance,
    calculate_mean
)


class KMeans(object):

    def __init__(self, data_set, number_of_centroids):
        self.data_set = data_set
        self.number_of_centroids = number_of_centroids
        self.iterations = 0

    def execute(self):
        self._define_centroids()

        for _ in range(KMeansConst.max_iterations_number):
            self._build_groups()
            if not self._has_change_occurred():
                break
            self._recalculate_controids()
            self.iterations += 1
        return self.groups

    def _define_centroids(self):
        self.groups = random.sample(self.data_set, k=self.number_of_centroids)
        self.groups = list(map(lambda centroid: {'centroid': centroid, 'group': []}, self.groups))

    def _has_change_occurred(self):
        for index in range(self.number_of_centroids):
            if not np.array_equal(self.groups[index]['group'], self.previous_groups[index]['group']):
                return True
        return False

    def _build_groups(self):
        self.previous_groups = copy.deepcopy(self.groups)
        self._clear_groups()
        for subject in self.data_set:
            centroids_distance = []
            for group in self.groups:
                centroids_distance.append(calculate_euclidean_distance(subject, group['centroid']))
            group = centroids_distance.index(min(centroids_distance))
            self.groups[group]['group'].append(subject)

    def _recalculate_controids(self):
        for centroid in self.groups:
            new_centroid = calculate_mean(centroid['group'])
            centroid['centroid'] = new_centroid

    def _clear_groups(self):
        for group in self.groups:
            group['group'] = []
