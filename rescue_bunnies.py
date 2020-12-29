from itertools import combinations

def loop(times):
    for k in range(len(times)):
        for c in combinations(range(len(times)),k):
            sum = times[c[k-1]][c[0]]
            for i in range(k-1):
                sum += times[c[i]][c[i+1]]
            if sum < 0:
                return True
    return False
