# Gendiff

![flake8 and pytest](https://github.com/SadLaboka/python-project-lvl2/actions/workflows/main.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/2f5a2e9ac051c9698f87/maintainability)](https://codeclimate.com/github/SadLaboka/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2f5a2e9ac051c9698f87/test_coverage)](https://codeclimate.com/github/SadLaboka/python-project-lvl2/test_coverage)

Gendiff is a simple CLI-tool to compare two files and show the difference between them

## Installing

```
pip install --user --index-url https://test.pypi.org/simple/ SadLaboka_gendiff
```

## Usage

### As library

```python
from gendiff import generate_diff

diff = generate_diff(file1_path, file2_path, output_format)
```

### As CLI tool

```
> gendiff --help
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

## Comparing 2 flat JSON-files:
<details>
  <summary>Click to show</summary>
  
[![asciicast](https://github.com/SadLaboka/python-project-lvl2/blob/main/docs/json_json.svg)](https://asciinema.org/a/0DK7OpfKQzXHUQJcaac02TarZ)
</details>

## Comparing 2 nested JSON-files:
### Stylish output
<details>
  <summary>Click to show</summary>
  
[![asciicast](https://github.com/SadLaboka/python-project-lvl2/blob/main/docs/nested_json_json.svg)](https://asciinema.org/a/u3wVhAOyc4jxNC05UtK2oLtPr)
</details>

### Plain output
<details>
  <summary>Click to show</summary>
  
[![asciicast](https://github.com/SadLaboka/python-project-lvl2/blob/main/docs/nested_json_plain.svg)](https://asciinema.org/a/9qcFqiPC59XzGTwA4P6x4m8y9)
</details>

### JSON output
<details>
  <summary>Click to show</summary>
  
[![asciicast](https://github.com/SadLaboka/python-project-lvl2/blob/main/docs/nested_json_json_out.svg)](https://asciinema.org/a/O15LPhDQErgzgK8vWz9W8QYUN)
</details>

## Comparing 2 flat YAML-files:
<details>
  <summary>Click to show</summary>
  
[![asciicast](https://github.com/SadLaboka/python-project-lvl2/blob/main/docs/yaml_json.svg)](https://asciinema.org/a/TRuExyOhlyzFV23PI4H6CqYuZ)
</details>
