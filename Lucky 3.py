def solution(l):
    count = 0
    n = len(l)
    for i in range(n-2):
        for j in range(i+1, n-1):
            if not l[j] % l[i]:
                for k in range(j+1,n):
                    if not l[k] % l[j]:
                        count += 1
    return count



print(solution([1]))

