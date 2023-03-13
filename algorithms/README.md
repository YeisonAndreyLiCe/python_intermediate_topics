## Algorithm Complexity
### Temporal Complexity vs Spatial Complexity
Temporal complexity is the time it takes to run an algorithm. Spatial complexity is the amount of memory it takes to run an algorithm. The two are often related, but not always. For example, a sorting algorithm may have a high temporal complexity, but a low spatial complexity. A sorting algorithm may also have a low temporal complexity, but a high spatial complexity. The two are often related, but not always. For example, a sorting algorithm may have a high temporal complexity, but a low spatial complexity. A sorting algorithm may also have a low temporal complexity, but a high spatial complexity. The two are often related, but not always. For example, a sorting algorithm may have a high temporal complexity, but a low spatial complexity. A sorting algorithm may also have a low temporal complexity, but a high spatial complexity. 

## Example 
```python
def f(x):
    answer = 0 # 1
    for i in range(1000):
        answer += 1  # 1000
    for j in range(x):
        answer += x  # x
    for i in range(x): 
        for j in range(x):  # x^2
            answer += i * j 
    return answer # 1
    
# 1 + 1000 + x + x^2 + 1 = 1002 + x + x^2 
```

## Big O Notation
### Addition Rule
```python
def f(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)
# O(n) + O(n) = O(n + n) = O(2n) = O(n)
```
```python
def f(n):
    for i in range(n):
        print(i)
    for i in range(n * n):
        print(i)
# O(n) + O(n^2) = O(n + n^2) = O(n^2)
```

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# O(2^n)
```

- O(1) - Constant
- O(log n) - Logarithmic
- O(n) - Linear
- O(n log n) - Log Linear
- O(n^2) - Quadratic
- O(2^n) - Exponential
- O(n!) - Factorial

## Dynamic Programming
- Optimal Substructure: An optimal solution can be constructed from optimal solutions of its subproblems.
- Overlapping Subproblems: The same subproblem is solved multiple times.
- Memoization: Store the results of subproblems, so we don't have to solve them multiple times.
### Memoization
```python
def fibonacci(number: int, memo={}):
    if number == 0 or number == 1:
        return number
    try:
        return memo[n]
    except KeyError:
        result = fibonacci(number - 1, memo) + fibonacci(number - 2, memo)
        memo[number] = result
        return result
```

## Greedy Algorithms
- A greedy algorithm makes the locally optimal choice at each stage with the hope of finding a global optimum.
- Greedy algorithms are not always optimal.
- Greedy algorithms are often used as a subprocedure to solve more complex problems.
- Greedy algorithms are often used to solve optimization problems.

## Divide and Conquer
- Divide the problem into a number of subproblems that are smaller instances of the same problem.
- Conquer the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the subproblems in a straightforward manner.
- Combine the solutions to the subproblems into the solution for the original problem.

## Backtracking
- Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons each partial candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

## Randomized Walks
- Randomized walks are a type of algorithm that uses random numbers to solve problems.
- Randomized walks are often used to solve optimization problems.
- Randomized walks are often used to solve search problems.
- Randomized walks are often used to solve simulation problems.

