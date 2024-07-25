# -*- coding: utf-8 -*-



# from flask import app
# def job3():
#     with app.app_context():
#         a = current_app
#         d = current_app.config['DEBUG']
#         a.logger.info("测试数据++++++++++++++++")
#
#
# print(job3())


# def cz(ls,target):
#     l = 0
#     r = len(ls)-1
#     while l<r:
#         mid = (l+r)//2
#         if ls[mid]==target:
#             return mid
#         elif ls[mid] > target:
#             r = mid-1
#         else:
#             l = mid+1
#     return False
#
# ls = list(range(4,100))
#
# # res = cz(ls,target=7)
# # print(res)
#
# def mp(ls):
#     for i in range(len(ls)-1):
#         for j in range(len(ls)-1):
#             if ls[j]>ls[j+1]:
#                 ls[j],ls[j+1]=ls[j+1],ls[j]
#     return ls
#
#
#
# # print(mp(ls))
#
# def part(ls,l,r):
#     tmp = ls[l]
#     while l<r:
#         while l<r and ls[r]>=tmp:
#             r-=1
#         ls[l] = ls[r]
#         while l<r and ls[l]<=tmp:
#             l+=1
#         ls[r] = ls[l]
#     ls[l]=tmp
#     return l
#
# def ks(ls,l,r):
#     if l<r:
#         q = part(ls,l,r)
#         ks(ls,l,q-1)
#         ks(ls,q+1,r)
#
# ls1 = [1,456,23,132,13,13,1,31,46343,32,132,1,321,112,1,51,5,46,4,151,68,486,46,45,631,35,321]
# # print(ls1)
# # ks(ls1,0,len(ls1)-1)
# # print("222222",ls1)
#
#
# def partition(li,left,right):
#     tmp = li[left]
#     while left < right:
#         while left<right and li[right]>= tmp:#从右面找比tmp小的数
#             right -=1
#         li[left] = li[right]
#         while left < right and li[left] <= tmp:
#             left += 1
#         li[right]=li[left]
#     li[left] = tmp
#     return left
#
# def quick_sort(li,left,right):
#     if left<right:
#         mid = partition(li, left, right)
#         quick_sort(li,left,mid-1)
#         quick_sort(li,mid+1,right)
# # quick_sort(ls1,0,len(ls1)-1)
# # print(ls1)
#
# def partgb(ls,l,mid,r):
#     li=[]
#     i = l
#     j=mid+1
#     while i<=mid and j<=r:
#         if ls[i] < ls[j]:
#             li.append(ls[i])
#             i+=1
#         else:
#             li.append(ls[j])
#             j+=1
#     while i<=mid:
#         li.append(ls[i])
#         i += 1
#     while j <= r:
#         li.append(ls[j])
#         j += 1
#     ls[l:r+1]=li
# # ls2 = [0,2,3,4,5,6,1,2,3,4,5,6,8,10,55,66]
# # print(ls2)
# # partgb(ls2,0,5,len(ls1)-1)
# # print(ls2)
#
# def merge(li,low,mid,high):
#     i = low
#     j = mid+1
#     ltmp = []
#
#     while i<=mid and j<=high:
#         if li[i] < li[j]:
#             ltmp.append(li[i])
#             i += 1
#         else:
#             ltmp.append(li[j])
#             j += 1
#     print(1,ltmp)
#     while i <= mid:
#         ltmp.append(li[i])
#         i += 1
#     while j <= high:
#         ltmp.append(li[j])
#         j += 1
#     li[low:high+1] = ltmp
#
#
# ls2 = [0,2,3,4,5,6,1,2,3,4,5,6,8,10,55,66]
# l3 = [48646,5,5,4,4,64,64,6,46,48,4,64,684,68,468,4,64,64,6,8464,13,13,4,6,9,87,964,6,1,68,98,4,6,6,8498,7,6,84,46]
#
# m = merge(ls2,0,5,len(ls2)-1)
#
#
# def merge_sort(ls,l,r):
#     if l<r:
#         mid = (l+r)//2
#         merge_sort(ls,l,mid)
#         merge_sort(ls,mid+1,r)
#         merge(ls,l,mid,r)
#
#
#
#
#
#
# str = 'a;f;akf;af;afm;afm;afm;fmpqnpnp'
# s = str[::-1]
#
# s1 = ''
# for i in str:
#     s1 = i+s1
#
#
#
# def confim_balense(str):
#     if len(str) <=1:
#         return True
#
#     if len(str)%2==0:
#         mid = len(str)//2
#         j  = mid - 1
#         str1 = str[0:mid]
#         str1 = str1[::-1]
#         str2 = str[mid:len(str)]
#         if str1 == str2:
#             return True
#         else:
#             return False
#     else:
#         mid = len(str)//2
#         i = mid-1
#         j  = mid + 1
#         if str[0:i] == str[j:len(str)]:
#             return True
#         else:
#             return False
#
# print(confim_balense(str="112211"))




def longsonstr(str):

    #遍历整个字符串，找到相等的两个字符
    num = []
    ls = []
    for i in range(len(str)-1):
        for j in range(i+1,len(str)-1):
            if len(ls) < 1:
                ls.append(j)

            if j != i:
                ls.append(j)
            else:
                ls.append(j)
                num.append(len(ls))
                print(num,ls)
                ls = []
    mu = max(num)
    print(mu)

    # st = ''.join(mu)
    # print(st)
    #每次找到相等字符记录字符串长度
    #如果找到的字符串长度大约原始的字符串替换原来的字符串
    #输出最长字符串长度



def lengthOfLongestSubstring( s):
    if len(s) ==0:
        return 0
    if len(s) ==1:
        return 1
    li = []
    ls = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[j] not in li :
                li.append(s[j])
            elif s[j]==s[-1]:
                ls.append(len(li))
            else:
                ls.append(len(li))
                li = []
    target = max(ls)
    return target

str1 = 'abb'


import pytest
import requests




def get_lists_from_dict(d):
    lists = []
    if isinstance(d, list):
        lists.extend(get_lists_from_dict(d))
    elif isinstance(d, dict):
        for key, value in d.items():
            if isinstance(value, list):
                lists.append(value)
            elif isinstance(value, dict):
                lists.extend(get_lists_from_dict(value))
    else:
        return [d]

    return lists



import json
def js_get(data):

    target  = data['data']['data']['jobCardList']
    return target

# @pytest.mark.parametrize('target', list(range(1, 30, 1)))
# def test_cpc_search_word_list():
#     s = "010"
#     url = "https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job"
#     data = {"mainSearchPcConditionForm":"{\"city\": \"410\", \"dq\": \"410\", \"pubTime\": \"\", \"currentPage\": 0, \"pageSize\": 40,\"key\": \"测试\", \"suggestTag\": \"\", \"workYearCode\": \"0\", \"compId\": \"\", \"compName\": \"\",\"compTag\": \"\", \"industry\": \"\", \"salary\": \"\", \"jobKind\": \"\", \"compScale\": \"\",\"compKind\": \"\", \"compStage\": \"\", \"eduLevel\": \"040\"}",
#                  "passThroughForm":"{\"scene\": \"input\", \"skId\": \"\", \"fkId\": \"\", \"ckId\": \"wf66llskcd3lfhhxqob6e9dtj7oyhb10\"}"}
#
#     header = {
#
#         'X-Client-Type': 'web',
#         'X-Fscp-Std-Info': '{"client_id": "40108"}',
#         'X-Fscp-Trace-Id': '0519960d-bf32-4c76-b6a0-f88b54ab3c33',
#         'X-Fscp-Version': '1.1',
#         'X-Requested-With': 'XMLHttpRequest'
#
#     }
#
#     re = requests.post(url=url, headers=header, data=data,verify=True)
#
#
#
#     from aig_get_value_tool import aig_get_target_value
#     res = aig_get_target_value(re.json(),'requireEduLevel')
#     for i in res:
#         assert "本科" in i
#     return res
#
#
#
# print(test_cpc_search_word_list())

# ta = {"city": "410", "dq": "410", "pubTime": "", "currentPage": 0, "pageSize": 40, "key": "测试", "suggestTag": "",
#       "workYearCode": "0", "compId": "", "compName": "", "compTag": "", "industry": "", "salary": "", "jobKind": "",
#       "compScale": "", "compKind": "", "compStage": "", "eduLevel": edulevel}


def test_cpc_search_word_list():
    s = "040"
    ta = '{"city": "410", "dq": "410", "pubTime": "", "currentPage": 0, "pageSize": 40, "key": "测试", "suggestTag": "","workYearCode": "0", "compId": "", "compName": "", "compTag": "", "industry": "", "salary": "", "jobKind": "","compScale": "", "compKind": "", "compStage": "", "eduLevel": '+s+'}'

    re = ta.encode().decode('unicode_escape')
    print(re)
    url = "https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job"
    data = {"mainSearchPcConditionForm":re,
            "passThroughForm":"{\"scene\": \"input\", \"skId\": \"\", \"fkId\": \"\", \"ckId\": \"wf66llskcd3lfhhxqob6e9dtj7oyhb10\"}"}

    header = {

        'X-Client-Type': 'web',
        'X-Fscp-Std-Info': '{"client_id": "40108"}',
        'X-Fscp-Trace-Id': '0519960d-bf32-4c76-b6a0-f88b54ab3c33',
        'X-Fscp-Version': '1.1',
        'X-Requested-With': 'XMLHttpRequest'

    }

    re = requests.post(url=url, headers=header, data=data,verify=True)
    print(re.json())


    from aig_get_value_tool import aig_get_target_value
    res = aig_get_target_value(re.json(),'requireEduLevel')
    for i in res:
        assert "本科" in i
    return res



def mbws(a,b,n):
    res= a+b
    n-= 1
    if n== 0:
        return res
    else:

        return mbws(b,a+b,n)

print(mbws(3,4,3))




