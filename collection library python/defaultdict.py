"""
collections.defaultdict Masterclass
===================================

A `defaultdict` works exactly like a standard Python dictionary, but with one massive superpower: 
It NEVER throws a `KeyError`. 

If you try to access or modify a key that doesn't exist, `defaultdict` will automatically 
create that key and assign it a default value on the fly.

THE BIG QUESTION: Why not just use a normal dict?
-------------------------------------------------
In a normal dict, if you want to append to a list of values, you have to write boilerplate:
    if key not in my_dict:
        my_dict[key] = []
    my_dict[key].append(value)

With a defaultdict, you skip the check completely:
    my_dict[key].append(value) # Creates the list and appends instantly!

HOW IT WORKS:
-------------
When you create a defaultdict, you pass it a "default factory" (a function). 
When a missing key is accessed, it calls that function to generate the default value.
- int() returns 0
- list() returns []
- set() returns set()
"""

from collections import defaultdict

# ==========================================
# 1. THE PROBLEM IT SOLVES
# ==========================================
print("--- 1. The Normal Dict Crash ---")
normal_dict = {}
# normal_dict['missing_key'] += 1  # ❌ THIS CRASHES WITH A KeyError!


# ==========================================
# 2. defaultdict(int) - THE COUNTER
# ==========================================
# Passing 'int' tells it: "If a key is missing, its default value is 0"
print("\n--- 2. defaultdict(int) ---")
int_dict = defaultdict(int)

# We don't need to check if 'apples' exists. It defaults to 0, then adds 5!
int_dict['apples'] += 5  
int_dict['bananas'] += 1

print(f"Apples: {int_dict['apples']}")
print(f"Oranges (Never added!): {int_dict['oranges']}") # Automatically returns 0!


# ==========================================
# 3. defaultdict(list) - THE GROUPER
# ==========================================
# Passing 'list' tells it: "If a key is missing, its default value is an empty list []"
# This is incredibly useful for grouping items.
print("\n--- 3. defaultdict(list) ---")

list_dict = defaultdict(list)
students = [('Math', 'Deepa'), ('Science', 'John'), ('Math', 'Sarah')]

for subject, name in students:
    # No "if subject not in list_dict:" needed!
    list_dict[subject].append(name)

print("Grouped by Subject:", dict(list_dict))


# ==========================================
# 4. defaultdict(set) - UNIQUE GROUPER
# ==========================================
# Passing 'set' tells it: "If a key is missing, its default value is an empty set set()"
# Useful when you want to group items but ignore duplicates.
print("\n--- 4. defaultdict(set) ---")

set_dict = defaultdict(set)
# Notice 'Deepa' is added to Math twice
students_with_dupes = [('Math', 'Deepa'), ('Math', 'Deepa'), ('Science', 'John')]

for subject, name in students_with_dupes:
    set_dict[subject].add(name)

print("Unique Students by Subject:", dict(set_dict))


# ==========================================
# 5. CUSTOM FACTORY FUNCTIONS
# ==========================================
# You can pass ANY function that returns a value. Usually, we use a lambda function.
print("\n--- 5. Custom Default Values ---")

# "If a key is missing, return the string 'Not Found'"
custom_dict = defaultdict(lambda: "Not Found")

custom_dict['user_1'] = "Admin"
print(f"user_1: {custom_dict['user_1']}")
print(f"user_2: {custom_dict['user_2']}") # Returns 'Not Found'


# ==========================================
# 6. REAL WORLD DSA: GRAPH ADJACENCY LIST
# ==========================================
# If you ever get a Graph problem on LeetCode (like "Number of Islands" or "Course Schedule"),
# Step 1 is almost always building an Adjacency List using defaultdict(list).

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "E")
]

# We want a dictionary that shows who each node connects to:
# {'A': ['B', 'C'], 'B': ['D'], 'C': ['E']}

graph = defaultdict(list)

for u, v in edges:
    graph[u].append(v)
    # If it was an undirected (two-way) graph, you'd also do: graph[v].append(u)

print("\n--- 6. Graph Adjacency List ---")
for node, neighbors in graph.items():
    print(f"Node {node} connects to -> {neighbors}")
"""eof

The Graph Adjacency List example at the bottom is the absolute most important takeaway here. When you progress to the "Trees and Graphs" phase of your DSA roadmap, `defaultdict(list)` will be the very first line of code you write in almost every solution!"""