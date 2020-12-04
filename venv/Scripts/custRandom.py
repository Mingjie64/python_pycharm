# _*_ coding: utf-8 _*_
import string, random


def mix_letters(n):
    letters = ''.join(random.sample(string.ascii_letters + string.digits, n))
    return letters


print(mix_letters(11))

# 获取随机数
