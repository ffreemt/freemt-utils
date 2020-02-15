from pathlib import Path
# from freemt_utils.switch_to import switch_to
from freemt_utils import switch_to


def test_swtch_to():
    ''' test swtch_to '''
    assert 'switch_to' in Path(__file__).__str__()
    with switch_to(Path.home()):
        assert Path.cwd() == Path('~').expanduser()
