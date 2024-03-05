#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project ：alist-detector 
@File    ：config.py
@desc    ：
@Author  ：@Natro92
@Date    ：2024/3/5 15:11 
@Blog    : natro92.github.io
@Contact : 2997453446@qq.com
"""
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
# * 设置请求timeout时间
timeout = 10
# * 是否使用ssl
ssl = False
# * debug 模式
debug = False
# * 控制线程数量
concurrent_tasks = 400
