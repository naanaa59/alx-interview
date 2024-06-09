#!/usr/bin/python3
""" This script unlock boxes using graph traversal: BFS"""

from collections import deque


def canUnlockAll(boxes):
    """ This function opens boxes based on keys:
        It uses BFS algorithm and Queue to track visited boxes"""
    n = len(boxes)
    visited_boxes = set([0])
    queue_keys = deque([0])

    while queue_keys:
        current_box = queue_keys.popleft()
        for key in boxes[current_box]:
            if key not in visited_boxes and key < n:
                visited_boxes.add(key)
                queue_keys.append(key)
    return len(visited_boxes) == n
