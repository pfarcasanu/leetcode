### Caesar cipher word groupings

def normalize(s):
  new_s = [''] * len(s)
  upshift = (26 - ord(s[0]) + 97) % 26
  for i, c in enumerate(s):
    newc = (ord(c) - 97 + upshift) % 26
    new_s[i] = chr(newc + 97)
  return "".join(new_s)

def groupings(words):
  out = {}
  for word in words:
    normword = normalize(word)
    group = out.get(normword, [])
    group.append(word)
    out[normword] = group
  return list(out.values())

print(groupings(["abc", "bcd", "bde", "cef", "yza"]))