"""
collections.deque (Double-Ended Queue) Masterclass
==================================================

A deque (pronounced "deck") is a list-like container designed for blazing-fast 
appends and pops from BOTH ends. 

WHY USE IT OVER A LIST?
-----------------------
In a standard Python list, appending to the end `list.append()` is fast O(1).
However, inserting or removing from the FRONT `list.insert(0, val)` or `list.pop(0)` 
is terribly slow O(n) because Python has to physically shift every other item in 
memory one slot over.

A deque is implemented in C as a doubly-linked list of blocks (size 64). 
This means adding or removing from the left side `.appendleft()` and `.popleft()` 
is instant O(1) time.

WHEN TO USE IT:
---------------
1. Queues (First-In, First-Out)
2. Stacks (Last-In, First-Out)
3. Keeping a rolling history of the last N items (using maxlen)
4. Sliding Window Algorithms in LeetCode
5. Breadth-First Search (BFS) in Graph/Tree problems
"""

from collections import deque

# ==========================================
# 1. INITIALIZATION
# ==========================================
# You can initialize a deque empty, or pass it any iterable (list, tuple, string)
empty_dq = deque()
num_dq = deque([1, 2, 3, 4])
str_dq = deque("abc")  # Becomes deque(['a', 'b', 'c'])


# ==========================================
# 2. CORE OPERATIONS: BOTH ENDS O(1)
# ==========================================
q = deque(['b', 'c'])

# Add to the right (Like a normal list)
q.append('d')       # deque(['b', 'c', 'd'])

# Add to the left (The superpower)
q.appendleft('a')   # deque(['a', 'b', 'c', 'd'])

# Remove from the right (Like a normal list)
last_item = q.pop() # returns 'd', q is now deque(['a', 'b', 'c'])

# Remove from the left (The superpower)
first_item = q.popleft() # returns 'a', q is now deque(['b', 'c'])


# ==========================================
# 3. BULK ADDING (Extending)
# ==========================================
q = deque([1, 2])

# Add multiple items to the right
q.extend([3, 4])     # deque([1, 2, 3, 4])

# Add multiple items to the left
# NOTE: They are added one by one, so the order appears reversed!
q.extendleft([-1, 0]) # deque([0, -1, 1, 2, 3, 4])


# ==========================================
# 4. ROTATION O(k)
# ==========================================
# You can shift items circularly from one end to the other.
q = deque([1, 2, 3, 4, 5])

# Rotate right by 2 (take 2 from right end, put on left end)
q.rotate(2)   # deque([4, 5, 1, 2, 3])

# Rotate left by 1 (take 1 from left end, put on right end)
q.rotate(-1)  # deque([5, 1, 2, 3, 4])


# ==========================================
# 5. THE MAGIC OF 'maxlen' (Rolling Windows)
# ==========================================
# If you set a maxlen, the deque becomes bounded. 
# Once it is full, adding an item to one end automatically discards an item from the opposite end.
history = deque(maxlen=3)

history.append("Page 1") # deque(['Page 1'])
history.append("Page 2") # deque(['Page 1', 'Page 2'])
history.append("Page 3") # deque(['Page 1', 'Page 2', 'Page 3'])

# Adding a 4th item pushes out "Page 1" from the left!
history.append("Page 4") # deque(['Page 2', 'Page 3', 'Page 4'])


# ==========================================
# 6. WHAT DEQUE IS *BAD* AT (The Trade-off)
# ==========================================
# Because a deque is a linked-list of blocks under the hood, it is not a contiguous array.
# This means RANDOM ACCESS is O(n) slow in the middle!
d = deque([0, 1, 2, 3, 4, 5])

# Accessing the ends is fast:
print(d[0])   # Fast!
print(d[-1])  # Fast!

# Accessing the middle forces Python to traverse the linked list to find it:
print(d[3])   # Slow! O(n) time. (Do not use deque if you need heavy random access)


# ==========================================
# 7. REAL WORLD DSA EXAMPLE: Breadth-First Search (BFS)
# ==========================================
def bfs_example(start_node):
    """
    In BFS, we process nodes level by level. We must process the oldest discovered 
    nodes first (FIFO Queue). A list pop(0) would cause an O(N^2) bottleneck here.
    Deque makes it O(V + E).
    """
    # Initialize queue with starting node
    queue = deque([start_node])
    visited = {start_node}
    
    while queue:
        # INSTANT O(1) removal from the front
        current = queue.popleft()
        
        # print(f"Processing {current}")
        
        # # Find neighbors (Simulated here)
        # for neighbor in get_neighbors(current):
        #     if neighbor not in visited:
        #         visited.add(neighbor)
        #         queue.append(neighbor) # Add to the back to process later
    return visited

# ==========================================
# 8. SUMMARY OF TIME COMPLEXITIES
# ==========================================
# .append()         O(1)
# .appendleft()     O(1)
# .pop()            O(1)
# .popleft()        O(1)
# len(d)            O(1)
# d[0] / d[-1]      O(1)
# d[k] (middle)     O(n) - Slower than list
# .remove(val)      O(n)
# .rotate(k)        O(k)