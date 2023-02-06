# input must in order from 0 to N
def isNewBetter(prefer, w, m, old):
  for i in range(N):
    if (prefer[w][i] == old):
      return True

    if (prefer[w][i] == m):
      return False
 
def stableMarriage(prefer):
  wPartner = [-1 for i in range(N)]

  mFree = [False for i in range(N)]

  freeCount = N

  while (freeCount > 0):      
    mNum = 0
    while (mNum < N):
      if (mFree[mNum] == False):
        break
      mNum += 1
 
    rank = 0
    while (rank < N and mFree[mNum] == False):
      w = prefer[mNum][rank]

      if (wPartner[w - N] == -1):
        wPartner[w - N] = mNum
        mFree[mNum] = True
        freeCount -= 1
      else:
        old = wPartner[w - N]

        if (isNewBetter(prefer, w, mNum, old) == False):
          wPartner[w - N] = mNum
          mFree[mNum] = True
          mFree[old] = False
      rank += 1
 
  print("Woman ", "  Man")
  for i in range(N):
    print(i + N, "\t" * 3, wPartner[i])
 
N = 4
prefer = [[7, 5, 6, 4], [5, 4, 6, 7],
          [4, 5, 6, 7], [4, 5, 6, 7],
          [0, 1, 2, 3], [0, 1, 2, 3],
          [0, 1, 2, 3], [0, 1, 2, 3]]

# N = 3
# prefer = [[0, 1, 2], [2, 1, 0],
#           [0, 1, 2], [1, 0, 2],
#           [0, 1, 2], [0, 1, 2]]
 
stableMarriage(prefer)