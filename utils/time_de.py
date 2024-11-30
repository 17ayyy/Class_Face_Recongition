# -*- coding: UTF-8 -*-
"""
*@ description: 装饰器 | 函数执行时间测量
*@ name:	time.py
*@ author: dengbozfan
*@ time:	2024/11/28 21:08
"""

import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录函数开始执行的时间
        result = func(*args, **kwargs)  # 执行函数
        end_time = time.time()  # 记录函数结束执行的时间
        print(f"{func.__name__}执行了-->{end_time - start_time} seconds")
        return result
    return wrapper
