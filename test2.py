# -*- coding: utf-8 -*-

# --** coding="UTF-8" **--
import os
import re
import sys

foldname = r"./binren"
    # 举例：r"./neteasy_playlist_data3"
fileList = os.listdir(foldname)
    # 输出此文件夹中包含的文件名称
print( fileList[0])
    # 得到进程当前工作目录
currentpath = os.getcwd()
    # 将当前工作目录修改为待修改文件夹的位置

os.chdir(foldname)
    # 名称变量
num = 1
    # 遍历文件夹中所有文件
for fileName in fileList:
        # 匹配文件名正则表达式
    pat = "[\u4e00-\u9fa5]+"
        # 进行匹配
    pattern = re.findall(pat, fileName)
        # 文件重新命名
    os.rename(fileName, str(num))
        # 改变编号，继续下一项（拓展名也可修改为其他的）
    num = num + 1
print("***************************************")
    # 改回程序运行前的工作目录
os.chdir(currentpath)
    # 刷新
sys.stdin.flush()
    # 输出修改后文件夹中包含的文件名称
print("修改后：" + os.listdir(foldname)[0])
