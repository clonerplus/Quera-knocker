class BTN:
    def __init__(self, label):
        # self.parent = None
        self.left_child = None
        self.right_child = None
        self.label = label
        self.way_cost = None

    def __str__(self):
        return "\"%s\"" % str(self.label)


class Tree:
    def __init__(self):
        self.root = None
        self.last_level = None

    def assign_next_level(self, labels):
        if not self.root:
            self.root = BTN(int(labels[0]))
            self.last_level = [self.root]
            self.root.way_cost = self.root.label

            return

        new_last_level = []

        for i in range(len(self.last_level)):

            left_node = BTN(int(labels[i]))
            right_node = BTN(int(labels[i+1]))
            self.last_level[i].left_child = left_node
            self.last_level[i].right_child = right_node
            if i == 0:
                left_node.way_cost = self.last_level[0].way_cost + left_node.label

                if len(self.last_level) > 1:
                    right_node.way_cost = max(self.last_level[0].way_cost, self.last_level[1].way_cost) + right_node.label
                else:
                    right_node.way_cost = self.last_level[0].way_cost + right_node.label

            elif i == len(self.last_level) - 1:
                right_node.way_cost = self.last_level[len(self.last_level) - 1].way_cost + right_node.label

                if i > 0:
                    left_node.way_cost = max(self.last_level[i].way_cost, self.last_level[i-1].way_cost) + left_node.label
                else:
                    left_node.way_cost = self.last_level[i].way_cost + left_node.label

            else:
                # print(self.last_level, i)
                left_node.way_cost = max(self.last_level[i].way_cost, self.last_level[i - 1].way_cost) + left_node.label
                right_node.way_cost = max(self.last_level[i].way_cost, self.last_level[i + 1].way_cost) + right_node.label

            new_last_level.append(left_node)

        new_last_level.append(right_node)
        # for j in new_last_level: print(j, j.way_cost, end=' ')
        # print()

        self.last_level = new_last_level[:]

    def print_pricey_way(self):
        return max([j.way_cost for j in self.last_level])

    def print_tree(self):
        nodes = [self.root]
        childs = []
        # print(self.root.left_child)
        while nodes:
            for i in range(len(nodes)):
                if i//2 == 0:
                    print(nodes[i], end=' ')
                if nodes[i]:
                    childs.append(nodes[i].left_child)
                    childs.append(nodes[i].right_child)
            print(nodes[-1], end=' ')
            print()
            nodes = childs[:]
            childs.clear()


if __name__ == "__main__":
    t = int(input())
    triangle = []
    results = []

    for i in range(t):
        n = int(input())
        triangle = [[] for j in range(n)]
        index = 0
        tree = Tree()
        for j in range(n):
            row = input().split(' ')
            row = [int(k) for k in row]
            triangle[j] = row
            tree.assign_next_level(row)

        results.append(tree.print_pricey_way())

    for result in results: print(result)

