#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cerberus

def define_and_validate():
    # define a schema
    schema = {"name": {"type": "string"}}
    
    # create a validator instance
    v = cerberus.Validator(schema)
    
    # validate
    document = {"name": "John"}
    result = v.validate(document)
    assert result is True
    
    # fetch validated document
    assert v.document == {"name": "John"}
    
    # fetch errors
    assert v.errors == {}


if __name__ == "__main__":
    """
    """
    define_and_validate()