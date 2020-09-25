from scripts.chp2.mapmaker import Point
import pytest


def tests_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    # get_lat_long() == (14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)

# using exception handling
def test_invalid_point_generation():
    # with pytest.raises(Exception) as exp:
    # raise exception
    with pytest.raises(ValueError) as exp:
        Point('Buenos Aires', 12.11386, -555.08269)
    # breakpoint()
    assert str(exp.value) == "Invalid latitude, longitude combination"

    with pytest.raises(ValueError) as exp:
        Point(5, 12.11386, -55.08269)
    assert str(exp.value) == "City name provided must be a string"

"""
Challenges 
- Supply city name that can only be a string object
- Throw an error if another data type is provided
- Begin writing from the test and run pytest to spot the test failure
"""

