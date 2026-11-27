import sys


def test_break():
    assert sys.platform != "win32"  # échoue uniquement sur Windows