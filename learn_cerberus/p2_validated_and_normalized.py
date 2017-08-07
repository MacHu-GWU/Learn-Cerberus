#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cerberus

schema = {"name": {"type": "string"},
          "age": {"type": "integer", "coerce": int}}
v = cerberus.Validator(schema)

document = {"name": "John", "age": 32}
result = v.validate(document)
assert result is True

print(v.document)
print()
