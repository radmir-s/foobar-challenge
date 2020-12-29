def solution(m):
    from fractions import Fraction as fr

    def transpose(m):
        return list(map(list, zip(*m)))

    def Minor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def det(m):
        if len(m) == 1:
            return m[0][0]

        determinant = fr(0)
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * det(Minor(m, 0, c))
        return determinant

    def inverse(m):
        determinant = det(m)

        if len(m) == 1:
            return [[1 / m[0][0]]]

        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = Minor(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * det(minor))
            cofactors.append(cofactorRow)
        cofactors = transpose(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors

    def zeros(rows, cols):
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(fr(0))
        return M

    def identity(n):
        idx = zeros(n, n)
        for i in range(n):
            idx[i][i] = fr(1)
        return idx

    def multiply(A, B):
        rowsA = len(A)
        colsA = len(A[0])
        colsB = len(B[0])

        C = zeros(rowsA, colsB)
        for i in range(rowsA):
            for j in range(colsB):
                total = fr(0)
                for ii in range(colsA):
                    total += A[i][ii] * B[ii][j]
                C[i][j] = total
        return C

    def subtract(A, B):
        rowsA = len(A)
        colsB = len(B[0])

        C = zeros(rowsA, colsB)

        for i in range(rowsA):
            for j in range(colsB):
                C[i][j] = A[i][j] - B[i][j]

        return C

    class State:
        state_num = -1

        def __init__(self, state_int):
            State.state_num += 1
            if sum(state_int) and state_int[State.state_num] != sum(state_int):
                self.p = [fr(x, sum(state_int)) for x in state_int]
            else:
                self.p = False

        def sub(self, ind):
            return [self.p[x] for x in ind]

    s = [State(state) for state in m]

    rec_ind = [i for i in range(len(m)) if s[i].p]
    trans_ind = [i for i in range(len(m)) if not s[i].p]

    if 0 in trans_ind:
        return [1] + [0] * (len(trans_ind)-1) + [1]

    A = [s[i].sub(rec_ind) for i in rec_ind]
    Q = [s[i].sub(trans_ind) for i in rec_ind]

    prob_fracs = multiply(inverse(subtract(identity(len(A)), A)), Q)[0]
    denominators = [r.denominator for r in prob_fracs]

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    lcm = denominators[0]
    for d in denominators[1:]:
        lcm = lcm / gcd(lcm, d) * d

    prob_ints = [int(lcm * x) for x in prob_fracs]
    prob_ints.append(int(lcm))

    return prob_ints