from gendiff.diff_generator import generate_diff, boolean_to_lower_str


def test_generate_diff():
    with open('tests/fixtures/json1_json2_output.txt') as file:
        json1_json2_output = file.read()
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'

    assert generate_diff(file1_path, file2_path) == json1_json2_output


def test_boolean_to_lower_str():
    assert boolean_to_lower_str(True) == 'true'
    assert boolean_to_lower_str(False) == 'false'
