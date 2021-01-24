from fractions import Fraction as fr


def solution(h, w, s):
    def partition(n, c=(), k=1):
        if n == 0:
            yield c
        for i in range(k, n + 1):
            for p in partition(n - i, c + (i,), i):
                yield p

    def cycles_of_partition(partition):
        for i in set(partition):
            yield i, partition.count(i)

    hw = max(h, w)
    gcf = [[x + 1] * hw for x in range(hw)]
    for a in range(1, hw + 1):
        for b in range(1, a):
            gcf[a - 1][b - 1] = gcf[b - 1][a - 1] = gcf[b - 1][a % b - 1] if a % b else b

    factorial = [1]
    for k in range(1, hw + 1):
        factorial.append(factorial[-1] * k)

    def cycle_n(gamma, theta):
        sum = 0
        for i, c_i in cycles_of_partition(gamma):
            for j, c_j in cycles_of_partition(theta):
                sum += c_i * c_j * gcf[i - 1][j - 1]

        return sum

    def denom(gamma):
        product = 1
        for i, c_i in cycles_of_partition(gamma):
            product *= i ** c_i * factorial[c_i]

        return product

    ans = fr(0)
    for gamma in partition(h):
        for theta in partition(w):
            ans += fr(s ** cycle_n(gamma, theta), denom(gamma) * denom(theta))
    return int(ans)


if __name__ == "__main__":
    print(solution(2, 3, 4))

