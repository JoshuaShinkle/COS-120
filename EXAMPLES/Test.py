def make_bricks(small, big, goal):
  while big != -1:
    if big == 0:
      if small >= goal:
        return True
      return False
    test = goal / (big*5)
    if test >= 1:
      amountLeft = goal - big * 5
      if small >= amountLeft:
        return True
      return False
    big -= 1
  return False

print(make_bricks(3,1,8))