# 후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.
# 첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다.
# (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 
# 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.
# 후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

if __name__ == "__main__":
    import sys
    import pprint
    N = int(sys.stdin.readline())
    postfix = list(sys.stdin.readline().strip())
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    nums = [None] * 26 
    for i in range(N):
        nums[i] = int(sys.stdin.readline())
    num_dict = {char: num for (num, char) in zip(nums, alphabet)}
    stack = []
    for char in postfix:
        if char not in alphabet: # operator
            first, second = stack.pop(), stack.pop() # stack should have at least 2 elements.
            if char == "*":
                stack.append(first * second)
            elif char == "-":
                stack.append(second - first)  
            elif char == "+":
                stack.append(first + second)
            else: 
                stack.append(second / first)
        else:
            stack.append(num_dict[char])
    print(f"{stack[0]:0.2f}")
    
    