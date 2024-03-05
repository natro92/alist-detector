#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project : alist-detector 
@File    : reader.py
@desc    : 读取文件内容
@Author  : @Natro92
@Date    : 2024/3/4 11:56 
@Blog    : natro92.github.io
@Contact : 2997453446@qq.com
"""

import re


class WebsiteIpListCleaner:
    """
    
    Read URL list and tidy it to URL.

    Usage:

    cleaner = WebsiteIpListCleaner("./ip.txt")
    cleaned_lines = cleaner.clean()
    print(cleaned_lines)

    """
    def __init__(self, filename):
        self.filename = filename
        self.unique_lines = set()

    def clean(self):
        with open(self.filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line.startswith("https://") or line.startswith("http://"):
                    line = "https://" + line
                # 这里不添加末尾 后面再添加
                # if not line.endswith("/"):
                #     line += "/api/public/settings"
                self.unique_lines.add(line)

        return list(self.unique_lines)
