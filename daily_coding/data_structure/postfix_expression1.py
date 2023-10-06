# 첫째 줄에 중위 표기식이 주어진다. 단 이 수식의 피연산자는 알파벳 대문자로 이루어지며 수식에서 한 번씩만 등장한다. 
# 그리고 -A+B와 같이 -가 가장 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 주어지지 않는다. 
# 표기식은 알파벳 대문자와 +, -, *, /, (, )로만 이루어져 있으며, 길이는 100을 넘지 않는다. 
import sys
def main():
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
main()