from tests.fixtures.expected import EXPECTED_DIFF, FILE3_FILE4_PLAIN
from gendiff.formatters.plain import format_to_plain, checks_complex


def test_format_to_plain():

    assert format_to_plain(EXPECTED_DIFF, FILE3_FILE4_PLAIN)


def test_checks_complex():
    dict1 = {}
    dict2 = {'a': 2}
    complex_value = '[complex value]'

    assert checks_complex(dict1) == complex_value
    assert checks_complex(dict2) == complex_value
    assert checks_complex('false') == 'false'
    assert checks_complex('asdf') == "'asdf'"
