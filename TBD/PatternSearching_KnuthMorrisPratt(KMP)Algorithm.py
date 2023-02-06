def KMPSearch(pat, txt):
  pat_len = len(pat)
  txt_len = len(txt)

  lps = [0] * pat_len
  pat_index = 0

  computeLPSArray(pat, pat_len, lps)

  txt_index = 0
  while txt_index < txt_len:
    if pat[pat_index] == txt[txt_index]:
      txt_index += 1
      pat_index += 1

    if pat_index == pat_len:
      print ("Found pattern at index " + str(txt_index - pat_index))
      pat_index = lps[pat_index - 1]
    # mismatch after pat_index matches
    elif txt_index < txt_len and pat[pat_index] != txt[txt_index]:
      # Do not match lps[0..lps[pat_index - 1]] characters,
      # they will match anyway
      if pat_index != 0:
        pat_index = lps[pat_index - 1]
      else:
        txt_index += 1
  
def computeLPSArray(pat, pat_len, lps):
  len = 0 # length of the previous longest prefix suffix

  lps[0]
  now = 1

  while now < pat_len:
    # If letters match, now and len plus 1, otherwise only now plus 1.
    if pat[now] == pat[len]:
      len += 1
      lps[now] = len
      now += 1
    else:
      #  
      if len != 0:
        len = lps[len - 1]

        # From the back to the first, all of letters are different.
      else:
        lps[now] = 0
        now += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)

txt = "THIS IS A TEST TEXT"
pat = "TEST"
KMPSearch(pat, txt)

txt = "AABAACAADAABAABA"
pat = "AABA"
KMPSearch(pat, txt)