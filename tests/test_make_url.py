# from freemt_utils.make_url import make_url
from freemt_utils import make_url


def test_make_url():
    ''' test make_url '''
    assert make_url('http://127.0.0.1') == 'http://127.0.0.1'
    assert make_url('htp://127.0.0.1') == 'http://127.0.0.1'
    assert make_url('127.0.0.1') == 'http://127.0.0.1'
    assert make_url('http://173.82.240.230:5000/json') == 'http://173.82.240.230:5000/json'


def  test_make_url_none():
    ''' test_make_url_none '''
    assert make_url() is None
    assert make_url(None) is None
