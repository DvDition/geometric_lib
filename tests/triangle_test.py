import pytest
from triangle import area, perimeter


class TestArea:
    def test_number_area(self):
        a = 100
        h = 200
        result = area(a, h)
        assert result == 10000

    def test_zero_area(self):
        a = 0
        h = 0
        result = area(a, h)
        assert result == 0

    def test_negative_area(self):
        a = -5
        h = 10
        with pytest.raises(ValueError, match="Length can't have a negative value"):
            area(a, h)


class TestPerimeter:
    def test_number_perimeter(self):
        a = 50
        b = 100
        c = 80
        result = perimeter(a, b, c)
        assert result == 230

    def test_zero_perimeter(self):
        a = 0
        b = 0
        c = 0
        with pytest.raises(ValueError, match="Length can't have a negative/zero value"):
            perimeter(a, b, c)

    def test_negative_perimeter(self):
        a = -10
        b = -100
        c = 20
        with pytest.raises(ValueError, match="Length can't have a negative/zero value"):
            perimeter(a, b, c)
