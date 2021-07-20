import statistics


def test_variance():
    assert statistics.variance([1, 2, 3, 4, 5]) == 2.5


def test_mean():
    assert statistics.mean([1, 2, 3, 4, 5]) == 3
