s, r = input(), 0
for g in range(len(s)):
    if s[g] == s[(len(s)-(g+1))]:
        r += 1
if r == len(s):
    print ("YES")
else:
    print ("NO")

