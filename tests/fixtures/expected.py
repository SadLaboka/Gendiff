"""Expected values for tests"""
from gendiff.status_constants import (
    ADDED,
    CHANGED,
    UNCHANGED,
    REMOVED,
    NESTED
)

EXPECTED_DIFF = {
    "common": {
        "status": NESTED,
        "value": {
            "follow": {"status": ADDED, "value": "false"},
            "setting1": {"status": UNCHANGED, "value": "Value 1"},
            "setting2": {"status": REMOVED, "value": 200},
            "setting3": {"status": CHANGED, "first_value": "true", "second_value": "null"},
            "setting4": {"status": ADDED, "value": "blah blah"},
            "setting5": {"status": ADDED, "value": {"key5": "value5"}},
            "setting6": {"status": NESTED, "value": {
                "doge": {"status": NESTED, "value": {
                    "wow": {"status": CHANGED, "first_value": "", "second_value": "so much"}
                }},
                "key": {"status": UNCHANGED, "value": "value"},
                "ops": {"status": ADDED, "value": "vops"}
            }}
        }
    },
    "group1": {"status": NESTED, "value": {
        "baz": {"status": CHANGED, "first_value": "bas", "second_value": "bars"},
        "foo": {"status": UNCHANGED, "value": "bar"},
        "nest": {"status": CHANGED, "first_value": {"key": "value"}, "second_value": "str"}
    }},
    "group2": {"status": REMOVED, "value": {
        "abc": 12345,
        "deep": {"id": 45}
    }},
    "group3": {"status": ADDED, "value": {"deep": {"id": {"number": 45}},
                                          "fee": 100500}}
}

EXPECTED_STRING1 = """{
        wow: so much
    }"""

EXPECTED_STRING2 = """{
            wow: so much
        }"""

EXPECTED_STRING3 = """{
        abc: 12345
        deep: {
            id: 45
        }
    }"""

FILE3_FILE4_STRING = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:"""
FILE3_FILE4_STRING += ' '
FILE3_FILE4_STRING += """
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

FILE1_FILE2_JSON = '{"follow": {"status": "REMOVED", "value": "false"},' \
                   ' "host": {"status": "UNCHANGED", "value": "hexlet.io"},' \
                   ' "proxy": {"status": "REMOVED", "value": "123.234.53.22"},' \
                   ' "timeout": {"status": "CHANGED", "first_value": 50, "second_value": 20},' \
                   ' "verbose": {"status": "ADDED", "value": "true"}}'

FILE1_FILE2_STRING = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

FILE1_STRING = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""

FILE2_STRING = """{
    host: hexlet.io
    timeout: 20
    verbose: true
}"""

FILE3_STRING = """{
    common: {
        setting1: Value 1
        setting2: 200
        setting3: true
        setting6: {
            doge: {
                wow:"""
FILE3_STRING += ' '
FILE3_STRING += """
            }
            key: value
        }
    }
    group1: {
        baz: bas
        foo: bar
        nest: {
            key: value
        }
    }
    group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
}"""

FILE4_STRING = """{
    common: {
        follow: false
        setting1: Value 1
        setting3: null
        setting4: blah blah
        setting5: {
            key5: value5
        }
        setting6: {
            doge: {
                wow: so much
            }
            key: value
            ops: vops
        }
    }
    group1: {
        baz: bars
        foo: bar
        nest: str
    }
    group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

FILE3_FILE4_JSON = '{"common": {"status": "NESTED", "value": {"follow": {"status": "ADDED", "value": "false"},' \
                   ' "setting1": {"status": "UNCHANGED", "value": "Value 1"},' \
                   ' "setting2": {"status": "REMOVED", "value": 200},' \
                   ' "setting3": {"status": "CHANGED", "first_value": "true", "second_value": "null"},' \
                   ' "setting4": {"status": "ADDED", "value": "blah blah"},' \
                   ' "setting5": {"status": "ADDED", "value": {"key5": "value5"}},' \
                   ' "setting6": {"status": "NESTED",' \
                   ' "value": {"doge": {"status": "NESTED", "value": {"wow": {"status": "CHANGED", "first_value": "",' \
                   ' "second_value": "so much"}}}, "key": {"status": "UNCHANGED", "value": "value"},' \
                   ' "ops": {"status": "ADDED", "value": "vops"}}}}}, "group1": {"status": "NESTED",' \
                   ' "value": {"baz": {"status": "CHANGED", "first_value": "bas", "second_value": "bars"},' \
                   ' "foo": {"status": "UNCHANGED", "value": "bar"}, "nest": {"status": "CHANGED",' \
                   ' "first_value": {"key": "value"}, "second_value": "str"}}}, "group2": {"status": "REMOVED",' \
                   ' "value": {"abc": 12345, "deep": {"id": 45}}}, "group3": {"status": "ADDED",' \
                   ' "value": {"deep": {"id": {"number": 45}}, "fee": 100500}}}'

FILE3_FILE4_PLAIN = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
