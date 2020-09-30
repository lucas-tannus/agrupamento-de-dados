
class Purity:

    def __init__(self, clusters, subjects_class):
        self.clusters = clusters
        self.subjects_class = subjects_class
        self.clusters_purity = self._calculate()

    def _calculate(self):
        clusters_purity = []
        for cluster in self.clusters:
            cluster_classes = {}
            for subject in cluster['group']:
                subject_class = self.subjects_class[str(subject)]

                if hasattr(cluster_classes, subject_class):
                    cluster_classes += 1
                else:
                    cluster_classes[subject_class] = 1
            purity = self._calculate_purity(cluster_classes, len(cluster['group']))
            clusters_purity.append({'centroid': cluster['centroid'], 'purity': purity})
        return clusters_purity

    def _calculate_purity(self, clusters_classes, cluster_size):
        return max(clusters_classes.values()) / cluster_size
