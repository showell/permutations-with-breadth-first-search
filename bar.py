from collections import defaultdict

print("<pre>")


def brute_search(orig, transpositions):
    perm_dict = defaultdict(list)
    for p in transpositions:
        permutation = orig.neighbor(p)
        perm_dict[permutation].append((str(p),))
        for q in transpositions:
            permutation = orig.neighbor(p).neighbor(q)
            perm_dict[permutation].append((str(p), str(q)))
            for r in transpositions:
                permutation = orig.neighbor(p).neighbor(q).neighbor(r)
                perm_dict[permutation].append((str(p), str(q), str(r)))

    return perm_dict


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

class Permutation:
    def __init__(self, lst):
        assert set(lst) == set(range(1, LIST_SIZE + 1))
        self.lst = lst

    def neighbor(self, t):
        lst = self.lst[:]
        i = lst.index(t.j)
        j = lst.index(t.i)
        (lst[i], lst[j]) = (lst[j], lst[i])
        return Permutation(lst)

    def __eq__(self, other):
        return self.lst == other.lst

    def __lt__(self, other):
        return self.lst < other.lst

    def __str__(self):
        return str(self.lst)

    def __hash__(self):
        return hash(tuple(self.lst))


orig = Permutation(list(range(1, LIST_SIZE + 1)))
dct = brute_search(orig, transpositions)

print("all permutations:")
for permutation in sorted(dct):
    lst = sorted(dct[permutation], key=lambda tup: len(tup)) 
    print(permutation)
    for elem in lst:
        print(" ", len(elem), elem)
print()

print("</pre>")
