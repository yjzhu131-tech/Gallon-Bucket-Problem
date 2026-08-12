# Gallon-Bucket-Problem

This project solves the water bucket problem:

> Measure exactly 4 gallons of water using only an unmarked 3-gallon bucket
> and an unmarked 5-gallon bucket in fewer than 15 steps. The other bucket
> must be empty at the end.

## Method

The program uses BFS, which stands for **Breadth-First Search**.

BFS checks possible moves level by level:

1. Check all paths with 0 steps.
2. Check all paths with 1 step.
3. Check all paths with 2 steps.
4. Continue until one bucket has exactly 4 gallons and the other bucket is empty.

Because BFS checks shorter paths first, the first solution it finds is a short solution.

## State

Each state is stored as:

```python
(bucket3, bucket5)
```

For example:

```python
(0, 5)
```

means:

```text
3-gallon bucket has 0 gallons
5-gallon bucket has 5 gallons
```

## Possible Moves

From any state, the program can try these moves:

- Fill the 3-gallon bucket
- Fill the 5-gallon bucket
- Empty the 3-gallon bucket
- Empty the 5-gallon bucket
- Pour the 3-gallon bucket into the 5-gallon bucket
- Pour the 5-gallon bucket into the 3-gallon bucket


## How to Run

Run this command:

```bash
python3 water_bucket_bfs.py
```

## Example Output

```text
Step 0: Start
3-gallon bucket: 0, 5-gallon bucket: 0
Step 1: Fill the 5-gallon bucket
3-gallon bucket: 0, 5-gallon bucket: 5
Step 2: Pour 5-gallon into 3-gallon
3-gallon bucket: 3, 5-gallon bucket: 2
Step 3: Empty the 3-gallon bucket
3-gallon bucket: 0, 5-gallon bucket: 2
Step 4: Pour 5-gallon into 3-gallon
3-gallon bucket: 2, 5-gallon bucket: 0
Step 5: Fill the 5-gallon bucket
3-gallon bucket: 2, 5-gallon bucket: 5
Step 6: Pour 5-gallon into 3-gallon
3-gallon bucket: 3, 5-gallon bucket: 4
Step 7: Empty the 3-gallon bucket
3-gallon bucket: 0, 5-gallon bucket: 4
Total steps: 7
```

The final result is:

```text
5-gallon bucket has exactly 4 gallons, and the 3-gallon bucket is empty.
```
