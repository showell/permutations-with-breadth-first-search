N = 4

class Transposition:
    def __init__(self, i, j):
        assert i < j
        assert j < N
        self.i = i
        self.j = j

    def __str__(self):
        return f"({self.i +1}{self.j + 1})"


def make_transpositions():
    transpositions = []
    for i in range(N):
        for j in range(i+1, N):
            t = Transposition(i, j)
            transpositions.append(t)

    for t in transpositions:
        print(t)
    return transpositions

print("<pre>")
print("all transpositions:")
transpositions = make_transpositions()
print()

class Permutation:
    def __init__(self, lst, transpositions):
        assert set(lst) == set(range(1, N+1))
        self.lst = lst
        self.transpositions = transpositions
        
    def neighbor(self, t):
        lst = self.lst[:]
        i = lst.index(t.j + 1)
        j = lst.index(t.i + 1)
        (lst[i], lst[j]) = (lst[j], lst[i])
        return Permutation(lst, self.transpositions + [t])

    def neighbors(self):
        return [self.neighbor(t) for t in transpositions]

    def __eq__(self, other):
        return self.lst == other.lst

    def __str__(self):
        transpositions = "".join(str(t) for t in self.transpositions)
        return str(self.lst) + " " + transpositions

    def __hash__(self):
        return hash(tuple(self.lst))

def breadth_first_search(orig, *, neighbors):
    q = [orig]
    depth_dict = dict()
    depth_dict[orig] = 0
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

orig = Permutation(list(range(1, N+1)), [])
distance = breadth_first_search(orig, neighbors=lambda perm: perm.neighbors())

print("all permutations:")
for p, d in distance.items():
    print(f"d={d}", p)
print()

print("distance counts")
for i in range(N):
    print(i, len([d for d in distance.values() if d == i]))

print("</pre>")
