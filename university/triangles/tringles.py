global triangle, results
t = int(input())
# t = 1
triangle = []
results = []


def find_biggest_precise_way(ways):
    indx = len(ways[0]) - 2
    while len(ways) > 1 and indx > 0:
        if sum(ways[-1][:indx]) < sum(ways[-2][:indx]):
            ways = ways[:-2] + [ways[-2][:indx] + ways[-1][indx:]]
        indx -= 1
    results.append(sum(ways[-1]))


def find_biggest_approximate_way(height):
    ways_elements = []
    previous_rows = 0
    way_elements1 = []
    indx = 0
    biggest_sum = 0
    for i in range(height-1):
        way_elements1.append(triangle[i][-1])
        previous_rows += triangle[i][-1]
        row_sum = previous_rows
        way_elements2 = way_elements1[:]
        for j in range(i+1, height):
            row_sum += triangle[j][i]
            way_elements2.append(triangle[j][i])
            # print(triangle[j][i])
        ways_elements.append(way_elements2)
        if biggest_sum < row_sum:
            biggest_sum = row_sum
            indx = i
        # print(row_sum)

    way_elements3 = way_elements2[:]
    way_elements3.pop()
    way_elements3.append(triangle[-1][-1])
    ways_elements.append(way_elements3)
    if biggest_sum < previous_rows + triangle[-1][-1]:
        biggest_sum = row_sum
        indx = len(triangle) - 1
    # print(previous_rows)
    # print(ways_elements, indx)
    find_biggest_precise_way(ways_elements[:indx+1])

# def upper_rows(j, k, max_way_sum):
#     if j == -1:
#         return 0
#
#     elif j == 0:
#         max_way_sum += triangle[0][0]
#         # print(max_way_sum)
#
#         return max_way_sum
#
#     if k == 0:
#         max_way_sum += triangle[j][0]
#         return upper_rows(j - 1, 0, max_way_sum)
#
#     elif k == len(triangle[j]) - 1:
#         max_way_sum += triangle[j][len(triangle[j]) - 1]
#         return upper_rows(j - 1, len(triangle[j]) - 2, max_way_sum)
#
#     else:
#         max_way_sum += max(triangle[j][k - 1:k + 1])
#         return upper_rows(j - 1, triangle[j].index(max(triangle[j][k - 1:k + 1])), max_way_sum)
#
#
# def lower_rows(j, k, max_way_sum):
#     if j == len(triangle):
#         return 0
#
#     elif j == len(triangle) - 1:
#         max_way_sum += max(triangle[j][k:k+2])
#         # print(max_way_sum)
#
#         return max_way_sum
#
#     max_way_sum += max(triangle[j][k:k + 2])
#
#     return lower_rows(j + 1, triangle[j].index(max(triangle[j][k:k + 2])), max_way_sum)
#
#
# def max_elements_sum(j, k, max_element):
#     a = upper_rows(j - 1, k, 0)
#     # print(max_element)
#     b = lower_rows(j + 1, k, 0)
#     return a + b + max_element


# def all_sums(j, k, way_sum):
#     global triangle, biggest_sum
#
#     if j == len(triangle) - 1:
#         way_sum += triangle[j][k]
#
#         if biggest_sum < way_sum:
#             biggest_sum = way_sum
#         return
#
#     way_sum += triangle[j][k]
#     for l in range(k, k+2):
#         all_sums(j + 1, l, way_sum)


for i in range(t):
    n = int(input())
    triangle = [[] for j in range(n)]
    index = 0
    for j in range(n):
        row = input().split(' ')
        row = [int(k) for k in row]
        triangle[j] = row

# all_sums(0, 0, biggest_sum)
# for i in range(len(triangle)):
#     tmp = max_elements_sum(i, triangle[i].index(max(triangle[i])), max(triangle[i]))
#     if biggest_sum < tmp:
#         biggest_sum = tmp
# print(triangle)
    find_biggest_approximate_way(len(triangle))

for i in results: print(i)
# print(biggest_sum)
