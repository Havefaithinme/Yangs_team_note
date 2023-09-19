# 10799번
# 여러 개의 쇠막대기를 레이저로 절단하려고 한다. 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.
# 쇠막대기와 레이저의 배치는 다음 조건을 만족한다.

# 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
# 쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다.
# 위 예의 괄호 표현은 그림 위에 주어져 있다.

# 쇠막대기는 레이저에 의해 몇 개의 조각으로 잘려지는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘려지고, 이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘려진다.

# 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하시오.

import sys
if __name__ == "__main__":
    state = list(sys.stdin.readline().strip())
    # 열린괄호 = 새로운 막대 혹은 레이저. stack에 추가한다.
    # 닫힌괄호 = 막대의 끝 혹은 레이저. 열린괄호 바로 직후의 닫힌 괄호는 레이저, 닫힌괄호 바로 직후의 닫힌괄호는 막대의 끝
    # 2개의 상태를 이용해 막대의 분할 상태를 변경. => 스택의 열린 괄호 개수 = 현재의 레이저가 분할할 수 있는 막대의 수. = 추가되는 괄호 개수
    sticks = []
    ans = 0
    for i, char in enumerate(state):
        if not sticks:
            sticks.append(char)
            ans += 1
            # print(sticks, ans)
            continue
        if char == "(":
            ans += 1
            sticks.append(char)
            # print(sticks, ans)
        elif char == ")":
            if state[i-1] == "(":  # lazer
                sticks.pop()
                ans += len(sticks) - 1
                # print(sticks, ans)
            elif state[i-1] == ")":  # end of a stick
                sticks.pop()
                # print(sticks, ans)
    ans = ans if ans > 0 else 0
    print(ans)
