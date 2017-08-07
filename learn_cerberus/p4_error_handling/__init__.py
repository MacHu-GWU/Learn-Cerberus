#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref: http://docs.python-cerberus.org/en/stable/errors.html
"""

from __future__ import print_function
import cerberus

def example_error_handling():
    schema = {"name": {"type": "string"}}
    v = cerberus.Validator(schema)
    assert v.validate({"name": 1}) is False
    
    # v._errors储存了当前触发的所有错误的实例
    print(v._errors)
    print(v.document_error_tree)
    
#     print(cerberus.errors.BAD_TYPE)
    
if __name__ == "__main__":
    """
    """
    example_error_handling()
