import pytest
from utils import map_reduce

class TestUtils:
    def test_flat_map(self):
        assert map_reduce(lambda x: x+1, list(range(1, 4))) == 9

        with pytest.raises(Exception):
           map_reduce(lambda x: x+1, [])