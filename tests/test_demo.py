import Demo


def test_get_data():
    results = Demo.get_data()
    assert len(results) == 100
