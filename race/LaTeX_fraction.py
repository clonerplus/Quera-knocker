n = int(input())
string = "1"
new_string = "1"
nums = "1023456789"
seen = []

while n > 1:
    string = new_string
    diff = 0
    for i in range(len(string)):
        if len(string) == 1:
            new_string = "1+\\frac{2}{3}"
            break
        elif i > 0 and string[i-1] not in nums and string[i] in nums:
            j = i
            num = ""
            while j < len(string) and string[j] in nums:
                num += string[j]
                j += 1
            if num not in seen:
                seen.append(num)
                new_string = new_string[:j + diff] + "+\\frac{" + str(int(num)*2) + "}" + "{" + str(
                    int(num)*2 + 1) + "}" + new_string[j + diff:]
                diff += 12
    n -= 1

print(new_string)

