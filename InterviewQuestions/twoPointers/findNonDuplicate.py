# Easy
# Passes all test cases
class Solution:
  def remove(self, arr):
    first, second = 0, 1
    if len(arr) == 1:
      return 1
    while second <= len(arr) - 1:
        if arr[first] == arr[second]:
            arr.pop(second)

        else:
          first += 1
          second += 1

    return len(arr)

    