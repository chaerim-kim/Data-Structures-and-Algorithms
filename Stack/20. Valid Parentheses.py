class Solution:
  def isValid(self, s: str) -> bool:
      stack = []
      dic = {'(':')',
             '{':'}',
             '[':']'
            }

      for char in s:
          if char in dic.keys():
              stack.append(char)

          elif stack == [] or char != dic[stack.pop()] :
              return False

      return stack ==[]
