class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(2 * node, start, mid, left, right)
        right_sum = self.query(2 * node + 1, mid + 1, end, left, right)
        return left_sum + right_sum

    def update(self, node, start, end, index, value):
        if start == end:
            self.arr[index] = value
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= index <= mid:
                self.update(2 * node, start, mid, index, value)
            else:
                self.update(2 * node + 1, mid + 1, end, index, value)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]