import pytest
from square import area, perimeter


class TestArea:
    def test_number_area(self):
        side = 100
        result = area(side)
        assert result == 10000

    def test_zero_area(self):
        side = 0
        result = area(side)
        assert result == 0

    def test_negative_area(self):
        side = -5
        with pytest.raises(ValueError, match="Length can't have\
                            a negative value"):
            area(side)


class TestPerimeter:
    def test_number_perimeter(self):
        side = 50
        result = perimeter(side)
        assert result == 200

    def test_zero_perimeter(self):
        side = 0
        result = perimeter(side)
        assert result == 0

    def test_negative_perimeter(self):
        side = -10
        with pytest.raises(ValueError, match="Length can't have\
                            a negative value"):
            perimeter(side)
