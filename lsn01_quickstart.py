##encoding=utf-8

"""
Validation Rules
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

def basic_usage_example():
    """
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

def list_type_example():
    """对list中的元素的数据类型进行限制
    """
    schema = {"tag": {"type": "list"}}
    v = Validator(schema)
    
    document = {"tag": [1, 2, 3]}
    print(v.validate(document))
    document = {"tag": ["small", "mid", "big"]}
    print(v.validate(document))
    
    schema = {"tag": {"type": "list", "schema": {"type": "string"}}} # has to be string
    v = Validator(schema)
    
    document = {"tag": [1, 2, 3]}
    print(v.validate(document))
    print(v.errors)
    
    document = {"tag": ["small", "mid", "big"]}
    print(v.validate(document))

# list_type_example()

def require_example():
    schema = {"name": {"required": True, "type": "string"}, "age": {"type": "integer"}}
    v = Validator(schema)
    
    document = {"age": 10}
    print(v.validate(document))
    print(v.errors)
    
# require_example()

def nullable_example():
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

def allowed_example():
    """list中的值要求必须是allowed中的子集
    """
    schema = {"role": {"type": "list", "allowed": ["agent", "client", "supplier"]}}
    v = Validator(schema)
    
    print(v.validate({"role": ["agent", "supplier"]}))
    print(v.validate({"role": ["agent", "boss"]}))
    print(v.errors)
    
# allowed_example()

def empty_example():
    schema = {"name": {"type": "string", "empty": False}}
    v = Validator(schema)
    
    document = {"name": ""}
    print(v.validate(document))
    print(v.errors)
    
# empty_example()

def item_example():
    """定义嵌套的字典中的key, value的 data type
    """
    schema = {"rows": {"type": "list", "items": {"sku": {"type": "string"}, "price": {"type": "integer"}}}}
    v = Validator(schema)
    
    document = {"rows": [{"sku": "KT123", "price": 100}]}
    print(v.validate(document, schema))

    document = {"rows": [{"sku": 123, "price": "100"}]}
    print(v.validate(document, schema))
    print(v.errors)
    
# item_example()

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