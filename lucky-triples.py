def solution(l):
    n = len(l)
    p = [0]
    q = [0]
    for k in range(1, n):
        p.append(0)
        q.append(0)
        for j in range(k):
            if not l[k] % l[j]:
                p[k] += 1
                q[k] += p[j]
    return sum(q)
