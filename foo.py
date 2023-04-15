print("<pre>")


def breadth_first_search(top, *, neighbors):
    q = [top]
    depth_dict = dict()
    depth_dict[top] = 0
    depth = 0
    while q:
        depth += 1
        new_q = []
        for obj in q:
            for neighbor in neighbors(obj):
                if neighbor not in depth_dict:
                    depth_dict[neighbor] = depth
                    new_q.append(neighbor)
        q = new_q
    return depth_dict


LIST_SIZE = 4


class Transposition:
    def __init__(self, i, j):
        assert i >= 1
        assert i < j
        assert j <= LIST_SIZE
        self.i = i
        self.j = j

    def __str__(self):
        return f"({self.i}{self.j})"


def make_transpositions():
    transpositions = []
    for i in range(LIST_SIZE):
        for j in range(i + 1, LIST_SIZE):
            t = Transposition(i + 1, j + 1)
            transpositions.append(t)
    return transpositions


transpositions = make_transpositions()
print("all transpositions:")
for t in transpositions:
    print(t)

print()


class Permutation:
    def __init__(self, lst, *, parent, transposition):
        if parent is None:
            assert transposition is None
        assert set(lst) == set(range(1, LIST_SIZE + 1))
        self.lst = lst
        self.parent = parent
        self.transposition = transposition

    def neighbor(self, t):
        lst = self.lst[:]
        i = lst.index(t.j)
        j = lst.index(t.i)
        (lst[i], lst[j]) = (lst[j], lst[i])
        return Permutation(lst, parent=self, transposition=t)

    def neighbors(self):
        return [self.neighbor(t) for t in transpositions]

    def __eq__(self, other):
        return self.lst == other.lst

    def __str__(self):
        s = str(self.lst)
        if self.parent is None:
            return s
        return f"{s} == {self.transposition} on {self.parent}"

    def __hash__(self):
        return hash(tuple(self.lst))


orig = Permutation(list(range(1, LIST_SIZE + 1)), parent=None, transposition=None)
distance = breadth_first_search(orig, neighbors=lambda perm: perm.neighbors())

print("all permutations:")
for p, d in distance.items():
    print(f"d={d}", p)
print()

print("distance counts")
for i in range(LIST_SIZE):
    print(i, len([d for d in distance.values() if d == i]))

print("</pre>")
