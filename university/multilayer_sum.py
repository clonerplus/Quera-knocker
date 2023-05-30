input_set = input()
nums = "0123456789"

indexes = []


def sumation(string):

    sum = 0
    number = ""
    for char in string:
        if char in nums:
            number += char
        elif char == ',':
            sum += int(number)
            number = ""
    sum += int(number)

    return sum


def sub_list(j, k):
    a = input_set[j: k + 1]
    return sumation(a)


for i, ch in enumerate(input_set):
    # print(indexes)
    if ch == '{':
        indexes.append(i)
    elif ch == '}':
        print(sub_list(indexes[-1], i))
        indexes = indexes[:-1]
