

### Validation Functions

def valid_string_list(obj:dict, key:str) -> bool:
    """Validation function that returns True if the following
    conditions are met:
        * key is a dict key of obj and obj is a dictionary
        * obj[key] is an list
        * obj[key] has only string inside it
    
    Otherwise it returns False
    """
    if (not valid_dict_key(obj, key)):
        return False
    
    if(type(obj[key])!=list):
        return False
    
    for s in obj[key]:
        if (type(s)!=str):
            return False
    
    return True

def valid_order_param(obj:dict, key:str) -> bool:
    """Validation function that returns True if the following
    conditions are met:
        * key is a dict key of obj and obj is a dictionary
        * obj[key] is an string
        * obj[key] has only string inside it
    
    Otherwise it returns False
    """
    if (not valid_dict_key(obj, key)):
        return False
    
    if (type(obj[key])!=str):
        return False
    
    if (obj[key] not in ['asc', 'desc']):
        return False
        
    return True

def valid_dict_key(obj:dict, key) -> bool:
    """Validation function that returns True if the following
    conditions are met:
        * obj is a Python dicionary
        * key is a key of obj

    Otherwise it returns False.
    """
    if (type(obj)!=dict):
        return False
    
    if (key not in obj):
        return False
    
    return True

