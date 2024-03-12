#!/usr/bin/python3
"""
Lockedboxes
"""


def canUnlockAll(boxes: list) -> bool:
    """
    returns a boolean if all boxes
    can be opened. DFS approach
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
