from typing import Optional


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.curr_size = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def next(self, val: int) -> float:
        self._enqueue(val)
        return self._calculate_average()

    def _enqueue(self, val: int):
        if self._is_empty():
            self.head = Node(val)
            self.tail = Node(val)
        else:
            new_node = Node(val, self.tail, None)
            if self.head.get_right() is None:
                self.head.set_right(new_node)
            self.tail.set_right(new_node)
            self.tail = new_node
            if self._is_full():
                self._dequeue()
        self.curr_size = self.curr_size + 1

    def _dequeue(self):
        if self._is_empty():
            return

        next_head = self.head.get_right()
        if next_head is not None:
            next_head.set_left(None)
            del self.head
            self.head = next_head
            self.curr_size = self.curr_size - 1

    def _peek(self):
        return self.head

    def _is_full(self) -> bool:
        return self.curr_size >= self.size

    def _is_empty(self) -> bool:
        return self.head is None and self.tail is None

    def _calculate_average(self) -> float:
        current_node = self.tail
        cumulative = current_node.get_value()
        while (current_node.get_left() is not None):
            next = current_node.get_left()
            cumulative = cumulative + next.get_value()
            current_node = next

        return cumulative/self.curr_size


class Node:

    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_value(self) -> int:
        return self.value

    def is_head(self) -> bool:
        return self.left is None

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node
