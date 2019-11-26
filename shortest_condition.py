from itertools import product

# Parameters
valid = [12,23,31]
invalid = [21,32,13]

stop = False
inv = True
depth = 3

OPS = ['+', '-', '*', '/', '%']
DIGS = [str(x) for x in range(1,10)]


# Initialize
valid = [str(x) for x in valid]
invalid = [str(x) for x in invalid]

def merge_alternate(a, b):
  assert len(a) == len(b)
  ret = []
  for i, j in zip(a, b):
    ret += [i, j]
  return ret

def check(expr):
  all_exp = all([eval(x + expr) for x in valid])
  any_exp = any([eval(x + expr) for x in invalid])
  if all_exp and not any_exp:
    return True

  if inv:
    all_inv_exp = all([eval(x + expr) for x in invalid])
    any_inv_exp = any([eval(x + expr) for x in valid])
    if all_inv_exp and not any_inv_exp:
      return True

  return False

for d in range(1, depth+1):
  for ops in product(OPS, repeat=d):
    for digs in product(DIGS, repeat=d):
      expr = "".join(merge_alternate(ops, digs))
      if(check(expr)):
        print(expr)
        if(stop):
          exit(0)
