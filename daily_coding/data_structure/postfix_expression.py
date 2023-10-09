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
    
    
    
# 첫째 줄에 중위 표기식이 주어진다. 단 이 수식의 피연산자는 알파벳 대문자로 이루어지며 수식에서 한 번씩만 등장한다. 
# 그리고 -A+B와 같이 -가 가장 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 주어지지 않는다. 
# 표기식은 알파벳 대문자와 +, -, *, /, (, )로만 이루어져 있으며, 길이는 100을 넘지 않는다. 
import sys
def postfix1():
  expression = list(input())
  res = ""
  opstack = []
  for char in expression:
    if char.isalpha(): # 숫자는 순서가 유지되기 때문에 바로 더해줌. 
      res += char
    elif char == "(": # 열린괄호는 1순위. 스택에 더해서 우선순위의 기준이 됨.
      opstack.append(char)
    elif char in ["*", "/"]: # 곱셈, 나눗셈은 2순위. 괄호안의 같은 우선순위의 연산자인 곱셈과 나눗셈을 결과에 더해주고 스택에 들어감. 
      while opstack and opstack[-1] in ["*", "/"]:
        res += opstack.pop()
      opstack.append(char)
    elif char in ["+", "-"]: # 덧셈, 뺄셈은 연산 순위 최하위. 괄호안의 다른 연산자들을 결과에 더해주고 스택에 들어감.
      while opstack and opstack[-1] != "(":
        res += opstack.pop()
      opstack.append(char)
    elif char == ")": # 괄호의 경우 최우선으로 계산되기 때문에 괄호안의 연산자들 모두 결과에 더해주고 스택에 들어감.
      while opstack and opstack[-1] != "(":
        res += opstack.pop()
      opstack.pop() # 열린괄호는 제외해주어야 기준이 바뀔 수 있음. 
  while opstack: # 괄호를 제외한 나머지 연산자들을 더해줌.
    res += opstack.pop()
  print(res)
postfix1()