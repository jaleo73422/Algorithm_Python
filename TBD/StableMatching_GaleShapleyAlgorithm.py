def stableMarriage(m, w):
  m_id = sorted(w[0])
  w_id = sorted(m[0])
  m_num = 0
  rank = 0
  m_parner = []
  wait = len(m)
  tem_m_num = m_num
  tem_rank = rank
  tem_m_parner = []

  for i in range(len(m)):
    m_parner.append(-1)

  while (wait):
    if (m[m_num][rank] not in m_parner):
      m_parner[m_num] = m[m_num][rank]
      wait -= 1
      m_num = len(m) - wait
      rank = 0
    else:
      # new parner better than older one
      if (w[w_id.index(m[m_num][rank])].index(m_id[m_num]) < w[w_id.index(m[m_num][rank])].index(m_id[m_parner.index(m[m_num][rank])])):
        tem_m_num = m_num
        tem_rank = rank
        tem_m_parner = list(m_parner)

        m_parner[m_parner.index(m[m_num][rank])] = -1
        m_parner[m_num] = m[m_num][rank]
        
        m_num = tem_m_parner.index(m[tem_m_num][tem_rank])
        rank = m[tem_m_parner.index(m[tem_m_num][tem_rank])].index(m[tem_m_num][tem_rank]) + 1
      else:
        rank += 1
      
  print(m_parner)

# m = [[8, 9, 10, 11],
#       [8, 9, 10, 11],
#       [8, 9, 10, 11],
#       [8, 9, 10, 11]]

# w = [[7, 5, 6, 4],
#       [5, 4, 6, 7],
#       [4, 5, 6, 7],
#       [4, 5, 6, 7]]

m = [[0, 1, 2],
      [2, 1, 0],
      [0, 1, 2]]

w = [[1, 0, 2],
      [0, 1, 2],
      [0, 1, 2]]

stableMarriage(m, w)