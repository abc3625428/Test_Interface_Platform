
import requests
import json

def get_value(res, keys):

    if res.status_code != 200:
        return False

    try:
        response_json = res.json()
        res = json.loads(response_json)
        for key,value in res.items():
            if keys ==response_json[key]:
                return response_json[value]
            else:
                return None
        # return response_json[value] if key in response_json else None
    except res.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except ValueError as e:
        print(f"Invalid JSON: {e}")
        return None


def get_jsonvalue(res, keys="token"):

    for k,v in res.items():
        if k == keys:
            return v
        if type(v) is dict:
            for key,value in v.items():
                if key == keys:
                    return value


def res_get_ls(data):
    for key,value in data.items():
        if isinstance(value,list):
            return value
        else:
            for k,y in value.items():
                if isinstance(y,list):
                    return y

def res_get_dc(data,target):
    list = []
    for i in data:
        for key,value in i.items():
            if target == key:
                list.append(value)
    return list

def res_get_value(data,target):

    return res_get_dc(res_get_ls(data),target)


def aig_res_get_list(data):
    li = []
    for key, val in data.items():
        if isinstance(val, list):
            li.append(val)
        elif isinstance(val, dict):
            li.extend(aig_res_get_list(val))

    return list(filter(None, li))