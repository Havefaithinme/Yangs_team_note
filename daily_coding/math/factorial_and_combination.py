# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

def my_fac():
    N = int(input())
    ans = 1
    for num in [i+1 for i in range(N)]:
        ans *= num
    return ans

def count_non_zero_from_my_fac(lst):
    ans = 0
    while lst:
        current_num = lst.pop()
        if current_num == "0":
            ans += 1
        else:
            break
    return ans

def combination(n, m):
    count = 0
    parent = 1 
    tmp = n
    while count < m:
        parent *= tmp
        tmp -= 1
        count += 1
    child = 1
    tmp = m
    while tmp > 0:
        child *= tmp
        tmp -= 1 
    return int(parent / child)

    
    
if __name__ == "__main__":
    n, m = list(map(lambda x:int(x), input().split(" ")))
    num = combination(n, m)
    ans = count_non_zero_from_my_fac(list(str(num)))
    print(ans)