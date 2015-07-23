##encoding=utf-8

from __future__ import print_function, unicode_literals
from cerberus import Validator
from cerberus.errors import ERROR_BAD_TYPE
import re

def class_based_custom_validators():
    """自定义你的validtor
    """
    class MyValidator(Validator):
        """
        1. 继承cerberus.Validator
        2. def _validate_<rulename>(self, <rulename>, field, value)
        3. 像使用cerberus.Validator一样使用MyValidator
        """
        def _validate_isodd(self, isodd, field, value):
            """
            first argument: Bool, default is True
            second argument: field name, key name
            third argument: value
            """
            if isodd and not bool(value & 1): #
                self._error(field, "Must be an odd number")
                
    schema = {"oddity": {"isodd": True, "type": "integer"}, "another": {"isodd": True}}
    v = MyValidator(schema)
    print(v.validate({"oddity": 10, "another": 12}))
    print(v.errors)
    print(v.validate({"oddity": 9, "another": 11}))

# class_based_custom_validators()

def function_based_custom_validators():
    """以函数的方式自定义你的validator
    """
    def validate_oddity(field, value, error):
        if not bool(value & 1):
            error(field, "Must be an odd number")
            
    schema = {"oddity": {"validator": validate_oddity}}
    v = Validator(schema)
    print(v.validate({"oddity": 10}))
    print(v.errors)
    
    print(v.validate({"oddity": 9}))
    
# function_based_custom_validators()

def custom_data_types():
    """自定义你的data type
    """
    class MyValidator(Validator):
        def _validate_type_objectid(self, field, value):
            """ Enables validation for `objectid` schema attribute.
        
            :param field: field name.
            :param value: field value.
            """
            if not re.match('[a-f0-9]{16}', value):
                self._error(field, ERROR_BAD_TYPE.format('ObjectId'))
                
    schema = {"_id": {"type": "objectid"}}
    v = MyValidator(schema)
    
    print(v.validate({"_id": "0123456789abcdef"}))
    
    print(v.validate({"_id": "0123456789"}))
    print(v.errors)
    
# custom_data_types()