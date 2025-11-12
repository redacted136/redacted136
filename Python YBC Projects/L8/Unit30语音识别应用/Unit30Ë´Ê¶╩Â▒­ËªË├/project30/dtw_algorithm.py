from numpy import array, zeros, argmin, inf, equal, ndim, linalg
from scipy.spatial.distance import cdist

def dtw(x, y):
    """
    Computes Dynamic Time Warping (DTW) of two sequences.

    :param array x: N1*M array
    :param array y: N2*M array
    :param func dist: distance used as cost measure

    Returns the minimum distance, the cost matrix, the accumulated cost matrix, and the wrap path.
    """
    x = x.T
    y = y.T
    dist = lambda x,y: linalg.norm(x - y, ord=1)
    assert len(x)  # Report error while x is none
    assert len(y)
    r, c = len(x), len(y)
    D0 = zeros((r + 1, c + 1))
    D0[0, 1:] = inf
    D0[1:, 0] = inf
    D1 = D0[1:, 1:] # view

    for i in range(r):
        for j in range(c):
            D1[i, j] = dist(x[i], y[j])

    for i in range(r):
        for j in range(c):
            D1[i, j] += min(D0[i, j], D0[i, j+1], D0[i+1, j])

    return D1[-1, -1] / sum(D1.shape)
