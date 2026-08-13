class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = [None] * (4 * n)
        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a
            lc, rc, pre, suf, best, length = a
            lc2, rc2, pre2, suf2, best2, length2 = b
            new_pre = pre
            new_suf = suf2
            new_best = max(best, best2)
            if rc == lc2:
                new_best = max(new_best, suf + pre2)
                if pre == length:
                    new_pre = length + pre2
                if suf2 == length2:
                    new_suf = suf + length2
            return (lc, rc2, new_pre, new_suf,
                    new_best, length + length2)
        def build(node, left, right):
            if left == right:
                tree[node] = (s[left], s[left], 1, 1, 1, 1)
                return
            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        def update(node, left, right, pos, ch):
            if left == right:
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return
            mid = (left + right) // 2
            if pos <= mid:
                update(node * 2, left, mid, pos, ch)
            else:
                update(node * 2 + 1, mid + 1, right, pos, ch)
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        build(1, 0, n - 1)
        answer = []
        for ch, pos in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, pos, ch)
            answer.append(tree[1][4])
        return answer