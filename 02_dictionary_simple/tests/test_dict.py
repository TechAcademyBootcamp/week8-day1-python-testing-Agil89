from scripts.math_lib import user_full_name


def test_fname():
    givenName = 'Elon'
    givenSurname = 'Musk'
    expected_result = givenName + ' ' + givenSurname
    actual_result = user_full_name()
    assert expected_result == actual_result