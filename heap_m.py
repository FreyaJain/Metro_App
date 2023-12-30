class Heap:
    def __init__(self):
        self.data = []
        self.map = {}

    def add(self, item):
        self.data.append(item)
        self.map[item] = len(self.data) - 1
        self._upheapify(len(self.data) - 1)

    def _upheapify(self, ci):
        pi = (ci - 1) // 2
        while ci > 0 and self._is_larger(self.data[ci], self.data[pi]) > 0:
            self._swap(pi, ci)
            ci = pi
            pi = (ci - 1) // 2

    def _swap(self, i, j):
        ith, jth = self.data[i], self.data[j]
        self.data[i], self.data[j] = jth, ith
        self.map[ith], self.map[jth] = j, i

    def display(self):
        print(self.data)

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def remove(self):
        self._swap(0, len(self.data) - 1)
        rv = self.data.pop()
        del self.map[rv]
        self._downheapify(0)
        return rv

    def _downheapify(self, pi):
        lci = 2 * pi + 1
        rci = 2 * pi + 2
        mini = pi

        if lci < len(self.data) and self._is_larger(self.data[lci], self.data[mini]) > 0:
            mini = lci

        if rci < len(self.data) and self._is_larger(self.data[rci], self.data[mini]) > 0:
            mini = rci

        if mini != pi:
            self._swap(mini, pi)
            self._downheapify(mini)

    def get(self):
        return self.data[0]

    def _is_larger(self, t, o):
        return (t > o) - (t < o)

    def update_priority(self, pair):
        index = self.map[pair]
        self._upheapify(index)
