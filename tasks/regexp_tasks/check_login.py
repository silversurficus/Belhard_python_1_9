"""
Написать функцию check_login, которая будет принимать строку и проверять,
что она является логином, который соответствует следующим правилам:
1. Длина от 5 до 20 символов
2. Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания
"""
import re

def check_login(string):
    pattern = re.compile(r"^(?=.{5,20}$)([\w]+)$")
    if not pattern.match(string):
        print("faaa")
        raise ValueError
    return string

check_login("aaaa__")
check_login("aaaaAAAVV")
check_login("AAAAAAAAAAA")
check_login("aaaa;;;")
check_login("aaaa___Avv")