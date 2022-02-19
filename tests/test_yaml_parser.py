from gendiff.yaml_parser import yaml_to_dict


def test_yaml_to_dict():
    filepath = 'tests/fixtures/file1.yml'
    assert yaml_to_dict(filepath) == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
