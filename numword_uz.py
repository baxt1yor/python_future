import random
number_dict = {
    1:"bir",
    2:"ikki",
    3:"uch",
    4:"to'rt",
    5:"besh",
    6:"olti",
    7:"yetti",
    8:"sakkiz",
    9:"to'qqiz",
    10:"o'n",
    20:"yigirma",
    30:"o'ttiz",
    40:"qirq",
    50:"ellik",
    60:"oltmish",
    70:"yetmish",
    80:"sakson",
    90:"to'qson"
}

denominations = {
    1000000000000:"trilion",
    1000000000:"milliard",
    1000000:"million",
    1000:"ming",
    100:"yuz"
}

def get_len(num):
        return len(str(num))

def convert(num):
        if num:
            if get_len(num) == 1:
                    return f"{number_dict[num % 10]}"
            elif get_len(num) == 2:
                return f"{number_dict[num // 10 * 10]} {str(convert(num % 10)).strip()}"
            else:
                for d in denominations:
                    res = num // d
                    if res:
                        return f"{str(convert(res)).strip()} {denominations[d]} {str(convert(num%d)).strip()}"
        return ""

num = int(input())

print(convert(num))
