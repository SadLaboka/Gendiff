from gendiff.diff_generator import generate_diff
from tests.fixtures.expected import (
    FILE1_STRING,
    FILE2_STRING,
    FILE3_STRING,
    FILE4_STRING,
    FILE1_FILE2_JSON,
    FILE1_FILE2_STRING,
    FILE3_FILE4_JSON,
    FILE3_FILE4_STRING,
    FILE3_FILE4_PLAIN
)


def test_generate_diff_json():
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'

    assert generate_diff(file1_path, file2_path) == FILE1_FILE2_STRING
    assert generate_diff(file1_path, file1_path) == FILE1_STRING
    assert generate_diff(file2_path, file2_path) == FILE2_STRING


def test_generate_diff_nested_json():
    file1_path = 'tests/fixtures/file3.json'
    file2_path = 'tests/fixtures/file4.json'

    assert generate_diff(file1_path, file1_path) == FILE3_STRING
    assert generate_diff(file2_path, file2_path) == FILE4_STRING
    assert generate_diff(file1_path, file2_path) == FILE3_FILE4_STRING


def test_generate_diff_yaml():
    file1_path = 'tests/fixtures/file1.yml'
    file2_path = 'tests/fixtures/file2.yaml'

    assert generate_diff(file1_path, file2_path) == FILE1_FILE2_STRING
    assert generate_diff(file1_path, file1_path) == FILE1_STRING
    assert generate_diff(file2_path, file2_path) == FILE2_STRING


def test_generate_diff_nested_yaml():
    file1_path = 'tests/fixtures/file3.yml'
    file2_path = 'tests/fixtures/file4.yml'

    assert generate_diff(file1_path, file2_path) == FILE3_FILE4_STRING


def test_generate_diff_nested_to_plain():
    file1_path = 'tests/fixtures/file3.json'
    file2_path = 'tests/fixtures/file4.json'

    assert generate_diff(
        file1_path,
        file2_path,
        output_format="plain") == FILE3_FILE4_PLAIN


def test_generate_diff_to_json():
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'

    assert generate_diff(
        file1_path,
        file2_path,
        output_format="json") == FILE1_FILE2_JSON


def test_generate_diff_nested_to_json():
    file1_path = 'tests/fixtures/file3.json'
    file2_path = 'tests/fixtures/file4.json'

    assert generate_diff(
        file1_path,
        file2_path,
        output_format="json") == FILE3_FILE4_JSON
