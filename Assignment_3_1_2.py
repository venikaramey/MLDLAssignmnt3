def myfilter(function,iterable):
    it = iter(iterable)
    value = next(it)
    for element in it:
        value = function(value, element)
    return value

def Checkeven(x):
  if x %2 == 0:
    return True
  else:
    return False

Num = [3, 10, 17, 18, 25, 32]
Even = filter(Checkeven, Num)
for x in Even:
  print(x)