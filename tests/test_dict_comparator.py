from gendiff.dict_comparator import compare_dicts
from gendiff.parser import construct_dict
from tests.fixtures.expected import EXPECTED_DIFF

first_dict = construct_dict('tests/fixtures/file3.json')
second_dict = construct_dict('tests/fixtures/file4.json')


def test_compare_dicts():
    assert compare_dicts(first_dict, second_dict) == EXPECTED_DIFF
