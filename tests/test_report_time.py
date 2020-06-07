# from freemt_utils.make_url import make_url
from freemt_utils import report_time


def test_report_time():
    ''' test report_time. '''
    from time import sleep
    with report_time():
        sleep(1)
    assert report_time.time_elapsed > 0.9
