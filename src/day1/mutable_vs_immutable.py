l = [1, 2, 3]
print(id(l))
l *= 2
print(l)
print(id(l))

t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t))
