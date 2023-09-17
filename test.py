a=[9,8,7,6,5,4,3,2]
print(a)
for x in range(len(a)-2):
    a.remove(a[2])
    print(a)
a.remove(a[1])
print(a)
a.remove(a[0])
print(a)

