n = int(input())
names = []
properties = dict()

for i in range(n):
    names.append(input())

for i in range(n):
    name = input()
    properties[name] = dict()
    initial_val, fr_count = [int(i) for i in input().split()]
    properties[name]["initial_val"] = initial_val
    properties[name]["fr_count"] = fr_count
    properties[name]["income"] = 0
    properties[name]["frs"] = []
    for j in range(fr_count):
        properties[name]["frs"].append(input())

for name in properties:
    dic = properties[name]
    dic["rem"] = dic["initial_val"]
    dic["diff"] = 0
    # if person has any friends
    if dic["fr_count"] != 0:
        dic["rem"] = dic["initial_val"] % dic["fr_count"]
        gift = dic["initial_val"] // dic["fr_count"]
        for fr in properties[name]["frs"]:
            properties[fr]["income"] += gift
        # dic["diff"] = dic["initial_val"] - dic["fr_count"] * gift + dic["rem"]

for name in names:
    dic = properties[name]
    dic["diff"] = dic["income"] - dic["initial_val"] + dic["rem"]
    print(name, dic["diff"])

# print(properties)
