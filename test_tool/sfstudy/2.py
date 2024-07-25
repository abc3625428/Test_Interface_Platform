




def is_symmetric(s):
    # 判断字符串是否为空或长度为 0
    if s is None or len(s) == 0:
        return False

    # 遍历字符串的一半，比较每一个字符和它对应的镜像字符是否相等
    for i in range(len(s) // 2):
        if s[i]!= s[len(s) - i - 1]:
            return False

    return True


print(is_symmetric('kaammaak'))


def is_symmtrics(str):
    if str is None or len(str)==0:
        return False
    for i in range(len(str)//2):
        print(len(str)-i-1)
        print(str[len(str)-i-1])
        if str[i] != str[len(str)-i-1]:
            return False
    return True




def activity_selection(problem):
    activities = problem['activities']
    n = len(activities)

    # 初始化结果
    result = {'start_time': [0] * n, 'end_time': [0] * n}

    # 按照结束时间进行排序
    activities.sort(key=lambda x: x['end_time'])

    i = 0
    current_time = 0

    while i < n:
        activity = activities[i]

        # 如果当前活动的开始时间大于等于当前时间，则可以选择该活动
        if current_time >= activity['start_time']:
            result['start_time'][i] = current_time
            result['end_time'][i] = activity['end_time']
            current_time = activity['end_time']
            i += 1

    return result

# 测试代码
if __name__ == "__main__":
    problem = {
        'activities': [
            {'start_time': 1, 'end_time': 4},
            {'start_time': 3, 'end_time': 5},
            {'start_time': 0, 'end_time': 3},
            {'start_time': 5, 'end_time': 7},
            {'start_time': 6, 'end_time': 8}
        ]
    }

    result = activity_selection(problem)
    print("活动安排结果：")
    for i in range(len(result['start_time'])):
        print(f"活动{i+1}：开始时间 {result['start_time'][i]}, 结束时间 {result['end_time'][i]}")


        int()