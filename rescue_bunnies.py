from itertools import combinations


def solutions(w, time_limit):
    # checking for negative cycles
    n = len(w)
    for k in range(2, n + 1):
        for c in combinations(range(n), k):
            cycle_dist = w[c[k - 1]][c[0]]
            for i in range(k - 1):
                cycle_dist += w[c[i]][c[i + 1]]
            if cycle_dist < 0:
                return list(range(n - 2))

    # Floyd-Warshall
    d = w  # shortest paths distance matrix
    p = [[i if i != j else None for j in range(n)] for i in range(n)]  # predecessors matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = p[k][j]

    def on_path(a, b):
        onpath = {b}
        while p[a][b] != a:
            b = p[a][b]
            onpath.add(b)
        return onpath

    def collection(togo, current=0, time_left=time_limit):
        print(togo)
        if not togo and d[current][n - 1] <= time_left:
            return True
        for target in togo:
            time_left_after = time_left - d[current][target]
            togonext = togo - on_path(current, target)
            if collection(togonext, target, time_left_after):
                return True
        return False

    for bunny_num in range(n - 2, -1, -1):
        for c in combinations(range(1, n - 1), bunny_num):
            # set(c) is a collection of bunnies
            if collection(set(c), 0, time_limit):
                return [x - 1 for x in c]
