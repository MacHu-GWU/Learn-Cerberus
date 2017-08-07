#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

empty能限制字符串不得为空

ref: http://docs.python-cerberus.org/en/stable/validation-rules.html#empty
"""

import cerberus

def example_empty():
    schema = {"name": {"type": "string", "empty": False}}
    v = cerberus.Validator(schema)
    assert v.validate({"name": ""}) is False
    assert v.errors == {"name": ["empty values not allowed"]}

if __name__ == "__main__":
    """
    """
    example_empty()