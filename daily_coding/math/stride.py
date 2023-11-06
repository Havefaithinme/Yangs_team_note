# 백준 17087번 숨바꼭질6
def gcd(a, b):
    # a > b
    if b == 0:
        return a
    a, b = b, a % b 
    return gcd(a, b)

if __name__ == "__main__": 
    bros_num , cur_location = list(map(int, input().split(" ")))
    bros_location = list(map(int, input().split(" ")))
    location_diffs = list(map(lambda x: abs(cur_location - x), bros_location))
    location_diffs.sort(reverse=True)
    ans = location_diffs[0]
    for i in location_diffs[1:]:
        ans = gcd(ans, i)
    print(ans)
    