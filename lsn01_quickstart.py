#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
cerberus usage examples, cerberus >= 0.9.1

validation rules

    http://docs.python-cerberus.org/en/latest/usage.html#validation-rules
    
    type: http://docs.python-cerberus.org/en/latest/usage.html#type
        string
        integer
        float
        number (integer or float)
        boolean
        datetime
        dict (formally collections.mapping)
        list (formally collections.sequence, excluding strings)
        set
    
"""
from cerberus import Validator

############
# 基本概念 #
############

def basic_usage_example():
    """
    最基础的例子就是对值的数据类型进行检查。在这里我们定义name项是一个字符串。
    在cerberus默认的设定中如果在schema中没有被定义的项, 是不允许的。当然, 我们
    可以通过修改Validator.allow_unknown = True取消该限制。
    """
    schema = {"name": {"type": "string"}}
    v = Validator(schema)
    
    document = {"name": "John"} # 检查数据类型
    print(v.validate(document))
    
    document = {"name": 123} # 检查数据类型
    print(v.validate(document))
    
    document = {"fullname": "Bill Gates"} # 检查Key是否在schema中被定义
    print(v.validate(document))
    print(v.errors) # print last error. if no error detected in the last check, return empty dict
    
# basic_usage_example()

def allow_unknown_example():
    """默认需要data中所有的key都要在schema中被预定义。而设置allow_unknown = True可以允许出现
    没有被预定义的key
    """
    schema = {"name": {"type": "string", "maxlength": 10}}
    v = Validator(schema)
    print(v.validate({"name": "john", "sex": "M"}))
    print(v.errors)
    
    v.allow_unknown = True
    print(v.validate({"name": "john", "sex": "M"}))
    
# allow_unknown_example()

def required_example():
    """
    在定义中的项在文档中不是都有的情况下, cerberus是允许的。当然我们可以通过设定::
    
        "required": True
        
    来强制要求必须该项必须存在。
    """
    schema = {"lastname": {"type": "string"}, "firstname": {"type": "string"}}
    v = Validator(schema)

    document = {"lastname": "Jackson"} # 检查数据类型
    print(v.validate(document))

    schema = {"lastname": {"type": "string", "required": True}, 
              "firstname": {"type": "string", "required": True}}
    v = Validator(schema)

    document = {"lastname": "Jackson"} # 检查数据类型
    print(v.validate(document))
    print(v.errors)
    
# required_example()

def nullable_example():
    """默认情况下cerberus只要定义了某项, 是不允许该项的值为None的。只有在设置
    了::
    
        "nullable": True
        
    才可以允许None值。
    """
    schema = {"memo": {"type": "string"}}
    v = Validator(schema)
    
    document = {"memo": None}
    print(v.validate(document))
    print(v.errors)
    
    schema = {"memo": {"nullable": True, "type": "string"}}
    v = Validator(schema)
    
    document = {"memo": None}
    print(v.validate(document))
    
# nullable_example()

def allowed_for_single_value():
    """对于值进行限制, 只能使预定义的几个值中的一个。
    """
    schema = {"label": {"type": "integer", "allowed": [1, 2, 3]}}
    v = Validator(schema)
    
    print(v.validate({"label": 1}))
    
# allowed_for_non_array()

###############
# string 类型 #
###############

def max_min_length_example():
    """对于字符串项, 可以限制字符串的长度。
    """
    schema = {"password": {"type": "string", "minlength": 8, "maxlength": 20}}
    v = Validator(schema)
    
    print(v.validate({"password": "123456"}))
    print(v.errors)

    print(v.validate({"password": "abcdefghijklmnopqrstuvwxyz"}))
    print(v.errors)
    
# max_min_length_example()

def regex_example():
    """对字符串进行正则匹配验证。
    """
    email_regex ="([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)" 
    schema = {"email": {"type": "string", "regex": email_regex}}
    v = Validator(schema)
    
    print(v.validate({"email": "example@gmail.com"}))
    
    print(v.validate({"email": "123456"}))
    print(v.errors)
    
# regex_example()

def empty_example():
    """对于字符串项, empty可以限制是否允许空字符串。默认cerberus是允许的。
    """
    schema = {"name": {"type": "string", "empty": False}}
    v = Validator(schema)
    
    document = {"name": ""}
    print(v.validate(document))
    print(v.errors)
    
# empty_example()

#################################################
# integer, float, number(integer or float) 类型 #
#################################################

def max_min_example():
    """对于数值项, 可以限制其最大值和最小值。
    """
    schema = {"value": {"type": "number", "min": 0, "max": 1}}
    v = Validator(schema)
    
    print(v.validate({"value": 1.5}))
    
    print(v.validate({"value": -0.5}))
    print(v.errors)
    
    print(v.validate({"value": 1.5}))
    print(v.errors)
    
# max_min_example()

#############
# list 类型 #
#############

def list_type_example():
    """对list中的元素的数据类型进行限制。
    """
    schema = {"tag": {"type": "list"}}
    v = Validator(schema)
    
    document = {"tag": [1, 2, 3]} # item type are not defined
    print(v.validate(document))
    document = {"tag": ["small", "mid", "big"]}
    print(v.validate(document))
    
    # item in list has to be string
    schema = {"tag": {"type": "list", "schema": {"type": "string"}}}
    v = Validator(schema)

    document = {"tag": ["small", "mid", "big"]}
    print(v.validate(document))
    
    document = {"tag": [1, 2, 3]}
    print(v.validate(document))
    print(v.errors)

# list_type_example()

def allowed_example():
    """对list中的值的取值进行限制。
    
    我们可以通过设定::
    
        "allowed": [item1, item2, ...]
        
    使得list中的值必须是allowed中的元素
    """
    schema = {"role": {"type": "list", "allowed": ["agent", "client", "supplier"]}}
    v = Validator(schema)
    
    print(v.validate({"role": ["agent", "supplier"]}))
    print(v.validate({"role": ["agent", "boss"]}))
    print(v.errors)
    
# allowed_example()

def set_type_example():
    """如果要求list中的元素不可以重复, 那么可以使用set类型。但是注意! 流行的文档
    格式Json,和mongodb中的document, 都不支持python原生set类型。所以该功能在用于
    数据库入库的检查一类的应用, 都要慎用。下一例提供了一种解决方案。
    """
    schema = {"tag": {"type": "set"}}
    v = Validator(schema)
    
    print(v.validate({"tag": set(["drama", "crime"])}))
    
# set_type_example()

def non_repeat_list():
    """cerberus 0.9 提供了一个新功能, 我们可以定义::
    
        "coerce": function
        
    这样在对该项的值进行验证前, 先调用function对值进行处理。这样我们可以对输入的
    list进行一个处理, 剔除掉重复的元素, 然后再进行validate。
    """
    def non_repeat_list(value):
        new_value = list()
        for item in value:
            if item not in new_value:
                new_value.append(item)
        return new_value
    
    schema = {"tag": {"type": "list", "coerce": non_repeat_list}}
    v = Validator(schema)
    
    print(v.validate({"tag": ["drama", "crime", "drama"]}))
    print(v.document) # processed document
    
# non_repeat_list()

def list_of_dict_example():
    """对于list中的值是字典的情况。因为list中的值通常具有同样的数据结构(不然就是
    数据模型设计的失败), 所以里面的字典的模型是可预定义的。
    """
    schema = {
        "rows": {
            "type": "list", 
            "items": {
                "sku": {"type": "string"}, 
                "price": {"type": "integer"},
            },
        },
    }
    v = Validator(schema)
    
    document = {"rows": [{"sku": "KT123", "price": 100}]}
    print(v.validate(document, schema))

    document = {"rows": [{"sku": 123, "price": "100"}]}
    print(v.validate(document, schema))
    print(v.errors)
    
# list_of_dict_example()

###############################
# dict (nested document) 类型 #
###############################

def dict_type_example():
    """对于某一项是字典的情况, 相当于是文档中嵌套文档。cerberus中使用schema项
    来定义子项。
    """
    schema = {
        "customer": {
            "type": "dict",
            "required": True,
            "schema": {
                "firstname": {"type": "string", "required": True},
                "lastname": {"type": "string", "required": True},
                "age": {"type": "integer", "required": True},
                },
        },    
    }
    v = Validator(schema)
    
    document = {"customer": {"firstname": "obama", "lastname": "barrack"}}
    print(v.validate(document))
    print(v.errors)
    
# dict_type_example()

def valueschema_example():
    """对于字典项, 我们可以允许任意多个子项, 但是对于所有的值, 我们可以用
    valueschema进行限制。
    """
    schema = {
        "poker_code": {
            "type": "dict",
            "valueschema": {"type": "integer", "min": 1, "max": 52},
        },
    }
    v = Validator(schema)
    
    document = {"poker_code": {"Ace of Spade": 1}}
    print(v.validate(document))

    document = {"poker_code": {"Joker": 53}}
    print(v.validate(document))
    print(v.errors)
    
# valueschema_example()

def propertychema_example():
    """对于字典项, 我们可以允许任意多个子项, 但是对于所有的值, 我们可以用
    valueschema进行限制。
    """
    schema = {
        "poker_code": {
            "type": "dict",
            "propertyschema": {"type": "string"},
        },
    }
    v = Validator(schema)
    
    document = {"poker_code": {"Ace of Spade": 1}}
    print(v.validate(document))

    document = {"poker_code": {41: 41}}
    print(v.validate(document))
    print(v.errors)
    
# propertychema_example()

##########################################
# *of-rules: anyof, allof, noneof, oneof #
##########################################
def anyof_example():
    """定义: 值需要满足以下几个条件中的任意一个
    除了anyof, 类似的还有: allof, noneof, oneof
    """
    schema = {"value": {"type": "number", "anyof": [{"min": 0, "max": 10}, {"min": 100, "max": 1000}]}}
    v = Validator(schema)
    
    document = {"value": 1}
    print(v.validate(document, schema))
    
    document = {"value": 111}
    print(v.validate(document, schema))
    
    document = {"value": 11}
    print(v.validate(document, schema))
    print(v.errors)
    
# anyof_example()

########
# 杂项 #
########

def dependency_example():
    """通过``dependencies``可以定义某项存在的前提条件是其他项。
    """
    schema = {"level1": {"type": "number"},
              "level2": {"type": "number", "dependencies": ["level1"]}}
    v = Validator(schema)
    
    print(v.validate({"level2": 100}))
    print(v.errors)
    
# dependency_example()



def type_coercion_example():
    """对于定义了coerce: func的field, cerberus会尝试调用func(value)对值进行处理之后再执行validate,
    若期间抛出异常, 则会返回False
    """
    schema = {"value": {"type": "number"}}
    v = Validator(schema)
    
    document = {"value": "1"}
    print(v.validate(document))
    print(v.errors)
    
    schema = {"value": {"type": "number", "coerce": int}}
    v = Validator(schema)
    
    document = {"value": "1"}
    print(v.validate(document))
    print(v.document)
    
# type_coercion_example()

def validated_method_example():
    """validated能返回验证后的document, 下面的代码给出了一种对输入的数据流进行处理的例子。
    """
    schema = {"value": {"type": "number"}}
    v = Validator(schema)
    
    documents = [
        {"value": 1},
        {"value": [1, 2, 3]},
        {"value": 2},
        ]
    valid_documents = [x for x in [v.validated(y) for y in documents] if x is not None]
    print(valid_documents)
    
# validated_method_example()