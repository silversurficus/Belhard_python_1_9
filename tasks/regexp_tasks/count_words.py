"""
Написать функцию count_words, которая будет считать количество слов в тексте,
с учетом, что в начале могут быть пробелы, в конце могут быть пробелы, между слов
может встречаться больше одного пробела подряд.
"""
import re


def count_words(file_path):
    words = re.findall(r'\w+', open(f"{file_path}").read())
    return len(words)
