#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cerberus

def example_allow_unknown():
    schema = {"name": {"type": "string"}}
    v = cerberus.Validator(schema)
    result = v.validate({"name": "John", "age": 32})
    assert result is False
    assert v.errors == {"age": ["unknown field"]}
    
    # usage 1
    schema = {"name": {"type": "string"}}
    v = cerberus.Validator(schema, allow_unknown=True)
    result = v.validate({"name": "John", "age": 32})
    assert result is True
    assert v.errors == {}
    
    # usage 2
    schema = {"name": {"type": "string"}}
    v = cerberus.Validator(schema)
    v.allow_unknown = True
    result = v.validate({"name": "John", "age": 32})
    assert result is True
    assert v.errors == {}
    
    # usage 3, for nested field
    schema = {
        "name": {"type": "string"},
        "profile": {
            "type": "dict",
            "schema": {
                "email": {"type": "string"},
                "phone": {"type": "string"},
            },
        }
    }
    v = cerberus.Validator(schema)
    result = v.validate({"name": "John", "profile": {"age": 32}})
    assert result is False
    assert v.errors == {"profile": [{"age": ["unknown field"]}]}
    
    schema = {
        "name": {"type": "string"},
        "profile": {
            "type": "dict",
            "allow_unknown": True,
            "schema": {
                "email": {"type": "string"},
                "phone": {"type": "string"},
            },
        }
    }
    v = cerberus.Validator(schema)
    result = v.validate({"name": "John", "profile": {"age": 32}})
    assert result is True
    assert v.errors == {}
    
if __name__ == "__main__":
    """
    """
    example_allow_unknown()