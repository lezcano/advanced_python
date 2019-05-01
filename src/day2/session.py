from pprint import pprint
#print("hi")
#a = {3: "hi", 4: "hello"}
#b = a[3]
#print(3 in a)
#del a[3]
#print(a)
#print(3 in a)

#print(hash("red"))
#print(hash("rad"))
#print(hash(3.5))
l1 = ["red", "blue", "pink", "yellow"]
l2 = ["dog", "cat", "mouse", "cow"]
d = {k: value for k, value  in zip(l1, l2) if k != 2}
#pprint(d)
#print(d["red"])
#
#class A:
#    def __init__(self):
#        self.a = "hello"
#        self.b = "world"
#
#    def __eq__(self, other):
#        return (self.a, self.b) == (other.a, other.b)
#
#    def __hash__(self):
#        return hash(self.a) ^ hash(self.b)
#
#    def __str__(self):
#        return "{}, {}".format(self.a, self.b)
#
#    def __repr__(self):
#        return "A({}, {})".format(self.a, self.b)
#
#a = A()
#d[a] = 3
#print(d)

d["red"]        #fine
#d["violet"]    #throw
#print(d.get("violet", 3)) #doesn't throw
#print(d)

#e = {"first": [2,5],
#    "second":  [1,5,7]}
#for elem in ["first", "third"]:
#    e.setdefault(elem, []).append(3)
#    #try:
#    #    e[elem].append(3)
#    #except KeyError:
#    #    e[elem] = [3]
#print(e)
#from collections import defaultdict
#e = defaultdict(list)
#e["first"] = [2,4]
#e["second"].append(5)
#print(e.get("third", [4,76,2]))
#print(e)
#
#class defaultdictlist(dict):
#
#    def __missing__(self, key):
#        self[key] = []
#        return self[key]
#
#e = defaultdictlist()
#e["first"] = [2,4]
#e["second"].append(5)
#print(e)

#class A:
#    "This is my class"
#    def __init__(self):
#        self.a = "hello"
#        self.b = "world"
#
#    def __str__(self):
#        return "{}, {}".format(self.a, self.b)
#
#    def uppera(self):
#        return self.a.upper()
#
#c = A()
#print(c)
#print(c.a)
#print(getattr(c, "a"))
#print(c.__dict__["a"])
#print(c.b)
#c1 = {"a": "hello", "b": "world", "uppera": lambda s: s["a"].upper()}
##print(c1["a"])
##print(c1["uppera"](c1))
##
##print(c.uppera())
#
##pprint(globals())
#
#pprint(vars(c))
#pprint(c.__dir__())
#pprint(c.__doc__)
#
#
hugelist = [] #define here

a = set(i for i in range(5))

print(len(set(a).intersection(set(hugelist))))


