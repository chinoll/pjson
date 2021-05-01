import json
import re
def _dumps(c):
    x = dir(c)
    attr_dict = {}
    for i in x:
        try:
            if re.match('__[a-zA-Z_]*__',i):
                continue
            attr_dict[i] = getattr(c,i)
        except:
            pass
    for i in attr_dict:
        if type(attr_dict[i]) in [int,str,dict,list,set]:
            continue
        if isinstance(attr_dict[i],object):
            attr_dict[i] = _dumps(attr_dict[i])
    return attr_dict

def dumps(c):
    x = dir(c)
    attr_dict = {}
    for i in x:
        try:
            if re.match('__[a-zA-Z_]*__',i):
                continue
            attr_dict[i] = getattr(c,i)
        except:
            pass
    for i in attr_dict:
        if type(attr_dict[i]) in [int,str,dict,list,set]:
            continue
        if isinstance(attr_dict[i],object):
            attr_dict[i] = _dumps(attr_dict[i])
    return json.dumps(attr_dict)