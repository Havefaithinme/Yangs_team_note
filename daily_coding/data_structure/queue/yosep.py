# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
# 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

if __name__ == "__main__":
    import sys
    import logging
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    N, K = list(map(int, sys.stdin.readline().split()))
    circle = [i+1 for i in range(N)]
    res = []
    current = -1
    for _ in range(N):
        count = 0
        while count < K:
            if circle[current] != None:
                count += 1
            current = (current + 1) % N
            logger.info("*"*30)
            logger.info(f"count  : {count}")
            logger.info(f"current: {current}")
            logger.info(f"circle : {circle}")
        res.append(circle[current-1])
        circle[current] = None
    print(res)