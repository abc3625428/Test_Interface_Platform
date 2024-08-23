
from operationexcel import OperationExcel,wirteExceldatas
from common.public import filePath_model

def ceshi1():

    read_data_bigmodel = OperationExcel()
    data = read_data_bigmodel.getExceldatas()

    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []

    for element in data:
        if element["metric"] == 'accuracy':
            l1.append(element)

        if element["metric"] == 'p_precision':

            l2.append(element)
        if element["metric"] == 'p_recall':
            l3.append(element)
        if element["metric"] == 'n_precision':
            l4.append(element)
        if element["metric"] == 'n_recall':
            l5.append(element)


    ls = l1+l2+l3+l4+l5


    wirteExceldatas(ls)
    return True


def ceshi2():
    read_data_bigmodel = OperationExcel()
    data = read_data_bigmodel.getExceldatas()

    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []

    for element in data:


        if element["metric"] == 'p_precision':
            l2.append(element)
        if element["metric"] == 'p_recall':
            l3.append(element)


    ls = l2 + l3

    wirteExceldatas(ls)
    return True

def ceshi3():
    read_data_bigmodel = OperationExcel()
    data = read_data_bigmodel.getExceldatas()

    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []

    for element in data:

        di = {}

        if element["dataset"] in di:
            di(element)
        if element["metric"] == 'p_recall':
            l3.append(element)


    ls = l2 + l3

    wirteExceldatas(ls)
    return True

import pandas as pd


read_data_bigmodel = OperationExcel()
data = read_data_bigmodel.getExceldatas()

print(data)
res = {}
for item in data:

    if item['metric'] == 'p_recall' or item['metric'] == 'p_precision':

        if item['dataset'] not in res:
            dataset_value = item['dataset']
            vllm_value = item['vllm']
            etric_value = item['metric']
            result= {etric_value:vllm_value}
            res[dataset_value] = result
        else:
            ls = []
            ls.append(res[item['dataset']])
            dataset_value = item['dataset']

            vllm_value = item['vllm']
            etric_value = item['metric']
            ls.append({etric_value:vllm_value})
            res[dataset_value] = ls


wirteExceldatas(res)

