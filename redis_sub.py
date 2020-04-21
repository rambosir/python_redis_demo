# -*-coding:utf-8-*-
import redis

"""
redis 订阅消息
author:Ben
"""

rc = redis.Redis(host='127.0.0.1', port=6379, db=0, password='xxx', decode_responses=True)
ps = rc.pubsub()
# 从stock订阅消息
ps.subscribe('stock')
# 监听状态：一发布，就会收到消息
for item in ps.listen():
    if item['type'] == 'message':
        data = item['data']
        print(data)
        # print(item['channel'])
