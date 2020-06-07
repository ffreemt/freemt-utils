# from freemt_utils.make_url import make_url
from freemt_utils import cos_matrix2


def test_cos_matrix2():
    ''' test cos_matrix2. '''

    assert cos_matrix2([[1, 1]], [[1, 1]])[0, 0] > 0.9


def test_cos_matrix2a():
    ''' test cos_matrix2. '''

    assert cos_matrix2([[1, 1]])[0, 0] > 0.9
