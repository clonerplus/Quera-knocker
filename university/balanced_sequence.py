input_parentheses = input()

unfinished = 0
change_count = 0
result = ""

for i in range(len(input_parentheses)):
    if input_parentheses[i] == '(':
        if len(input_parentheses) - i > unfinished:
            result += '('
            unfinished += 1
        else:
            result += ')'
            unfinished -= 1
            change_count += 1
    else:
        if unfinished == 0:
            result += '('
            unfinished += 1
            change_count += 1
        else:
            result += ')'
            unfinished -= 1

# print(result)
print(change_count)
