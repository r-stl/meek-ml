import numpy as np
import math

field = np.array([1, 0])

np.abs(field)

def euclideanDistance(vector1, vector2):
    """ computes the euclidean distance between
    the vectors a and b
    """
    distance = [np.diff(stack)**2 for stack in np.column_stack((vector1, vector2))]
    print(distance)
    distance = np.sqrt(np.sum(distance))
    return distance

print (euclideanDistance(np.array([1,2]), np.array([0,0])))


dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
    dist = math.sqrt(sum(dist))
    return dist