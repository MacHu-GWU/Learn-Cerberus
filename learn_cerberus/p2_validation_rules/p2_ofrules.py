#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
of rules是指多个用多个限制条件的逻辑与或非来限定一项。

ref: http://docs.python-cerberus.org/en/stable/validation-rules.html#of-rules
"""

import cerberus


def example_allof():
    """logic and.

    ref: http://docs.python-cerberus.org/en/stable/validation-rules.html#allof
    """
    schema = {
        "value": {
            "type": "number",
            "allof": [{"min": 25}, {"max": 75}],
        },
    }
    v = cerberus.Validator(schema)
    assert v.validate({"value": 25}) is True
    assert v.validate({"value": 50}) is True
    assert v.validate({"value": 75}) is True

    assert v.validate({"value": 0}) is False
    assert v.validate({"value": 100}) is False

if __name__ == "__main__":
    """
    """
    example_allof()


def example_anyof():
    """logic or.

    ref: http://docs.python-cerberus.org/en/stable/validation-rules.html#anyof
    """

    schema = {
        "value": {
            "type": "number",
            "anyof": [{"max": 25}, {"min": 75}],
        },
    }
    v = cerberus.Validator(schema)
    assert v.validate({"value": 25}) is True
    assert v.validate({"value": 75}) is True

    assert v.validate({"value": 50}) is False

if __name__ == "__main__":
    """
    """
    example_anyof()


def example_noneof():
    """logic or.

    ref: http://docs.python-cerberus.org/en/stable/validation-rules.html#noneof
    """

    schema = {
        "value": {
            "type": "number",
            "noneof": [{"max": 25}, {"min": 75}],
        },
    }
    v = cerberus.Validator(schema)
    assert v.validate({"value": 25}) is False
    assert v.validate({"value": 75}) is False

    assert v.validate({"value": 50}) is True

if __name__ == "__main__":
    """
    """
    example_noneof()


def example_oneof():
    """logic or.

    ref: http://docs.python-cerberus.org/en/stable/validation-rules.html#oneof
    """

    schema = {
        "value": {
            "type": "number",
            "oneof": [{"min": 25, "max": 50}, {"min": 50, "max": 75}],
        },
    }
    v = cerberus.Validator(schema)
    assert v.validate({"value": 25}) is True
    assert v.validate({"value": 75}) is True

    assert v.validate({"value": 50}) is False

if __name__ == "__main__":
    """
    """
    example_oneof()
