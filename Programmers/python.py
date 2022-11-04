# 한 번만 등장한 문자 ========

def solution(s):
  array = sorted([char for char in s if s.count(char) == 1])
  answer = "".join(array)
  return answer
