
import time
import random



def generate_token():
    """
    生成随机token
    :return: 随机token
    """
    # 使用当前时间戳作为token的一部分
    timestamp = int(time.time())
    # 使用随机数作为token的一部分
    rand = random.randint(0, 1000)
    # 将时间戳和随机数拼接成一个字符串
    token = f"{timestamp}{rand}"
    return token