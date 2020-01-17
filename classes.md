# Short notes on the classes

## Class 0: Generalities
- The Zen of Python
    - `import this`
- Duck Typing
    - If it walks like a duck and it quacks like a duck, then it must be a duck
- A word on efficiency
    - Premature optimisation is the root of all evil
    - Premature pesimisation vs. premature optimisation
    - If you do care:
        - Vectorise and measure
        - Rule of thumb: Shorter (in number of calls) is better
- A word on inheritance
    - Think about it as decorating the class

## Class 1: Flat containers
- [p.20 UML diagram]
- List comprehensions
    - Syntax
    - Their values are local: `x = 3; [x for x in range(5)]`
    - Prefer list comprehension over `map` / `filter`
    - Cartesian product.
- Generator expressions [More in Chapter 14]
    - Syntax
    - Example in for loop and min function
- Tuples
    - Syntax
    - As immutable lists
    - As records: Less space than an object
    - Unpacking (as with any sequence)
        - Swap two variables
        - Star operator for calling functions with tuple (Ex.)
        - Return multiple values (Ex.)
        - Nesting works fine (Ex.)
    - `Card = collections.namedtuple('Card', ['rank', 'suit'])`
- Slicing
    - Syntax (Ex palindrome: a == a[::-1])
    - Slice object. `seq.__getitem___(slice(start, stop, step))`
    - Multidimensional slicing. [`my_seq.py`]
    - Ellipsis (Numpy)
    - Assigning to slice: rhs has to be an iterable
- Sequences
    - Operator + and *
        - Lists of lists and operator *. [`operator_mul.py`, `fix_operator_mul.py`]
        - Mention empty list of lists
    - Operator += and *=: Mutable vs immutable [`mutable_vs_immutable.py`]
        - Puzzle [`puzzle.py`]: Putting mutable objects in immutable objects is not good
    - Sorted sequences
        - `.sort()` vs `sorted`
        - `bisect`, `insort`
- A word on numpy / scipy / torch
- Deques
    - Efficiency and thread-safe
    - Rotate and append left / right
    - Removing from middle is slow
    - Mention heapq module and asyncio.PriorityQueue

## Class 2: Mappings
- Dictionaries
    - Hashable objects:
        - Implements `__eq__` and `__hash__` and `a == b` => `hash(a) == hash(b)`
            - If you impelment `__eq__` you also have to implement `__hash__`
        - An immutable object is "always" hashable. A list is not.
    - `dict` comprehensions
    - `__getitem__` just called by `operator[]`, not by get or `__contains__`.
    - Don't look up more than you need to
        - `.get(key, default)` returns None or the element, but it is not inserted
        - `.setdefault()`: If not, the element is inserted
        - `collections.defaultdict(list)`: Just default value for `__getitem__`
        - `__missing__`
    - Other dicts:
        - `collections.OrderedDict`: Keeps an order on the keys
        - `collections.ChainMap`: "Flattens" a few dicts into one
        - `collections.Counter`
        - `UserDicts`: Just override magic methods and you're good. [Ex. strkeydict.py]
    - Everything in Python is a dictionary
        - `__dir__`
        - There are functions to access these inner things:
            - `vars`
            - `setattr(obj, a, 0) == obj.__dict__["a"] = 0 == obj.a = 0`
            - `hasattr`
- Sets
    - Set comprehensions and empty set
    - `frozenset` (built-in type)
    - Use & (intersection) operator to find multiple elements in set.
        - `len(set(needles).intersection(haystack))`
    - Create a `set` or a `frozenset` is a good use case for generators
- Under the hood
    - Explain hash tables: Upper part of hash to find bucket, lower part to resolve collisions
    - The hash() function is salted. The salt is constant at a process level.
    - Avg 1-2 collisions. 1/3 of the hash table empty
    - They are not memory efficient
        - But they are not as bad as they used to be: (See history below)
        - 2./ Keys were scrambled
        - 3.5 Randomised
        - 3.6 Ordered but not guaranteed by the standard
        - 3.7 Ordered guaranteed by the standard
- Design of a hash table
    - Taken from: https://www.youtube.com/watch?v=p33CVV29OG8
    - Separate chaining: Two buckets [[(hash, key, value), ...], [(hash, key, value), ...]]
        - It wastes empty buckets
        - Every list needs room to grow
    - Open addressing
        [(key, value), None, None, (key, value), None]
        - Linear probing
        - Gets rids of the extra lists
        - Catastrophic pile-up
    - Open addressing multiple pile-up
        - Random number generator (random probing)
    - Compact dict
        [list with (hash, key, value)]
        [pointer to position in list] # [0, None, 4, 3, None, None] -> 1 byte in size

## Class 3: Functional programming
- Functions are first-class citizens
    - Create, pass around and return functions at runtime
    - Higher-order functions (Ex. key for `sorted` or `max`. `map`, `filter`, and `reduce` (`fold`).
    - Lambda (anonymous) functions.
        - Not very useful: You can define a function anywhere
- Seven flavours of operator() (testeable with `callable()`):
    - User defined function / lambda
    - Built-in function
    - Built-in methods
    - Methods
    - Classes: When invoked with `__new__`
    - Classes instances (Functors) (functions with state) (a word on closures and decorators)
    - Coroutines
- Function introspection
    - `__dict__` : Stores the attributes of a function
    - `f.__code__.co_varnames`, `f.__code__.co_argcount`
    - `inspect` module (Ex. p.152)
- Function arguments
    - Default arguments
    - *args iterable arguments
    - **kwargs mapping arguments
    - Call by name. After default arguments or iterable arguments
- Function annotations
    - Syntax: def f(text:str) -> str
    - They do nothing -> Postprocessing needed
- Functional programming
    - `operator` module
        - shortcuts like `mul`
        - `itemgetter` for sorting (Ex `itemgetter(1)(foo) == foo[1]`)
        - `attrgetter` (attrgetter('bar')(foo) == foo.bar
        - `methodcaller (methodcaller("bar", arg1, arg2)(foo) == foo.bar(arg1, arg2))`
    - `functools` module
        - `functools.partial`.
        - Also achieved with lambdas although less fine (function.partial has the attributes of the previous function)

Extra readings:
Functional Programming HOWTO:
https://docs.python.org/3/howto/functional.html

## Class 4: Decorators and Closures
- Decorators
    - Syntax: Strictly speaking they are syntactic sugar (Ex. p.184)
    - Invoked at import time (after the function definition) (Ex. snippet on this?)
    - Example: Add functions to a list.
- Closures
    - Scope of variables. `global` keyword (Ex. 7.5 p.189)
    - Example averager: Implementation with functur and with closure
        - Add `avg.__code__.co_varnames`
        - Add `avg.__code__.co_freevars`
        - Add `avg.__closure__[0].cell_contents`
    - The only case when we have free variables that are non-global is when we have a function within a function
    - `nonlocal` declaration (Ex 7-13 p.195)
- Decorators in practice (metaprogramming!)
    - `clocked` (Ex 7.15, p.197)
    - `functools.wraps(func)`. (Ex.7.17, p.199)
    - `functools.lru_cache(maxsize, typed)`: Memoization (effortless dynamic programming) (Ex. dynammic programming)
    - `functools.singledispatch`: (Ex. 7.21 p.204)
        - Advantage: It delegates the responsability to each module, not to one function or one class
    - Decorators with parameters: Make a factory that returns a decorator (3 nested functions) (Ex 7-25 p.209)
    - Note: Difficult decorators are better implemented in a class + `__call__` fashion
    - Note: For really difficult decorators or library-level decorators, consider the module `wrapt`
- Further reading:
    - http://blog.dscpl.com.au/2014/01/how-you-implemented-your-python.html

## Class 5: Object References, Mutability, and Recycling
- Variables in Python ARE labels NOT boxes
    - Figure 8.1
    - ids are given when the variables are created. Ex. 8.2
    - id's are like the "memory address" of the variables
    - `is` compares the `id` of the variables: Useful when comparing to a singleton (faster, it's not a function)
    - Tuples are relatively immutable `a = (3, []); a[1].append(2)`
    - Copies are shallow by thefault (`l2 = list(l1)` or `l2 = l1[:]`).
    - `copy.deepcopy(obj)`: Cyclic references might be problematic, this module implements this correctly
        - `__copy__` and `__deepcopy__`
- Function parameters
    - Passed as `T *const` (copy of a constant pointer to a non-constant object)
    - Don't use mutable objects as parameter defaults
        - Different instances They will share the same instance of the parameter (Ex. 8.12 p.230)
        - They live in `C.__init__.__defaults__`
    - Don't use in-out parameters or aliase them! - deepcopy them if necessary
- Destruction
    - `del` deletes names, not objects. `__del__` is tricky to use and almost never needed
    - `weakref` module. (Ex 8.16) - Useful for caching objects
    - Refcounting
    - `weakref.WeakValueDictionary` and other weakref collections. It's fragile (Ex. 8.19)
    - Some classes (tuple, int) cannot be weakreferenced. list and dict can when subclassed
    - Interning: Some popular numbers are shared rahter than copied (not documented, don't rely on this)

## Class 6: Objects
- Object representation
    - `__repr__` (developer) and `__str__`(user).
    - `__bytes__` (sequence of bytes) and others [Ex. 9.11 p.250]
- Classmehots vs staticmethods
    - `classmethod` to provide with different constructors
- `__format__`
    - Format specifiers [Ex. 9.5 9.6 p. 255, 256]
- `__hash__`
    - Recommendable to make the class immutable: `@property`
    - Equal objects should imply equal hash
- Dunder attributes in Python
    - A comment on single underscore attributes
- `__slots__`
    - What are they
    - The behaviour is not inherited
    - Use numpy or pandas for large arrays
- `typecode`
    - It's a class attribute, and we can change it per-instance
    - To change it globally subclass

## Class 7: Sequences
p.277
