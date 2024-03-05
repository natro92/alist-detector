#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project : alist-detector 
@File    : alist-detector.py
@desc    : 
@Author  : @Natro92
@Date    : 2024/3/4 11:55 
@Blog    : natro92.github.io
@Contact : 2997453446@qq.com
"""

import asyncio
from alist.check import tasks_main
from alist.reader import WebsiteIpListCleaner
from utils.cli_beautify import start_program, get_colored_text
from utils.exporter import export_as_file


def reader_():
    cleaner = WebsiteIpListCleaner("./ip.txt")
    cleaned_lines = cleaner.clean()
    # print(cleaned_lines)
    print(get_colored_text(32, f"[*] 加载文件成功"))
    return cleaned_lines


def check_(_urls):
    urls = _urls if _urls else []
    policy = asyncio.WindowsSelectorEventLoopPolicy()
    asyncio.set_event_loop_policy(policy)
    loop = asyncio.new_event_loop()
    allowed_urls = loop.run_until_complete(tasks_main(urls))
    print(allowed_urls)
    return allowed_urls


if __name__ == '__main__':
    start_program()
    list_test = reader_()
    export_as_file(check_(list_test))

