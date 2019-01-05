"""Demo fixtue scope."""

import pytest

@pytest.fixture(scope='function')
def func_scope():
    """A function sceop fixture"""
@pytest.fixture(scope='module')
def mod_scope():
    """A module sceop fixture"""
@pytest.fixture(scope='session')
def sess_scope():
    """A session sceop fixture"""
@pytest.fixture(scope='class')
def class_scope():
    """A class sceop fixture"""


def test_1():
# def test_1(sess_scope,mod_scope,func_scope):

    """Test using session , module and funtion scope fixtures."""

# def test_2(sess_scope,mod_scope,func_scope):
def test_2():

    """Demo is more fun with multiple tests."""

# @pytest.mark.usefixtures('class_scope')
class TestSomething(class_scope):
    """Demo calss scope fixtuers."""
    def test_3(self):
        """test using a class sceop fixture"""
    def test_4(self):
        """Again, multiple tests are more fun"""


