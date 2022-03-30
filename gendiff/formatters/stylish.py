from gendiff.status_constants import (
    ADDED,
    REMOVED,
    NESTED,
    CHANGED,
    UNCHANGED
)


def format_to_stylish(diff: dict, depth=0) -> str:
    """Formats diff to json-like style for output"""
    output = []
    indent = '    ' * depth
    for key, node in diff.items():
        node_status = node.get('status')
        node_value = node.get('value')
        if node_status == NESTED:
            output.extend([
                f'{indent}    {key}: {{',
                format_to_stylish(node_value, depth=depth + 1),
                f'{indent}    }}'
            ])
        elif node_status == CHANGED:
            output.extend([
                f'{indent}  - {key}: '
                f'{get_value(node.get("first_value"), depth)}',
                f'{indent}  + {key}: '
                f'{get_value(node.get("second_value"), depth)}'
            ])
        else:
            view = get_status_view(node_status)
            output.append(
                f'{indent}{view}{key}: {get_value(node_value, depth)}'
            )
    if not depth:
        output = ['{'] + output + ['}']
    return '\n'.join(output)


def get_status_view(node_status: str) -> str:
    """Gets a view for the status type"""
    views = {
        ADDED: "  + ",
        REMOVED: "  - ",
        UNCHANGED: "    "
    }
    return views.get(node_status)


def get_value(item, depth) -> str:
    """
    Checks type of value and returns dict_to_string function if type is a dict
    """
    if isinstance(item, dict):
        return dict_to_string(item, depth)
    return item


def dict_to_string(item: dict, depth: int) -> str:
    """Transforms dict to string"""
    result = ['{']
    indent = '    '
    for key, value in item.items():
        value = get_value(value, depth=depth + 1)
        result.append(
            f'{indent * (depth + 2)}{key}: {value}'
        )
    result.append(f'{indent * (depth + 1)}}}')
    return '\n'.join(result)
