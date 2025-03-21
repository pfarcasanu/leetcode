def get_alphabet(words):
  nodes = set()
  graph = {}
  ingraph = {}

  def increment(d, c1, c2):
    nbs = d.get(c1, set())
    nbs.add(c2)
    d[c1] = nbs

  def add_edges(word1, word2):
    for c1, c2 in zip(word1, word2):
      nodes.add(c1)
      nodes.add(c2)
      if c1 != c2:
        increment(graph, c1, c2)
        increment(ingraph, c2, c1)
        return
  
  for i in range(len(words)):
    for j in range(i + 1, len(words)):
      add_edges(words[i], words[j])

  indegrees = {}
  for c in nodes:
    nbs = ingraph.get(c, set())
    indegrees[c] = len(nbs)

  ## Load the queue w/ indegree 0
  q = []
  for c in indegrees:
    if indegrees[c] == 0:
      q.append(c)

  result = []
  while len(q) != 0:
    curr = q.pop(0)
    result.append(curr)
    nbs = graph.get(curr, set())
    for nb in nbs:
      if nb not in indegrees:
        continue
      degrees = indegrees[nb] - 1
      if degrees == 0:
        q.append(nb)
        del indegrees[nb]
      else:
        indegrees[nb] = degrees

  return "".join(result)

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