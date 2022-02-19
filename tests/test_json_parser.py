from gendiff.json_parser import json_to_dict


def test_json_to_dict():
    filepath = 'tests/fixtures/file1.json'
    assert json_to_dict(filepath) == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
