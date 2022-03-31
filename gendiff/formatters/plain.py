from gendiff.status_constants import (
    ADDED,
    REMOVED,
    NESTED,
    CHANGED,
)


def format_to_plain(diff: dict, path="") -> str:
    """Formats diff to plain output-format"""
    output = []
    for key, node in diff.items():
        current_path = path_constructor(path, key)
        node_status = node.get("status")
        node_value = node.get("value")
        if node_status == NESTED:
            output.append(format_to_plain(node_value, current_path))
        elif node_status == CHANGED:
            output.append(
                "Property '{0}' was updated. "
                "From {1} "
                "to {2}".format(
                    current_path,
                    checks_complex(node.get('first_value')),
                    checks_complex(node.get('second_value'))
                ))
        elif node_status == REMOVED:
            output.append(
                f"Property '{current_path}' was removed"
            )
        elif node_status == ADDED:
            output.append(
                f"Property '{current_path}' was added with value: "
                f"{checks_complex(node_value)}"
            )
    return '\n'.join(output)


def checks_complex(value):
    """
    Checks type of value and returns '[complex value]' if type is a dict
    """
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, int):
        return f"{value}"
    if value in ("true", "null", "false"):
        return value
    return f"'{value}'"


def path_constructor(path, key):
    """Makes path-string"""
    return path + f'.{key}' if path else key
