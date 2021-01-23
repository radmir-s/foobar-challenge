def solution(w, h, s):
    hw = max(h,w)
    gcf = [[x + 1] * hw for x in range(hw)]
    for a in range(1, hw+1):
        for b in range(1, a):
            gcf[a - 1][b - 1] = gcf[b - 1][a - 1] = gcf[b - 1][a % b - 1] if a % b else b

    return gcf


if __name__ == "__main__":
    print(solution(5,7, 5))
