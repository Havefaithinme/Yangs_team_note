# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 에라토스테네스의 체를 이용한 구현

def prime_list(n):
    sieve = [True]*n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i, m+1, i):
                sieve[j] = False
    return sieve
        
def main():
    a, b = map(int, input().split(" "))
    primes = prime_list(b)
    for i, prime in enumerate(primes[a:]):
        if prime == True:
            print(i)