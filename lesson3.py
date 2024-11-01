print(str(8/1**2**2) == str(8/2**2**1))



r = 1
for i in range(4):
    r*=i

print(r)



a = [2,1,2,4]
a[1:].remove(2)
print(sum(a))



a = [1,2,3,2]
b = {1,2,3,2}
print(set(a) == b)
print(a == list(b))



nums = ['one', 'two', 'three', 'four']
numdict = {x[0]: x for x in nums}
print(numdict['t'])
