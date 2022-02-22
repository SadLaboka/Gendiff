from gendiff.formatters.stylish import dict_to_string
from tests.fixtures.expected import (
    EXPECTED_STRING1,
    EXPECTED_STRING2,
    EXPECTED_STRING3
)

DICT1 = {'wow': 'so much'}
DICT2 = {'abc': 12345, 'deep': {'id': 45}}


def test_dict_to_string():
    assert dict_to_string(DICT1, depth=0) == EXPECTED_STRING1
    assert dict_to_string(DICT1, depth=1) == EXPECTED_STRING2
    assert dict_to_string(DICT2, depth=0) == EXPECTED_STRING3
