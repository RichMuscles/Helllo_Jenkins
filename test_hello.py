import pytest
from hello_world import *

#this is a test
def test_hello():
    result = hello ()
    assert result == "Hello!"



