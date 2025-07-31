class Node:
    """Doubly Linked List node for LRU Cache"""
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    Problem:
    Design a data structure that follows the LRU (Least Recently Used) cache rules.
    Implement the LRUCache class with:
      - get(key): return value if key exists, else -1.
      - put(key, value): insert/update the value. If the cache exceeds capacity, evict the least recently used item.

    Approach:
    - Use a combination of a **HashMap** and a **Doubly Linked List**.
    - HashMap: maps keys → nodes for O(1) lookup.
    - Doubly Linked List: maintains usage order (head = most recent, tail = least recent).

    Helper methods:
    - _add_node(node): Add a new node right after dummy head.
    - _remove_node(node): Remove an existing node from the list.
    - _move_to_head(node): Move an existing node to the head (mark as most recently used).
    - _pop_tail(): Remove and return the least recently used node (node before dummy tail).

    Complexity:
    - Time: O(1) for both get and put operations.
    - Space: O(capacity) for storing up to `capacity` nodes.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key → Node

        # Create dummy head and tail to avoid null checks
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---------- Helper Methods ----------

    def _add_node(self, node):
        """Always add new node right after head."""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove an existing node from the linked list."""
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        """Move given node to the head (mark as recently used)."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Pop the least recently used node (right before dummy tail)."""
        node = self.tail.prev
        self._remove_node(node)
        return node

    # ---------- Core API Methods ----------

    def get(self, key: int) -> int:
        """
        If key exists:
          - Move its node to the head (recently used)
          - Return its value
        Else:
          - Return -1
        """
        node = self.cache.get(key)
        if not node:
            return -1

        # Move node to head (mark as most recently used)
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        If key already exists:
          - Update value
          - Move node to head
        Else:
          - Create a new node
          - Add to head and hashmap
          - If capacity exceeded → remove tail node and delete from hashmap
        """
        node = self.cache.get(key)

        if not node:
            # Create a new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)

            if len(self.cache) > self.capacity:
                # Remove least recently used node
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            # Update value and move to head
            node.value = value
            self._move_to_head(node)