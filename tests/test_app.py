from src.app import calculate_average, format_summary


def test_calculate_average():
    assert calculate_average(10, 2) == 5.0
    assert calculate_average(10, 0) == 0


def test_format_summary():
    assert format_summary([1, 2]) == "1, 2, "
