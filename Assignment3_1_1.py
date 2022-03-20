def myreduce(function,iterable):
    it = iter(iterable)
    value = next(it)
    for element in it:
        value = function(value, element)
    return value

def my_add(a, b):
    result = a + b
    return result

x =myreduce(my_add,[0,1,2,3])
print(x)


