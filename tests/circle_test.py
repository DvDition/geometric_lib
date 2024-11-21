import pytest
import math
from circle import area, perimeter


class TestArea:
    def test_number_area(self):
        r = 100
        result = area(r)
        assert result == 10000 * math.pi

    def test_zero_area(self):
        r = 0
        result = area(r)
        assert result == 0

    def test_negative_area(self):
        r = -1000
        with pytest.raises(ValueError, match="Radius can't have\
                            a negative value"):
            area(r)


class TestPerimeter:
    def test_number_perimeter(self):
        r = 50
        result = perimeter(r)
        assert result == 100 * math.pi

    def test_zero_perimeter(self):
        r = 0
        result = perimeter(r)
        assert result == 0

    def test_negative_perimeter(self):
        r = -30
        with pytest.raises(ValueError, match="Radius can't have\
                            a negative value"):
            perimeter(r)
