#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project : alist-detector 
@File    : check.py
@desc    : 判断接口情况
@Author  : @Natro92
@Date    : 2024/3/4 16:20 
@Blog    : natro92.github.io
@Contact : 2997453446@qq.com
"""

import asyncio
import aiohttp
from trange import trange
from tqdm.asyncio import tqdm

from utils.cli_beautify import get_colored_text
from config.config import *


async def check_guest_permission(url):
    # * 检测 是否有guest权限访问URL
    me_url = url + "/api/me"
    headers['Host'] = url.split("//")[1][:-1]
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl)) as session:
        try:
            async with session.get(me_url, headers=headers, timeout=timeout) as response:
                # async with session.get(me_url) as response:
                if response.status == 200:
                    data = await response.json()
                    # 用tqdm的write来代替print可以不让输出被打断
                    # tqdm.write(f"URL: {me_url} | code: {data['code']}")
                    if data['code'] == 200:
                        if debug: tqdm.write(f"[*] {url}/api/me | {data['code']} ")
                        return True
                    else:
                        if debug: tqdm.write(
                            get_colored_text(33, f"[*] {url}/api/me | Guest权限需要密码访问，或者没开启Guest访问 "))
                        return False
                else:
                    if debug: tqdm.write(get_colored_text(33, f"[*] {url}/api/me | 未正确获取到信息 "))
                    return False
        except Exception as e:
            if debug: tqdm.write(get_colored_text(33, f"[*] {url}/api/me | 出现问题 {e} "))
            return False


async def check_url_settings(url):
    # * 检测是否有权限挂载
    info_url = url + "/api/public/settings"
    headers['Host'] = url.split("//")[1][:-1]
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl)) as session:
        try:
            async with session.get(info_url, headers=headers, timeout=timeout) as response:
                # async with session.get(info_url) as response:
                if response.status == 200:
                    data = await response.json()
                    # 用tqdm的write来代替print可以不让输出被打断
                    # tqdm.write(f"URL: {info_url} | allow_mounted: {data['data']['allow_mounted']}")
                    if data['data']['allow_mounted'] == "true":
                        if debug: tqdm.write(f"[*] {url}/api/public/settings | {data['data']['allow_mounted']} ")
                        return True
                    else:
                        if debug: tqdm.write(get_colored_text(33, f"[*] {url}/api/public/settings | 不可挂载 "))
                        return False
                else:
                    if debug: tqdm.write(get_colored_text(33, f"[*] {url}/api/public/settings | 未正确获取到信息 "))
                    return False
        except Exception as e:
            if debug: tqdm.write(get_colored_text(33, f"[*] {url}/api/public/settings | 出现问题 {e} "))
            return False


async def check_url(url, semaphore):
    """

    # * 使用Semaphore 对线程上限进行限制 已完成

    :param url: 单个URL
    :param semaphore: semaphore对象
    :return:
    """

    async with semaphore:
        # * 整合 check_url_settings 和 check_url_permissions 两个函数
        # 异步调用两个函数
        guest_permission = await check_guest_permission(url)
        url_settings = await check_url_settings(url)
        # 只有当两个函数都返回 True 时才执行操作
        if guest_permission and url_settings:
            # 用tqdm的write来代替print可以不让输出被打断
            tqdm.write(get_colored_text(32, f"[*] {url} | 允许挂载且可以Guest访问 "))
            # 在这里执行操作
            return url


async def tasks_main(urls, _concurrent_tasks=concurrent_tasks):
    """
    设置任务总管理
    :param urls: URL列表
    :param _concurrent_tasks: 需要线程数量
    :return: 满足要求的URL列表
    """
    semaphore = asyncio.Semaphore(_concurrent_tasks)
    # * 这段改了半天也没改明白，最后让gpt改了几次才实现进度条
    tasks = [check_url(url, semaphore) for url in urls]
    results = []
    with tqdm(total=len(tasks)) as pbar:
        for coro in asyncio.as_completed(tasks):
            result = await coro
            if result:
                results.append(result)
            pbar.update(1)
    return results


"""
Usage:
urls = ["https://example1.com/api/public/settings", "https://example2.com/api/public/settings"]
loop = asyncio.get_event_loop()
allowed_urls = loop.run_until_complete(tasks_main(urls))
print(allowed_urls)
"""
