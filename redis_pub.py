# -*-coding:utf-8-*-
import redis

"""
redis 发布消息
author:Ben
"""

data = {'name': 'icbc', 'price': 2}

rc = redis.Redis(host='127.0.0.1', port=6379, db=0, password='xxx')
# 发布消息到stock频道
rc.publish('stock', str(data))
