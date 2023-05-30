
if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    made_nodes = []
    cost = 0
    lines = []
    graphs = list(list())

    for i in range(m):
        line = [int(j) for j in input().split()]
        lines.append(line)
    lines = sorted(lines, key=lambda x: x[2])

    for i in range(m):
        if len(graphs) > 0 and len(graphs[0]) == n:
            break
        door = lines[i]
        if door[0] not in made_nodes and door[1] not in made_nodes:
            made_nodes.append(door[0])
            made_nodes.append(door[1])
            graphs.append([door[0], door[1]])
            cost += door[2]

        elif door[0] not in made_nodes:
            made_nodes.append(door[0])
            for j in range(len(graphs)):
                if door[1] in graphs[j]:
                    graphs[j].append(door[0])
                    cost += door[2]
                    break

        elif door[1] not in made_nodes:
            made_nodes.append(door[1])
            for j in range(len(graphs)):
                if door[0] in graphs[j]:
                    graphs[j].append(door[1])
                    cost += door[2]
                    break

        else:
            indx1 = indx2 = -1
            for j in range(len(graphs)):
                if door[0] in graphs[j]:
                    indx1 = j
                if door[1] in graphs[j]:
                    indx2 = j
                if indx1 != -1 and indx2 != -1:
                    break

            if indx1 != indx2:
                graph1 = graphs.pop(max(indx1, indx2))
                graphs[min(indx1, indx2)] += graph1
                cost += door[2]

    print(cost)

""" 
test cases:
6 8
1 2 3
1 3 1
2 3 2
4 1 5
2 4 6
5 2 7
3 5 9
2 6 8

9 9
1 5 12
1 2 32
1 7 20
7 6 15
5 6 64
3 5 10
4 3 7
4 9 39
8 2 1

9 17
1 8 1
5 1 2
6 1 3
5 6 4
7 6 5
5 2 6
3 5 7
7 9 8
6 9 9
4 6 10
8 4 11
9 4 12
3 4 13
9 3 14
2 9 15
2 3 16
8 3 17
"""
