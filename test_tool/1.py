data = {'': 1.0, 'dataset': 'houyi_jobname', 'ersion': 'f2b634', 'etric': 'accuracy', 'ode': 'gen', 'vllm': 0.75}



# result = {}
# for item in data:
#     dataset = item['dataset']
#     if dataset not in result:
#         result[dataset] = []
#     result[dataset].append(item)


import json

s = str(json.dumps(data))
print(s)