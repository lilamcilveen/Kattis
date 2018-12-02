strin = input()


def fun(st):
  for i in range(len(st)-1):
    if ord(st[i]) == ord(st[i+1]):
      #print("consec letters", ord(st[i]), ord(st[i+1]))
      st = st[:i] + st[i+1:]
      fun(st)
      return st
  print(st)
fun(strin)
