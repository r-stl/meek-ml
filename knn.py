import metrics
from operator import itemgetter

class KNN():
    """ KNN classifier 
    
    at the moment it will use a naive search (brute force)
    and euclidean distance metrics
    TODO: 
        - ball-tree or m-tree
        - support for different metrics
    """

    def __init__(self):
        pass
        
    def calc_distance(self, point1, point2):
        """ calculates euclidean distance between two points
        """
        return metrics.euclidean_distance(point1, point2)

    def calc_distances_12m(self, point, other_points):
        """ calculates distances between a point and a list of points
        """
        return [self.calc_distance(point, other) for other in other_points]
    
    def calc_distances_m2m(self, points, other_points):
        """ calculates distances between two lists of points
        """
        return [self.calc_distances_12m(point, other_points) for point in points]

    def get_nearest_neighbors(self, points, other_points):
        """ get neighbors sorted by distance

        returns index and distance
        """
        raw_distances = self.calc_distances_m2m(points, other_points)
        enum_distances = enumerate(raw_distances)
        sorted_distances = sorted(enum_distances, key=itemgetter(1))
        indices, distances = zip(sorted_distances)
        return indices, distances

    def get_k_nearest_neighbors(self, points, other_points, k):
        indices, distances = self.get_nearest_neighbors(points, other_points)
        return indices[:k], distances[:k]        


    