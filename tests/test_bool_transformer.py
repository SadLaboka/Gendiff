from pytest import fixture
from gendiff.bool_transformer import boolean_to_lower_str


@fixture
def first_dict():
    return {1: False, 2: True, 3: 25}


@fixture
def second_dict():
    return {1: 'a', 2: 'b', 3: 'c'}


def test_boolean_to_lower_str(first_dict, second_dict):
    boolean_to_lower_str(first_dict)
    boolean_to_lower_str(second_dict)
    assert first_dict == {
        1: 'false',
        2: 'true',
        3: 25
    }
    assert second_dict == {
        1: 'a',
        2: 'b',
        3: 'c'
    }
