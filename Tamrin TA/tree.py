import sys, threading
sys.setrecursionlimit(10**7) 
threading.stack_size(2**25)  

class Tree_Height:
    def read(self):
            self.n = int(input())
            self.parent = list(map(int, input().split()))

    def getChildren(self, node, nodes):
        parent = {'key': node, 'child': []}
        children = [i for i, x in enumerate(nodes) if x == parent['key']]
        for child in children:
            parent['child'].append(self.getChildren(child, nodes))
        return parent

    def compute_height(self, tree):
        if len(tree['child']) == 0:
            return 0
        else:
            values = []
            for child in tree['child']:
                values.append(self.compute_height(child))
            return 1 + max(values)
def main():
    tree = Tree_Height()
    tree.read()
    treeChild = tree.getChildren(-1, tree.parent)
    print(tree.compute_height(treeChild))

threading.Thread(target=main).start()