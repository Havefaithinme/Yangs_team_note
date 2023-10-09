# 문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

# 각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.
import sys
def main():
    while True:
      line = input().rstrip("\n")
      if not line:
        break
      ans = [0] * 4 
      for char in line:
        if char.islower():
          ans[0] += 1 
        elif char.isupper():
          ans[1] += 1
        elif char.isdigit():
          ans[2] +=1 
        elif char.isspace():
          ans[3] += 1
      print(*ans)
      
main()