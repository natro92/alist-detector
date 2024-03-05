#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project ：alist-detector 
@File    ：exporter.py
@desc    ：
@Author  ：@Natro92
@Date    ：2024/3/5 14:27 
@Blog    : natro92.github.io
@Contact : 2997453446@qq.com
"""
import time
import os

from utils.cli_beautify import get_colored_text


def export_as_file(text):
    # * 导出为文件，名称为时间戳
    # 检测是否存在outputs 不存在初始化一个
    dir_path = "outputs"
    # 检查文件是否存在
    if not os.path.isdir(dir_path):
        # 文件夹不存在，创建新的文件夹
        os.makedirs(dir_path)
    filename = "outputs/" + str(int(time.time())) + ".txt"
    with open(filename, "w") as f:
        for line in text:
            f.write(line + "\n")
    print(get_colored_text(32, f"[*] 保存成功，保存在：{filename}"))

