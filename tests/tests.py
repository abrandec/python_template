""" Python Template Unit Tests """
from src.module import hello_world

def test_hello_world():
    """ Test Hello world """
    assert hello_world() == "Hello World"
