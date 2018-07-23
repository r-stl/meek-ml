import metrics

def test_euclidean_distance():
    distance = metrics.euclidean_distance([0, 0], [1, 0])
    assert( distance == 1 )