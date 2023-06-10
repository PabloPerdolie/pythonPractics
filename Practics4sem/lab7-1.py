# def main(number):
#     number = int(number)
#     number_bin = bin(number)
#     res = 0
#     for i in range(len(number_bin) - 2):
#         bit = (number >> i) & 1
#         if 0 <= i <= 4:
#             res |= bit << i
#         elif 5 <= i <= 9:
#             res |= bit << i + 22
#         elif 10 <= i <= 16:
#             res |= bit << i - 3
#         elif 17 <= i <= 26:
#             res |= bit << i - 3
#         elif 27 <= i <= 28:
#             res |= bit << i - 22
#         elif 29 <= i <= 31:
#             res |= bit << i - 5
#     return hex(res)
#
# print(main('2446845985'))
# print(main('304076462'))
# print(main('2198215426'))
# print(main('122690621'))
#
# def main_2(number):
#     number_bin = bin(number)
#     value_1 = value_2 = value_3 = 0
#     for i in range(len(number_bin) - 2):
#         bit = (number >> i) & 1
#         if 0 <= i <= 4:
#             continue
#         elif 5 <= i <= 14:
#             value_1 |= bit << i - 5
#         elif 15 <= i <= 19:
#             value_2 |= bit << i - 15
#         elif 20 <= i <= 27:
#             value_3 |= bit << i - 20
#     res = (value_1, value_2, value_3)
#     return res
#
# print(main_2(60186174))
# print(main_2(205774984))
# print(main_2(84542261))
# print(main_2(114224587))
#
# def main_3(array):
#     res = 0
#     value0 = array[0]
#     value1 = array[1]
#     value2 = array[2]
#     value3 = array[3]
#     value4 = array[4]
#     for i in range(27):
#         if 0 <= i <= 3:
#             bit = (int(value0, 16) >> i) & 1
#             res |= bit << i
#         elif 4 <= i <= 5:
#             bit = (int(value1, 16) >> i - 4) & 1
#             res |= bit << i
#         elif i == 6:
#             bit = (int(value2, 16) >> i - 6) & 1
#             res |= bit << i
#         elif 7 <= i <= 16:
#             bit = (int(value3, 16) >> i - 7) & 1
#             res |= bit << i
#         elif 17 <= i <= 26:
#             bit = (int(value4, 16) >> i - 17) & 1
#             res |= bit << i
#     return str(res)
#
#
# print(main_3(('0x1', '0x1', '0x1', '0x38b', '0x367')))
# def main(array):
#     value0 = int(array[0], 16)
#     value1 = int(array[1], 16)
#     value2 = int(array[2], 16)
#     value3 = int(array[3], 16)
#     res = 0
#     for i in range(29):
#         if 0 <= i <= 6:
#            bit = (value0 >> i) & 1
#            res |= bit << i
#         if 7 <= i <= 11:
#            bit = (value1 >> i - 7) & 1
#            res |= bit << i
#         if 12 <= i <= 18:
#            continue
#         if 19 <= i <= 26:
#            bit = (value2 >> i - 19) & 1
#            res |= bit << i
#         if 27 <= i <= 28:
#            bit = (value3 >> i - 27) & 1
#            res |= bit << i
#
#     return hex(res)
#
#
# print(main(['0x23', '0xa', '0xd0', '0x2']))
#
# def main(number1):
#     value1 = value2 = value3 = value4 = 0
#     number = int(number1)
#     for i in range(23):
#         # bit = (number >> i) & 1
#         if 0 <= i <= 4:
#             bit = (number >> i) & 1
#             value1 |= bit << i
#         if 5 <= i <= 7:
#             bit = (number >> i) & 1
#             value2 |= bit << i - 5
#         if 8 <= i <= 13:
#             bit = (number >> i) & 1
#             value3 |= bit << i - 8
#         if 14 <= i <= 22:
#             bit = (number >> i) & 1
#             value4 |= bit << i - 14
#     return [('J1', hex(value1)), ('J2', hex(value2)), ('J3', hex(value3)), ('J4', hex(value4))]
#
#
# print(main('6892556'))

def main_2(array):
    value1 = int(array[0], 16)
    value2 = int(array[1], 16)
    value3 = int(array[2], 16)
    value4 = int(array[3], 16)
    res = 0
    for i in range(29):
        if 0 <= i <= 6:
            bit = (value1 >> i) & 1
            res |= bit << i
        if 7 <= i <= 11:
            bit = (value2 >> i - 7) & 1
            res |= bit << i
        if 12 <= i <= 18:
            continue
        if 19 <= i <= 26:
            bit = (value3 >> i - 19) & 1
            res |= bit << i
        if 27 <= i <= 28:
            bit = (value4 >> i - 27) & 1
            res |= bit << i
    return hex(res)


print(main_2([('0x7'), ('0xc'), ('0xd9'), ('0x1')]))

def main(array):
    value1 = int(array[0])
    value1 = int(array[1])