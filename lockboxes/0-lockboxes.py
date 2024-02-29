#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    
    Args:
    - boxes (list of lists): A list of lists where each inner list represents a box and contains keys to other boxes.
    
    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    visited.add(0)  
    queue = [0]     

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]  

        for key in keys:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n

print(canUnlockAll(boxes)) 
