# Gallon Bucket Problem

# The objective of this project is to develop a program that can solve the problem of 
# 2 kids fetching 4 gallons of water from a stream, using only an unmarked 3-gallon bucket, 
# and an unmarked 5-gallon bucket, in less than 15 steps.

from collections import deque


# Each state is written as: (water in 3-gallon bucket, water in 5-gallon bucket)
# For example, (0, 5) means the 3-gallon bucket has 0 gallons,
# and the 5-gallon bucket has 5 gallons.
start = (0, 0)
target = 4


def next_states(state):
    # Split the state into two clearer variable names.
    # Example: if state is (3, 2), then bucket3 = 3 and bucket5 = 2.
    bucket3, bucket5 = state

    # moves will store every possible move from the current state.
    # Each item looks like: (new_state, action_description)
    moves = [
        # Fill the 3-gallon bucket.
        # Only bucket3 changes to 3. bucket5 stays the same.
        ((3, bucket5), "Fill the 3-gallon bucket"),

        # Fill the 5-gallon bucket.
        # Only bucket5 changes to 5. bucket3 stays the same.
        ((bucket3, 5), "Fill the 5-gallon bucket"),

        # Empty the 3-gallon bucket.
        # Only bucket3 changes to 0. bucket5 stays the same.
        ((0, bucket5), "Empty the 3-gallon bucket"),

        # Empty the 5-gallon bucket.
        # Only bucket5 changes to 0. bucket3 stays the same.
        ((bucket3, 0), "Empty the 5-gallon bucket"),
    ]

    # Pour 3-gallon bucket into 5-gallon bucket.
    # The amount poured cannot be more than bucket3 has,
    # and cannot be more than the empty space left in bucket5.
    pour = min(bucket3, 5 - bucket5)

    # After pouring:
    # bucket3 loses "pour" gallons, and bucket5 gains "pour" gallons.
    moves.append(((bucket3 - pour, bucket5 + pour), "Pour 3-gallon into 5-gallon"))

    # Pour 5-gallon bucket into 3-gallon bucket.
    # The amount poured cannot be more than bucket5 has,
    # and cannot be more than the empty space left in bucket3.
    pour = min(bucket5, 3 - bucket3)

    # After pouring:
    # bucket5 loses "pour" gallons, and bucket3 gains "pour" gallons.
    moves.append(((bucket3 + pour, bucket5 - pour), "Pour 5-gallon into 3-gallon"))

    # Return all possible next moves to the BFS loop.
    return moves


# BFS uses a queue to decide which path to check next.
# The queue stores whole paths, not just one state.
queue = deque()

# Put the first path into the queue.
# At the beginning, the path only has the start state.
queue.append([(start, "Start")])

# visited keeps us from repeating the same bucket amounts forever.
# Without this, the program could keep filling and emptying the same buckets.
visited = {start}

# Keep searching as long as there is at least one path waiting in the queue.
while queue:
    # Take the oldest path first.
    # This is what makes it BFS: older paths have fewer steps.
    path = queue.popleft()

    # Look at the last state in this path.
    # This tells us where this path currently ends.
    state = path[-1][0]

    # Split that current state into the two bucket amounts.
    bucket3, bucket5 = state

    # Stop when either bucket has exactly 4 gallons.
    if bucket3 == target or bucket5 == target:
        break

    # Try every possible next move from the current state.
    for new_state, action in next_states(state):
        # Only use this new state if BFS has not seen it before.
        if new_state not in visited:
            # Mark the new state as seen.
            visited.add(new_state)

            # Make a new path by copying the old path and adding one new step.
            # This keeps different choices as separate paths in the queue.
            queue.append(path + [(new_state, action)])


# Print each step of the solution that BFS found.
for step, (state, action) in enumerate(path):
    # Split the state so the output is easier to read.
    bucket3, bucket5 = state

    # Print the step number, the action, and the bucket amounts after that action.
    print(f"Step {step}: {action}")
    print(f"3-gallon bucket: {bucket3}, 5-gallon bucket: {bucket5}")

print("Total steps:", len(path) - 1)
