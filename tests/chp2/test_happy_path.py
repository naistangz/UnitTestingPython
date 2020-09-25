import pytest
from scripts import data_processor

def test_csv_reader_header_fields(process_data):
    """
    Happy Path testing to ensure processed data
    contains the right header fields
    """
    data = process_data
    header_fields = list(data[0].keys())
    assert header_fields == [
        'Country',
        'City',
        'State_Or_Province',
        'Lat',
        'Long',
        'Altitude'
    ]


def test_csv_reader_data_contents(process_data):
    """
    Another happy test to examine each row
    has appropriate data type per field
    """
    data = process_data
    # breakpoint()  # python debugging

    # check row types
    for row in data:
        assert (isinstance(row['Country'], str))
        assert (isinstance(row['City'], str))
        assert (isinstance(row['State_or_Province'], str))
        assert (isinstance(row['Lat'], float))
        assert (isinstance(row['Long'], float))
        assert (isinstance(row['Altitude'], float))
        # operations

    assert len(data) == 180
    assert data[0]['Country'] == 'Andorra'
    assert data[179]['Country'] == 'United States'

    # basic data checks
