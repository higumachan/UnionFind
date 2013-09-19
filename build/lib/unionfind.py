"""
struct UnionFind {
        vector<int> data;
        UnionFind(int size) : data(size, -1) { }
        bool unionSet(int x, int y) {
            x = root(x); y = root(y);
            if (x != y) {
                if (data[y] < data[x]) swap(x, y);
                data[x] += data[y]; data[y] = x;
                }
            return x != y;
            }
        bool findSet(int x, int y) {
            return root(x) == root(y);
            }
        int root(int x) {
            return data[x] < 0 ? x : data[x] = root(data[x]);
            }
        int size(int x) {
            return -data[root(x)];
            }
        };
"""

class UnionFind(object):
    def __init__(self, size):
        self.data = [-1 for i in range(size)];
    
    def unite(self, x, y):
        x = self.root(x);
        y = self.root(y);
        if (x != y):
            if (self.data[y] < self.data[x]):
                x, y = y, x;
            self.data[x] += self.data[y];
            self.data[y] = x;
        return x != y;

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def root(self, x):
        if self.data[x] < 0 :
            return x;
        self.data[x] = self.root(self.data[x]);
        return self.data[x];
    
    def size(self, x):
        return -self.data[self.root(x)];


if __name__ == '__main__':
    uf = UnionFind(10);
    uf.unite(0, 1);
    uf.unite(0, 2);
    print uf.same(0, 1);
    print uf.same(1, 2);
    print uf.same(1, 3);

