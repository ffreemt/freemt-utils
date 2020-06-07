"""test mtok mdetok

mtok('"I\'m a student.""我是学生"')  13

from sacremoses import MosesTokenizer, MosesDetokenizer
"""

from freemt_utils import mtok, mdetok


def test_mtok():
    """ test mtok """
    assert len(mtok('"I\'m a student.""我是学生"')) == 13


def test_mdetok():
    """ test mdetok """
    mdetok(mtok('"I\'m a student.""我是学生"')) == '"I\'m a student.""我是学生"'
