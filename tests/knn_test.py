import knn

def test_calculate_distance():
    distance = knn.calculate_distance([0, 0], [1, 0])
    assert( distance == 1)

def test_calculate_distances_12m():
    points = [[0 1] [2 2] [-1 0] [0 0]]
    distances = knn.calculate_distances_12m([0 0], points)
    assert( distances.shape() = points.shape())
    assert( distances == [[1][2][1][0])

def test_calculate_distance():
    points = [1 2 3 4 5]
    other_points = [0 1 2 3 4 5 6 7 8 9]
    distances = knn.calculate_distances_m2m(points, other_points)
    assert( distances == [[]])

def test_get_nearest_neighbors():
    

def test_get_k_nearest_neighbors():

