# -*- coding: utf-8 -*-

def res_get_ls(data):

    li= []
    for key,val in data.items():
        if isinstance(val, list):
            li.append(val)
        elif isinstance(val, dict):
            li.extend(res_get_ls(val))

    return list(filter(None,li))


def find_target(str, target):
    li = []

    for i in str:
        if isinstance(i,dict):
            for key, value in i.items():
                if target == key:
                    li.append(value)
                elif isinstance(value, dict):
                    for key, va in value.items():
                        if target == key:
                            li.append(va)
                elif isinstance(value, list):
                    for i in value:
                        if isinstance(i,dict):
                            for key, va in i.items():
                                if key == target:
                                    li.append(va)
    return li

def chang_list(res):

    return [item for sublist in res for item in sublist]


def aig_get_target_value(res, target):

    li = chang_list(res_get_ls(res))
    return find_target(li, target)