# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
import sys 
def main():
  word = list(input())
  lower_case = [chr(i) for i in range(97, 123)]
  res = {key:0 for _, key in enumerate(lower_case)}
  for char in word:
    res[char] += 1
  print(*[i for i in res.values()])

main()