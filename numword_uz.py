number_dict = {
    0:"no'l",
    1: "bir",
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
    1000000000:"milliard",
    1000000:"million",
    1000:"ming",
    100:"yuz",
}

def get_len(num):
        return len(str(num))

def convert(num, rec = False):
        if not rec:
            return number_dict[0]
        if num:
            if get_len(num) == 1:
                    return number_dict[num % 10]

            elif get_len(num) == 2:
                return number_dict[num // 10 * 10] + " " + convert(num % 10, True)

            else:
                for d in denominations:
                    if num not in [100, 1000]:
                        res = num // d
                        if res:
                            return f"{convert(res, True)} {denominations[d]} {convert(num%d, True)}"
                    else:
                        return f"{denominations[num]}"
        return ""

num = int(input())
print(convert(num, num != 0))
