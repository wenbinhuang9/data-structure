

class unionfind:

    def __init__(self, n):
        self.p = list(range(n))
        ## rank for tree balance
        self.rank = [0] * n
        self.count = [1] * n

    def find(self, x):
        ## path compression: points directly to the parent , it can significantly improve the finding time complexity
        if self.p[x] != x: self.p[x] = self.find(self.p[x])

        return self.p[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        x_parent_rank = self.rank[x_parent]
        y_parent_rank = self.rank[y_parent]

        x_parent_count = self.count[x_parent]
        y_parent_count = self.count[y_parent]
        
        if x_parent_rank < y_parent_rank:
            self.p[x_parent] = y_parent
            self.count[y_parent] += x_parent_count
        elif x_parent_rank > y_parent_rank:
            self.p[y_parent] = x_parent
            self.count[x_parent] += y_parent_count
        else:
            self.p[y_parent] = x_parent
            self.rank[x_parent] += 1
            self.count[x_parent] += y_parent_count


    def connected(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        return  x_parent == y_parent

    ## count member of components
    def count(self, x):
        parent = self.find(x)

        return self.count[parent]


