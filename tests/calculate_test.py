import pytest
import math
from calculate import calc


class TestCalcSquare:
    def test_number_area(self):
        side = 100
        result = calc("square", "area", [side])
        assert result == 10000

    def test_zero_area(self):
        side = 0
        result = calc("square", "area", [side])
        assert result == 0

    def test_negative_area(self):
        side = -5
        with pytest.raises(ValueError, match="Size can't have a negative value"):
            calc("square", "area", [side])

    def test_number_perimeter(self):
        side = 50
        result = calc("square", "perimeter", [side])
        assert result == 200

    def test_zero_perimeter(self):
        side = 0
        result = calc("square", "perimeter", [side])
        assert result == 0

    def test_negative_perimeter(self):
        side = -10
        with pytest.raises(ValueError, match="Size can't have a negative value"):
            calc("square", "perimeter", [side])


class TestCalcCircle:
    def test_number_area(self):
        r = 100
        result = calc("circle", "area", [r])
        assert result == 10000 * math.pi

    def test_zero_area(self):
        r = 0
        result = calc("circle", "area", [r])
        assert result == 0

    def test_negative_area(self):
        r = -1000
        with pytest.raises(ValueError, match="Size can't have a negative value"):
            calc("circle", "area", [r])

    def test_number_perimeter(self):
        r = 50
        result = calc("circle", "perimeter", [r])
        assert result == 100 * math.pi

    def test_zero_perimeter(self):
        r = 0
        result = calc("circle", "perimeter", [r])
        assert result == 0

    def test_negative_perimeter(self):
        r = -30
        with pytest.raises(ValueError, match="Size can't have a negative value"):
            calc("circle", "perimeter", [r])
