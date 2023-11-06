# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 
# 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

def find_all_primes(n):
    sieve = [False, False] + [True] * (n-1)
    for i in range(2, n+1):
        if sieve[i]:
            for j in range(2*i, n+1, i):
                sieve[j] = False
    return sieve


if __name__ == "__main__":
    test_case = int(input())
    sieve = find_all_primes(1000000)
    for _ in range(test_case):
        case = int(input())
        cnt = 0
        for i in range(2, case // 2 + 1):
            if sieve[i] and sieve[case-i]:
                cnt += 1
        print(cnt)
        