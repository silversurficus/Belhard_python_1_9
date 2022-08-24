"""
Написать функцию add_to_path, которая будет добавлять директорию, в которой находится
переданный файл (путь к файлу) в sys.path
"""
import os
import sys

base_dir = os.path.dirname(__file__) or '.'


def add_to_path(file_path):
    dir_md = os.path.join(base_dir, file_path)
    sys.path.append(dir_md)

