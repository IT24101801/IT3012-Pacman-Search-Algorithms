# IT3012 — Pac-Man Search Algorithms

## Intelligent Systems — Group Assignment

This project implements Artificial Intelligence search algorithms in the Pac-Man environment. The assignment focuses on uninformed and informed search algorithms to find paths through mazes and solve search problems.

## 1. Implemented Search Algorithms

| Question | Algorithm | Implementation | Contributor |
|---|---|---|---|
| Q1 | Depth First Search (DFS) | `depthFirstSearch()` | IT24100802 |
| Q2 | Breadth First Search (BFS) | `breadthFirstSearch()` | IT24101801 |
| Q3 | Uniform Cost Search | Pending | To be updated |
| Q4 | A* Search | Pending | To be updated |
| Q5 | Corners Problem | Pending | To be updated |
| Q6 | Corners Heuristic | Pending | To be updated |
| Q7 | Food Heuristic | Pending | To be updated |

## 2. Q1 — Depth First Search (DFS)

**Contributor:** IT24100802  
**Branch:** `Question1_DFS_IT24100802`  
**File:** `search.py`

### Overview

Depth First Search (DFS) is an uninformed search algorithm that explores the deepest available nodes before backtracking.

DFS uses a Stack data structure, which follows the Last In, First Out (LIFO) principle.

### Implementation

- Search function: `depthFirstSearch()`
- Data structure: `util.Stack`
- Uses graph search to avoid repeated state expansion
- Returns a sequence of actions to reach the goal

### Testing

Run the Q1 autograder:

```bash
python autograder.py -q q1
```

Run DFS in Pac-Man:

```bash
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
```

**Test status:** Awaiting verified Q1 autograder results.

## 3. Q2 — Breadth First Search (BFS)

**Contributor:** IT24101801  
**Branch:** `Question2_BFS_IT24101801`  
**File:** `search.py`

### Overview

Breadth First Search (BFS) is an uninformed search algorithm that explores states level by level.

BFS uses a Queue data structure, following the First In, First Out (FIFO) principle.

When all step costs are equal, BFS guarantees a shortest path in terms of the number of actions.

### Implementation

- Search function: `breadthFirstSearch()`
- Data structure: `util.Queue`
- Tracks expanded states using a Python set
- Prevents repeated expansion of states
- Checks whether the goal has been reached
- Returns the action sequence from the starting state to the goal

### Autograder Testing

Command:

```bash
python autograder.py -q q2
```

**Result: PASS — 3/3 (local autograder)**

All five test cases passed:

| Test case | Result |
|---|---|
| graph_backtrack.test | PASS |
| graph_bfs_vs_dfs.test | PASS |
| graph_infinite.test | PASS |
| graph_manypaths.test | PASS |
| pacman_1.test | PASS |

### Pac-Man Execution Testing

Commands:

```bash
python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

| Metric | tinyMaze | mediumMaze |
|---|---|---|
| Path cost | 8 | 68 |
| Nodes expanded | 15 | 269 |
| Game score | 502 | 442 |
| Win rate | 100% | 100% |
| Result | PASS | PASS |

BFS successfully found a valid path and Pac-Man reached the goal in both layouts.

## 4. DFS vs BFS

| Feature | DFS | BFS |
|---|---|---|
| Search type | Uninformed | Uninformed |
| Data structure | Stack | Queue |
| Traversal | Deepest nodes first | Shallowest nodes first |
| Processing order | LIFO | FIFO |
| Shortest path guarantee | No | Yes, for equal-cost steps |
| Expanded-state tracking | Yes | Yes |

## 5. Environment Setup

**Recommended Python version:** Python 3.11

Create a Conda environment:

```bash
conda create -n cs188 python=3.11
conda activate cs188
pip install numpy matplotlib
```

Alternatively, use a Python virtual environment.

On Windows:

```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
pip install numpy matplotlib
```

Run Pac-Man:

```bash
python pacman.py
```

## 6. Git Branches

| Branch | Purpose |
|---|---|
| `main` | Integrated project |
| `Question1_DFS_IT24100802` | Q1 DFS development |
| `Question2_BFS_IT24101801` | Q2 BFS development |

Further branches will be added as the other questions are developed.

## 7. Testing and Integration

Each question is tested separately using the provided autograder.

Q1:

```bash
python autograder.py -q q1
```

Q2:

```bash
python autograder.py -q q2
```

After both implementations are merged into `main`, both tests should be repeated to verify integration.

The full autograder can be executed using:

```bash
python autograder.py
```

## 8. Group Contributions

| Student ID | Development | Testing and Additional Responsibilities |
|---|---|---|
| IT24100802 | Q1 — DFS | DFS testing and contribution evidence |
| IT24101801 | Q2 — BFS | BFS testing, README documentation, Q1/Q2 integration verification |
| Other members | Q3–Q7 | To be updated |

## 9. Project Files

| File | Description |
|---|---|
| `search.py` | Search algorithm implementations |
| `searchAgents.py` | Search problems and heuristic functions |
| `util.py` | Stack, Queue and PriorityQueue |
| `pacman.py` | Pac-Man game |
| `game.py` | Game mechanics |
| `autograder.py` | Automated testing |
| `test_cases/` | Question test cases |
| `layouts/` | Pac-Man maze layouts |

## 10. Attribution

The Pac-Man AI starter project is based on the UC Berkeley CS188 Pac-Man projects.

Original copyright, licensing and attribution notices must be preserved. Repository publication should comply with the starter project's license and the lecturer's instructions.

Reference: http://ai.berkeley.edu

---

**Project Status:** Q2 BFS tested successfully; Q1 results and final Q1/Q2 integration verification pending.
