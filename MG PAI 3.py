from collections import deque

def is_valid_state(state, capacity):
    return 0 <= state[0] <= capacity[0] and 0 <= state[1] <= capacity[1]

def water_jug_dfs_variant(capacity, target):
    stack = deque()
    visited = set()
    stack.append((0, 0, []))  # (jug1, jug2, steps)

    while stack:
        jug1, jug2, steps = stack.pop()

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        new_steps = steps + [(jug1, jug2)]  # Create a new list with current step added

        if jug1 == target or jug2 == target:
            print("Solution Path:", new_steps)
            return new_steps

        # List of all possible next moves
        transitions = [
            (capacity[0], jug2),  # Fill jug1 to full capacity
            (jug1, capacity[1]),  # Fill jug2 to full capacity
            (0, jug2),            # Empty jug1
            (jug1, 0),            # Empty jug2
            (jug1 - min(jug1, capacity[1] - jug2), jug2 + min(jug1, capacity[1] - jug2)),  # Pour jug1 into jug2
            (jug1 + min(jug2, capacity[0] - jug1), jug2 - min(jug2, capacity[0] - jug1))   # Pour jug2 into jug1
        ]

        for new_state in transitions:
            if is_valid_state(new_state, capacity) and new_state not in visited:
                stack.append((new_state[0], new_state[1], new_steps))  # Pass the new steps list
    
    print("No solution found")
    return None

capacity = (4, 3)  # Jug1 capacity = 4, Jug2 capacity = 3
target = 2  # The target amount of water we need to reach
water_jug_dfs_variant(capacity, target)
