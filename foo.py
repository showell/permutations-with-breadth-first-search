class Transposition:
    def __init__(self, i, j):
        assert i < j
        assert j < 7
        self.i = i
        self.j = j

    def __str__(self):
        return f"({self.i +1}{self.j + 1})"


def make_transpositions():
    transpositions = []
    for i in range(7):
        for j in range(i+1, 7):
            t = Transposition(i, j)
            transpositions.append(t)

    for t in transpositions:
        print(t)
    return transpositions

transpositions = make_transpositions()

class Permutation:
    def __init__(self, lst):
        assert set(lst) == {1, 2, 3, 4, 5, 6, 7}
        self.lst = lst
        
    def neighbor(self, t):
        lst = self.lst[:]
        (lst[t.i], lst[t.j]) = (lst[t.j], lst[t.i])
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

orig = Permutation([1, 2, 3, 4, 5, 6, 7])
distance = breadth_first_search(orig)

for p, d in distance.items():
    print(p, d)

for i in range(7):
    print(i, len([d for d in distance.values() if d == i]))
