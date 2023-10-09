# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
import sys
def findAlpha():
    strs = list(sys.stdin.readline())
    ans = {chr(v):-1 for v in range(97, 123)}
    for i, char in enumerate(strs):
        if ans[char] == -1:
            ans[char] = i
        elif ans[char] != -1:
            continue
    print(ans.values())
findAlpha()

# 문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

# 각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.
import sys
def stringCount():
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
stringCount()

# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
import sys 
def numAlpha():
  word = list(input())
  lower_case = [chr(i) for i in range(97, 123)]
  res = {key:0 for _, key in enumerate(lower_case)}
  for char in word:
    res[char] += 1
  print(*[i for i in res.values()])

numAlpha()