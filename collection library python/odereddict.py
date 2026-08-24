"""
collections.OrderedDict Masterclass
====================================

An OrderedDict is a dictionary subclass that remembers the order in which keys were first inserted.

THE BIG QUESTION: Don't regular dictionaries do this now?
---------------------------------------------------------
YES! Since Python 3.7, the standard built-in `dict` guarantees insertion order.
So why does `OrderedDict` still exist? Two main reasons:

1. Specialized Order Methods: It has methods like `.move_to_end()` that standard dicts do not have.
2. Order-Sensitive Equality: When comparing two OrderedDicts, the order matters. In standard dicts, order is ignored during comparison.

WHEN TO USE IT:
---------------
1. When you need to explicitly manipulate the order of keys (e.g., move an item to the front or back).
2. When building an LRU (Least Recently Used) Cache.
3. When you need equality comparisons to fail if the order is different.
"""

from collections import OrderedDict

# ==========================================
# 1. INITIALIZATION & BASIC USAGE
# ==========================================
# You can initialize it empty, or pass it a list of tuples.
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print("1. Basic Iteration:")
for key, value in od.items():
    print(f"Key: {key}, Value: {value}")
# Output will ALWAYS be: a, then b, then c.


# ==========================================
# 2. THE SUPERPOWER: .move_to_end()
# ==========================================
# This is the primary reason to use OrderedDict today. You cannot do this with a normal dict.
print("\n2. Using move_to_end():")

# Move 'a' to the very end of the dictionary
od.move_to_end('a')
print("After moving 'a' to the end:", list(od.keys()))  # ['b', 'c', 'a']

# Move 'c' to the very beginning (using last=False)
od.move_to_end('c', last=False)
print("After moving 'c' to the front:", list(od.keys())) # ['c', 'b', 'a']


# ==========================================
# 3. THE OTHER SUPERPOWER: .popitem(last=True/False)
# ==========================================
# In a normal dict, .popitem() ALWAYS removes the last inserted item (LIFO).
# In an OrderedDict, you can choose to remove the FIRST inserted item (FIFO).

od = OrderedDict([('x', 10), ('y', 20), ('z', 30)])
print("\n3. Using popitem():")

# Remove the LAST item (like a normal dict)
last_item = od.popitem() # Or popitem(last=True)
print(f"Popped last: {last_item}, Remaining: {list(od.keys())}") # Popped 'z'

# Remove the FIRST item (FIFO Queue behavior)
first_item = od.popitem(last=False)
print(f"Popped first: {first_item}, Remaining: {list(od.keys())}") # Popped 'x'


# ==========================================
# 4. EQUALITY COMPARISONS (The Gotcha)
# ==========================================
print("\n4. Equality Comparisons:")

# Normal Dictionaries only care about content.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(f"Normal Dicts equal? {dict1 == dict2}") # TRUE!

# OrderedDicts care about content AND order.
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(f"OrderedDicts equal? {od1 == od2}") # FALSE!


# ==========================================
# 5. REAL WORLD DSA EXAMPLE: LRU Cache
# ==========================================
class LRUCache:
    """
    A classic LeetCode problem. An LRU Cache removes the "Least Recently Used" item
    when it reaches maximum capacity. OrderedDict makes this trivial!
    """
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Because we just used it, we move it to the end (marking it as "Most Recently Used")
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and mark it as recently used
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # If we exceeded capacity, we pop the FIRST item (last=False), 
        # which is the Least Recently Used!
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

print("\n5. LRU Cache Simulation:")
lru = LRUCache(2)
lru.put(1, 100) # Cache: [1]
lru.put(2, 200) # Cache: [1, 2]
print(f"Get 1: {lru.get(1)}") # Cache becomes: [2, 1] (1 is now most recent)
lru.put(3, 300) # Exceeds capacity! Pops 2. Cache becomes: [1, 3]
print(f"Cache keys remaining: {list(lru.cache.keys())}") # [1, 3]
"""eof

This script gives you the history, the "why," and the exact syntax for the two main superpower functions: `.move_to_end()` and `.popitem(last=False)`.

For standard LeetCode problems (like Two Sum or Frequency Counting), a standard `{}` dictionary is perfectly fine and slightly faster. But if you ever see the phrase "LRU Cache" in an interview, `OrderedDict` is the tool you need!"""