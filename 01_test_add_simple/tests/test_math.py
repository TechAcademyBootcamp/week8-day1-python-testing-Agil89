from scripts.math_lib import add

def test_add1():
    given_value = 1
    expected_result = 2
    actual_result = add(given_value)
    assert expected_result == actual_result

def test_add2():
    given_value = -1
    expected_result = 0
    actual_result = add(given_value)
    assert expected_result == actual_result