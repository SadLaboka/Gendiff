from gendiff.diff_generator import generate_diff
from tests.fixtures.expected import (
    file1_file2_json,
    file1_file1_json,
    file2_file2_json
)


def test_generate_diff_json():
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'

    assert generate_diff(file1_path, file2_path) == file1_file2_json
    assert generate_diff(file1_path, file1_path) == file1_file1_json
    assert generate_diff(file2_path, file2_path) == file2_file2_json


def test_generate_diff_yaml():
    file1_path = 'tests/fixtures/file1.yml'
    file2_path = 'tests/fixtures/file2.yaml'

    assert generate_diff(file1_path, file2_path) == file1_file2_json
    assert generate_diff(file1_path, file1_path) == file1_file1_json
    assert generate_diff(file2_path, file2_path) == file2_file2_json
