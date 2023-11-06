def gcd(a, b):
    # a > b
    if b == 0:
        return a
    a, b = b, a % b # a = b * q + r => GCD(a, b) = GCD(b, r)
    return gcd(a, b)

if __name__ == "__main__": 
    test_case = int(input())
    for i in range(test_case):
        case = list(map(int, input().split(" ")))
        ans = 0
        for j in range(1, len(case)-1):
            for k in range(j+1, len(case)):
                ans += gcd(case[j], case[k])
        print(ans)
         