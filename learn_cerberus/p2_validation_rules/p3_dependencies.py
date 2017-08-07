#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref: http://docs.python-cerberus.org/en/stable/validation-rules.html#dependencies
"""

import cerberus


def example_dependencies():
    # exists dependentcies
    schema = {"field1": {"required": False},
              "field2": {"required": False, "dependencies": ["field1"]}}
    v = cerberus.Validator(schema)
    assert v.validate({"field1": 7}) is True
    assert v.validate({"field2": 7}) is False  # field2 requires field 1
    assert v.validate({"field1": 1, "field2": 7}) is True

    # list dependentcies
    schema = {"field1": {"required": False},
              "field2": {"required": True, "dependencies": {"field1": ["one", "two"]}}}
    v = cerberus.Validator(schema)
    # field2 requires field 1 is "one" or "two"
    assert v.validate({"field1": 1, "field2": 7}) is False
    assert v.validate({"field1": "one", "field2": 7}) is True

    # dict dependentcies
    schema = {"field1": {"required": False},
              "field2": {"required": True, "dependencies": {"field1": "one"}}}
    v = cerberus.Validator(schema)
    # field2 requires field 1 is "one"
    assert v.validate({"field1": 1, "field2": 7}) is False
    assert v.validate({"field1": "one", "field2": 7}) is True

    # dot notation
    schema = {
        'test_field': {'dependencies': ['a_dict.foo', 'a_dict.bar']},
        'a_dict': {
            'type': 'dict',
            'schema': {
                'foo': {'type': 'string'},
                'bar': {'type': 'string'}
            }
        }
    }
    v = cerberus.Validator(schema)
    document = {'test_field': 'foobar', 'a_dict': {'foo': 'foo'}}
    assert v.validate(document) is False
    assert v.errors == {'test_field': ["field 'a_dict.bar' is required"]}

if __name__ == "__main__":
    """
    """
    example_dependencies()
