# Expected output : ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
list =['x','y','z']
result = [x*i for x in list for i in range(1,5)]
print(result)
# Expected output : ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
list =['x','y','z']
result = [x*i for i in range(1,5) for x in list]
print(result)
# Expected output : [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
list =[2,3,4]
result = [[x+y] for x in list for y in range(0,3)]
print(result)
# Expected output : [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
list =[2,3,4,5]
result = [[x+y for x in list] for y in range(0,4)]
print(result)
# Expected output : [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
list =[1,2,3]
result = [(y,x) for x in list for y in range(1,4)]
print(result)