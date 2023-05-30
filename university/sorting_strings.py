import math


def words_inequality(word1, word2):  # returns true if word2 is bigger than word1
    if word1[0].lower() < word2[0].lower():
        return True
    elif word1[0].lower() > word2[0].lower():
        return False

    else:
        if word1[0] < word2[0]:
            return True
        elif word1[0] > word2[0]:
            return False

        if len(word2) < 2:
            return False
        elif len(word1) < 2:
            return True

        if word1[1].lower() < word2[1].lower():
            return True
        elif word1[1].lower() > word2[1].lower():
            return False

        return False


def put_string_in_list(min, max):
    global string, srtd_nms

    if min == max:
        if words_inequality(string, srtd_nms[min]):

            return min
        return min + 1

    if words_inequality(string, srtd_nms[(min+max)//2]):
        return put_string_in_list(min, (min+max)//2)

    else:
        return put_string_in_list(math.ceil((min+max)/2), max)


if __name__ == "__main__":
    global string

    strs = input().split()[:-1]
    if len(strs) == 0:
        print()
        exit(0)
    srtd_nms = [strs[0]]
    # print(strs)

    for name in strs[1:]:
        string = name
        i = put_string_in_list(0, len(srtd_nms)-1)
        srtd_nms.insert(i, name)

    print(*srtd_nms)
