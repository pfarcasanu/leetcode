def get_alphabet(words):
  graph = {}

  def add_edges(word1, word2):
    for c1, c2 in zip(word1, word2):
      if c1 != c2:
        nbs = graph.get(c1, set())
        nbs.add(c2)
        graph[c1] = nbs
        return
  
  for i in range(len(words)):
    for j in range(i + 1, len(words)):
      add_edges(words[i], words[j])

  ## Return the longest path and char.
  ans = {}
  print(graph)
  def recur(c, lcurr):
    neighbors = graph.get(c, set())
    if len(neighbors) == 0:
      return lcurr
    longest = lcurr
    for nb in neighbors:
      lnext = recur(nb, lcurr + 1)
      if lnext >= longest:
        ans[c] = nb
        longest = lnext
    return longest

  def getans(c):
    if c in ans:
      return c + getans(ans[c])
    return c

  for c in graph.keys():
    pathlen = recur(c, 0)
    if pathlen == len(graph):
      return getans(c)

def test(num, expected):
  actual = get_alphabet(num)
  if actual == expected:
    print("[PASS] ", num)
  else:
    print("[FAIL] ", num)
    print(" |- expected: ", expected)
    print(" |- actual: ", actual)

test(["ct", "bt", "tb"], "cbt")
test(["cc", "cb", "bb", "ac"], "cba")
test(["cb", "cg", "db", "dx", "dg", "bg"], "cdbxg")