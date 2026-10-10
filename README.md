# IT3012 — Pac-Man Search Algorithms

## Intelligent Systems — Group Assignment

This project implements classical Artificial Intelligence search algorithms using the Pac-Man environment.

The objective is to implement uninformed and informed search algorithms and use them to find paths through mazes and solve more complex search problems.

## 1. Project Progress

| Question | Algorithm | Contributor | Status |
|---|---|---|---|
| Q1 | Depth First Search (DFS) | IT24100802 | Completed — PASS |
| Q2 | Breadth First Search (BFS) | IT24101801 | Completed — PASS |
| Q3 | Uniform Cost Search (UCS) | IT24101861 | Completed — PASS |
| Q4 | A* Search | IT24102710 | Completed — PASS |
| Q5 | Corners Problem | To be updated | Pending |
| Q6 | Corners Heuristic | IT24100802 | Completed - PASS |
| Q7 | Food Heuristic | To be updated | Pending |

**Current testing progress:** Q1–Q4 passed all available local autograder tests.

## 2. Implemented Algorithms

### Q1 — Depth First Search (DFS)

**Contributor:** IT24100802  
**Branch:** `Question1_DFS_IT24100802`  
**Function:** `depthFirstSearch()`  
**File:** `search.py`

DFS is an uninformed search algorithm that explores deeper nodes before backtracking.

It uses a Stack with Last In, First Out (LIFO) behaviour.

The implementation tracks expanded states and returns a valid sequence of actions when the goal is reached.

DFS does not guarantee the shortest path.

**Autograder result:** 3/3 — PASS

### Q2 — Breadth First Search (BFS)

**Contributor:** IT24101801  
**Branch:** `Question2_BFS_IT24101801`  
**Function:** `breadthFirstSearch()`  
**File:** `search.py`

BFS is an uninformed search algorithm that explores nodes level by level.

It uses a Queue with First In, First Out (FIFO) behaviour.

The implementation uses an expanded-state set to prevent repeated expansion and tracks the actions needed to reach the goal.

BFS guarantees a shortest path in number of actions when all movement costs are equal.

**Autograder result:** 3/3 — PASS

### Q3 — Uniform Cost Search (UCS)

**Contributor:** IT24101861  
**Branch:** `Question3_UCS_IT24101861`  
**Function:** `uniformCostSearch()`  
**File:** `search.py`

UCS is an uninformed search algorithm that selects the node with the lowest accumulated path cost.

It uses a Priority Queue.

Its priority is based on:

`g(n) = Actual cost from the starting state to node n`

UCS finds a minimum-cost path when step costs are nonnegative and the usual search conditions hold.

**Autograder result:** 3/3 — PASS

### Q4 — A* Search

**Contributor:** IT24102710  
**Branch:** `Question4_AStarSearch_IT24102710`  
**Function:** `aStarSearch()`  
**File:** `search.py`

A* is an informed search algorithm that combines the actual path cost and an estimate of the remaining cost.

It uses a Priority Queue with the evaluation function:

`f(n) = g(n) + h(n)`

Where:

- `g(n)` = Actual path cost from the starting node
- `h(n)` = Estimated remaining cost
- `f(n)` = Estimated total path cost

With a suitable admissible and consistent heuristic, A* can find an optimal solution efficiently.

**Autograder result:** 3/3 — PASS

## 3. Environment Setup

### Requirements

- Python 3.9–3.11
- Git
- NumPy and Matplotlib, as specified in the assignment setup

### Using a Python Virtual Environment on Windows

Create a virtual environment with Python 3.11:

```powershell
py -3.11 -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the assignment's listed packages:

```powershell
pip install numpy matplotlib
```

Verify Python:

```powershell
python --version
```

Run the Pac-Man game:

```powershell
python pacman.py
```

## 4. Autograder Testing

Run individual autograder tests:

```powershell
python autograder.py -q q1
python autograder.py -q q2
python autograder.py -q q3
python autograder.py -q q4
```

### Verified Results — October 10, 2026

| Question | Tests Passed | Local Score | Status |
|---|---:|---:|---|
| Q1 — DFS | 5/5 | 3/3 | PASS |
| Q2 — BFS | 5/5 | 3/3 | PASS |
| Q3 — UCS | 10/10 | 3/3 | PASS |
| Q4 — A* | 6/6 | 3/3 | PASS |
| **Total** | **26/26** | **12/12** | **PASS** |

These are the scores reported by the provided local autograder, not the final course grade.

## 5. Pac-Man Execution Testing

The following tests were performed using the `mediumMaze` layout.

### Commands

**DFS**

```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
```

**BFS**

```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

**UCS**

```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```

**A* with Manhattan Heuristic**

```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

### Execution Results

| Algorithm | Path Cost | Nodes Expanded | Pac-Man Score | Result |
|---|---:|---:|---:|---|
| DFS | 130 | 146 | 380 | WIN |
| BFS | 68 | 269 | 442 | WIN |
| UCS | 68 | 269 | 442 | WIN |
| A* | 68 | 221 | 442 | WIN |

All four algorithms successfully found paths to the goal.

### Observations

- DFS expanded 146 nodes but returned a longer path with cost 130.
- BFS found a shortest path with cost 68 and expanded 269 nodes.
- UCS also found a path with cost 68 and expanded 269 nodes.
- A* with Manhattan distance found a path with cost 68 while expanding 221 nodes.
- A* reduced the number of expanded nodes compared with BFS and UCS in this maze.

## 6. Algorithm Comparison

| Feature | DFS | BFS | UCS | A* |
|---|---|---|---|---|
| Search type | Uninformed | Uninformed | Uninformed | Informed |
| Data structure | Stack | Queue | Priority Queue | Priority Queue |
| Exploration rule | Deepest first | Shallowest first | Lowest path cost | Lowest estimated total cost |
| Priority | LIFO | FIFO | g(n) | g(n) + h(n) |
| Uses a heuristic | No | No | No | Yes |
| Optimality | Not guaranteed | Equal-cost steps | Nonnegative costs under standard conditions | Suitable heuristic and conditions |

## 7. Git Branches and Contributions

| Branch | Contributor | Task |
|---|---|---|
| `main` | Group | Integrated code |
| `Question1_DFS_IT24100802` | IT24100802 | Q1 DFS |
| `Question2_BFS_IT24101801` | IT24101801 | Q2 BFS |
| `Question3_UCS_IT24101861` | IT24101861 | Q3 UCS |
| `Question4_AStarSearch_IT24102710` | IT24102710 | Q4 A* |

Each question is developed in a separate branch to support code review, collaboration, and individual contribution tracking.

## 8. Pending Implementation

The remaining implementation tasks are:

**Q5 — Corners Problem**
- Implement `CornersProblem` in `searchAgents.py`.
- Represent the current position and visited corners.
- Implement start state, goal checking, and successor generation.

**Q6 — Corners Heuristic**
- Implement `cornersHeuristic()` in `searchAgents.py`.
- Ensure admissibility and consistency.
- Optimize the number of expanded nodes.

**Q7 — Food Heuristic**
- Implement `foodHeuristic()` in `searchAgents.py`.
- Estimate the remaining cost of collecting all food dots.
- Ensure admissibility and consistency.
- Optimize search efficiency.

## 9. Integration and Final Testing

After all seven implementations have been reviewed and merged into `main`, execute:

```powershell
python autograder.py
```

Capture the final autograder results and verify that Q1–Q7 all pass.

## 10. Project Structure

```text
IT3012-Pacman-Search-Algorithms/
├── search.py
├── searchAgents.py
├── util.py
├── pacman.py
├── game.py
├── autograder.py
├── layouts/
├── test_cases/
└── README.md
```

## 11. Attribution

The Pac-Man AI starter project is based on the UC Berkeley CS188 Pac-Man search project.

Original copyright, license, and attribution notices must be preserved. Any public distribution of starter or solution code must comply with the applicable project license and lecturer instructions.

Reference: http://ai.berkeley.edu

---

**Current Status:** Q1–Q4 passed local autograder and mediumMaze execution tests. Q5–Q7 remain pending.
