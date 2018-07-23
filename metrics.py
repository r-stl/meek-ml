import math

def euclidean_distance(vector1, vector2):
    """ computes the euclidean distance between
    the vectors a and b
    """
    distance = [(a - b)**2 for a, b in zip(vector1, vector2)]
    distance = math.sqrt(sum(distance))
    return distance