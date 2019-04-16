l = [1,2,3]
#print(len(l))
#print(l.__len__())
#
#class A:
#    def __len__(self):
#        return 4
#print(len(A()))
#print(3 in l)
#print(l[2])

l1 = [i for i in range(7)]
l2 = [i for i in range(5)]
l = [(i, j) for i in l1
            for j in l2]
#print(l)
#print(type(l))
#gen = (i for i in range(7))
#import math
#def f(x):
#    return math.exp(x) + x**2
#print(
#        min(
#            f(x) for x in range(-10, 10)
#            )
#        )
#
#p = f"{l1}"
#print(p)
#t = tuple(i for i in range(5))
#print(t)
#a = t
#print(id(a))
#print(id(t))
t = (2, 5, [2,52], 4., "asaf")
#t[0] = 3
#t[2] = [21, 532]
#print(t)
#t[2].append(6)
#print(t)
#import collections
#Card = collections.namedtuple("Card", ["rank", "suit"])
#c = Card(rank=12, suit="spades")
#print(c)
#print(c.rank)

#l = "ABRACADABRA"
#def palindrome(x):
#    return l == l[::-1]
#FIRST = slice(1, 3)
#print(l[FIRST])
#print(l.__getitem__(FIRST))
#
#class A:
#    def __getitem__(self,x):
#        return x

#a =A()

#a = 3
#b = 3
#def f():
#    return (3,)
#a, = f()
#print(a)


#a = [3, 5, 6, 2, 5,2,1,6]
#c, b, *d = a
#print(c)
#print(d)

#print(a[..., 2:6, 3:6])
#print(a[:, :, :, 2:6, 3:6])
#print(a[2:6][3:6])
#a = [i for i in range(5)] * 2
#print(a)
a = [1, 5, 2, 2, 6, 3]
print(a.sort())
print(sorted((3,6,2)))
#print(a)


