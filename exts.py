# -*- encoding: utf-8 -*-
import os
import shutil


#  删除文件夹
def de_clifile(dir):
    filelist = os.listdir(dir)
    for f in filelist:
        filepath = os.path.join(dir, f)  # 将文件名映射成绝对路劲
        if os.path.isfile(filepath):  # 判断该文件是否为文件或者文件夹
            os.remove(filepath)  # 若为文件，则直接删除
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)  # 若为文件夹，则删除该文件夹及文件夹内所有文件
    shutil.rmtree(dir, True)  # 最后删除总文件夹


#  删除文件
def de_file(dir):
    os.remove(dir)


#  复制文件
def copy(old, new):
    source_path = os.path.abspath(old)
    target_path = os.path.abspath(new)
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)
