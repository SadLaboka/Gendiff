from gendiff.parser import construct_dict


def generate_diff(filepath1: str, filepath2: str) -> str:
    """Generates difference between 2 files"""
    file1 = construct_dict(filepath1)
    file2 = construct_dict(filepath2)
    set_of_keys = set(file1)
    set_of_keys.update(file2)
    difference = '{\n'
    for key in sorted(set_of_keys):
        if key in file1 and key not in file2:
            difference += f'  - {key}: {file1[key]}\n'
        elif key not in file1 and key in file2:
            difference += f'  + {key}: {file2[key]}\n'
        elif key in file1 and key in file2:
            if file1[key] != file2[key]:
                difference += f'  - {key}: {file1[key]}\n'
                difference += f'  + {key}: {file2[key]}\n'
            else:
                difference += f'    {key}: {file1[key]}\n'
    return difference + '}'
