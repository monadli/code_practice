from ..convert_string_to_number import string_to_number

def test_valid_cases():
    assert string_to_number("-1") == -1
    assert string_to_number("-0") == 0
    assert string_to_number("0") == 0
    assert string_to_number("1") == 1
    assert string_to_number("10924083") == 10924083
    assert string_to_number("-10924083") == -10924083
