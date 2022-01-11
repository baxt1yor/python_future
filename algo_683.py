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

symbols = ["-", "+", "*", "/"]

res = []
a , b = "", ""
inputStr = input()
isSymbolBefor = True
minus = ""
lastSymbolMinus = False

try:
    res = int(eval(inputStr))
    lastSymbolMinus = True if res < 0 else False
except ZeroDivisionError:
    res = False

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


operation = ""
firstOperation = True

for i in inputStr:
    if (i.isnumeric() or i == '-') and isSymbolBefor:
        a += i
    else:
        isSymbolBefor = False
        if isSymbolBefor != True and i.isnumeric():
            b += i
        else:
            if i in symbols:
                indexed = inputStr.index(i)
                if firstOperation and inputStr[indexed+2] == '-' and inputStr[indexed+3].isnumeric():
                    minus = "-"
                    operation = i
                    firstOperation = False
                elif inputStr[indexed-2] not in symbols and inputStr[indexed+2].isnumeric():
                    operation = i

rerOperation = ""

a = int(a)
b = int(b)

if str(res).isnumeric() or str(res)[1].isnumeric():
    if res < 0:
        rerOperation = f"minus {convert(-1*res, True)}"
    else:
        rerOperation = f"{convert(res, res != 0)}"

    if len(minus) and a < 0:
        result = f"minus {convert(abs(a), abs(a) != 0)} {operation} minus {convert(b, b != 0)} = {rerOperation}"
    elif len(minus) and not a < 0:
        result = f"{convert(a, a != 0)} {operation} minus {convert(b, b != 0)} = {rerOperation}"
    elif a < 0 and not len(minus):
        result = f"minus {convert(abs(a), abs(a) != 0)} {operation} minus {convert(b, b != 0)} = {rerOperation}"
    else:
        result = f"{convert(a, a != 0)} {operation} {convert(b, b != 0)} = {rerOperation}"
    
    print(result)
else:
    print("Gangdalf eshikni ocha olmadi")
