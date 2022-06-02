

### Validation Functions

def valid_string_list(obj:dict, key:str) -> bool:
    """Validation function that returns True if the following
    conditions are met:
        * key is a dict key of obj and obj is a dictionary
        * obj[key] is an iterable
        * obj[key] has only string inside it

    Args:
        obj (dict): Object to be validated
        key (str): Value to be validated as a key of obj
        and to validate a valid list of strings

    Returns:
        bool: Returns True if all conditions are met,
        otherwise return False
    """
    if (not valid_dict_key(obj, key)):
        return False
    
    try:
        obj_iter = iter(obj[key])
    except TypeError as e:
        return False
    
    for s in obj_iter:
        if (type(s)!=str):
            return False
    
    return True

def valid_order_param(obj:dict, key:str) -> bool:
    """Validation function that returns True if the following
    conditions are met:
        * key is a dict key of obj and obj is a dictionary
        * obj[key] is an iterable
        * obj[key] has only string inside it

    Args:
        obj (dict): _description_
        key (str): _description_

    Returns:
        bool: _description_
    """
    if (not valid_dict_key(obj, key)):
        return False
    
    if (type(obj[key])!=str):
        return False
    
    if (obj[key] not in ['asc', 'desc']):
        return False
    
    sorted(obj[key])
    
    return True

def valid_dict_key(obj:dict, key:str) -> bool:
    """Validation function that verifies if obj is a Python dicionary,
    key is a key of this dicitonary and key's type is string,

    Args:
        obj (dict): Object to be validated as a dict
        key (str): String key that must be one of the dict's keys.

    Returns:
        bool: Returns True if all conditions are met,
        otherwise return False.
    """
    if (type(obj)!=dict):
        return False
    
    if (type(key)!=str):
        return False
    
    if (key not in obj):
        return False
    
    return True

