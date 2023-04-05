N = 5

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
    def __init__(self, lst):
        assert set(lst) == {1, 2, 3, 4, 5}
        self.lst = lst
        
    def neighbor(self, t):
        lst = self.lst[:]
        i = lst.index(t.j + 1)
        j = lst.index(t.i + 1)
        (lst[i], lst[j]) = (lst[j], lst[i])
        return Permutation(lst)

    def neighbors(self):
        return [self.neighbor(t) for t in transpositions]

    def __eq__(self, other):
        return self.lst == other.lst

    def __str__(self):
        return str(self.lst)

    def __hash__(self):
        return hash(tuple(self.lst))

def breadth_first_search(orig):
    q = [orig]
    distance = dict()
    distance[orig] = 0
    dist = 0
    while q:
        dist += 1
        new_q = []
        for obj in q:
            for neighbor in obj.neighbors():
                if neighbor not in distance:
                    distance[neighbor] = dist
                    new_q.append(neighbor)
        q = new_q
    return distance

orig = Permutation([1, 2, 3, 4, 5])
distance = breadth_first_search(orig)

print("all permutations:")
for p, d in distance.items():
    print(d, p)
print()

print("distance counts")
for i in range(N):
    print(i, len([d for d in distance.values() if d == i]))

print("</pre>")
