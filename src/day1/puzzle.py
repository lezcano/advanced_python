t = (1, 2, [30, 40])
a = t[2]
a += [50, 60]
t[2] = a
try:
    t[2] += [50, 60]
except:
    print("TRHOWS")
print(t)

# Options:
#     a) t becomes (1, 2, [30, 40, 50, 60]).
#     b) TypeError is raised with the message 'tuple' object does not support item assignment.
#     c) Neither.
#     d) Both a and b.
