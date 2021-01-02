from itertools import combinations


def solutions(W, time):
    # checking for negative cycles
    n = len(W)
    for k in range(2, n + 1):
        for c in combinations(range(n), k):
            cycle_dist = W[c[k - 1]][c[0]]
            for i in range(k - 1):
                cycle_dist += W[c[i]][c[i + 1]]
            if cycle_dist < 0:
                return list(range(n - 2))

    # Floyd-Warshall
    D = W  # shortest paths distance matrix
    P = [[i if i != j else None for j in range(n)] for i in range(n)] # predecessors matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = P[k][j]

    return D, P
