def path_length(node1, node2, visited, path=1):
    # print(node1, node2, visited, path)

    if node1 == node2:
        return path

    path += 1
    if node2 in nodes_dict[node1]:
        return path

    for node3 in nodes_dict[node1]:
        if node3 not in visited:
            visited.append(node3)
            final_path = path_length(node3, node2, visited, path)
            if final_path is not None:
                return final_path
            visited.pop()


def find_longest_path():
    global leaves, nodes_dict

    path = 1
    for i in range(len(leaves)):
        for j in range(i+1, len(leaves)):
            result = path_length(leaves[i], leaves[j], [leaves[i]])
            if path < result:
                path = result

    print(path)


if __name__ == "__main__":
    n = int(input())
    made_nodes = []
    leaves = []
    nodes_dict = dict()

    for i in range(n-1):
        node1, node2 = [int(j) for j in input().split()]

        if node1 not in made_nodes:
            made_nodes.append(node1)
            leaves.append(node1)
            nodes_dict[node1] = [node2]
        else:
            if node1 in leaves:
                leaves.pop(leaves.index(node1))
            nodes_dict[node1].append(node2)

        if node2 not in made_nodes:
            made_nodes.append(node2)
            leaves.append(node2)
            nodes_dict[node2] = [node1]
        else:
            if node2 in leaves:
                leaves.pop(leaves.index(node2))
            nodes_dict[node2].append(node1)

    find_longest_path()
    # print(made_nodes, leaves, nodes_dict, sep='\n')

