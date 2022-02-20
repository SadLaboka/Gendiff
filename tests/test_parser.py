from gendiff.parser import construct_dict, boolean_to_lower_str


def test_boolean_to_lower_str():
    first_dict = {1: False, 2: True, 3: 25}
    second_dict = {1: 'a', 2: 'b', 3: 'c'}
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


def test_construct_dict_with_json():
    filepath = 'tests/fixtures/file1.json'
    assert construct_dict(filepath) == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": "false"
    }


def test_yaml_to_dict():
    filepath = 'tests/fixtures/file1.yml'
    assert construct_dict(filepath) == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": "false"
    }
