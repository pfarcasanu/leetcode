## Number of ways to convert number to alpha
##   111 -> aaa, ak, ka
##   1111 -> aaaa, aak, aka, kaa, kk
##   127 -> abg, lg (27 doesn't convert) 
##   001 -> none (0 doesn't convert)

def num_convert(num: str):
  if '0' in num:
    return 0

  def can_convert_2(idx):
    if idx > len(num) - 2:
      return False
    return int(num[idx:idx+2]) <= 26

  def helper(idx):
    if idx >= len(num):
      return 1
    convert_1 = helper(idx + 1)
    convert_2 = 0 if not can_convert_2(idx) else helper(idx + 2)
    return convert_1 + convert_2

  return helper(0)

def test(num, expected):
  actual = num_convert(num)
  if actual == expected:
    print("[PASS] ", num)
  else:
    print("[FAIL] ", num)
    print(" |- expected: ", expected)
    print(" |- actual: ", actual)

test("111", 3)
test("126", 3)
test("1111", 5)
test("127", 2)
test("01", 0)