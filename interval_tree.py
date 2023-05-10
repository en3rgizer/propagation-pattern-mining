from typing import Union, List, Tuple, Dict, Optional

class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def contains(self, point) -> bool:
        return  self.start <= point <= self.end

class Node:
    def __init__(self, interval: Interval, vmax=None, vmin=None, left=None, right=None, **kwargs) -> None:
        self.interval = interval
        self.vmax = vmax if not vmax is None else self.interval.end
        self.vmin = vmin if not vmin is None else self.interval.start
        self.left = left
        self.right = right
        self.kwargs = kwargs

class IntervalTree:
    def __init__(self) -> None:
        self.root = None

    def add(self, interval: Interval, **kwargs) -> None:
        new_node = Node(interval, **kwargs)
        if self.root is None:
            self.root = new_node
            return
        n = self.root
        while True:
            n.vmax = max(n.vmax, interval.end)
            n.vmin = min(n.vmin, interval.start)
            if interval.start <= n.interval.start:
                if n.left is None:
                    n.left = new_node
                    return
                else:
                    n = n.left
            else:
                if n.right is None:
                    n.right = new_node
                    return
                else:
                    n = n.right
        return

    def query_point(self, point) -> List:
        if self.root is None:
            return []
        res = []
        queue = [self.root]
        while len(queue) > 0:
            n = queue.pop(0)
            if n.interval.start <= point <= n.interval.end:
                res.append(n.kwargs)
            if not n.left is None and n.left.vmin <= point <= n.left.vmax:
                queue.append(n.left)
            if not n.right is None and n.right.vmin <= point <= n.right.vmax:
                queue.append(n.right)
        return res


    
