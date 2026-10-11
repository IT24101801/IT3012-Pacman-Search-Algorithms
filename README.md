# IT3012 — Pac-Man Search Algorithms

**Intelligent Systems | Group Assignment | 2026**

**Repository:** [IT24101801/IT3012-Pacman-Search-Algorithms](https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms)

## Project Overview

This project implements seven search-related tasks in the UC Berkeley CS188 Pac-Man environment. It explores **uninformed search** (Depth First Search, Breadth First Search, and Uniform Cost Search), **informed search** (A*), problem-state representation for visiting every maze corner, and admissible, consistent heuristics for visiting corners and collecting all remaining food dots.

All **seven questions required by the group's assignment (Q1–Q7)** are implemented in the integrated project. Their local autograder tests have passed. The project uses the provided Pac-Man engine and autograder; these are not original implementations by the group.

## Contents

- [Implementation Status and Contributions](#implementation-status-and-contributions)
- [Algorithms and Heuristics](#algorithms-and-heuristics)
- [Requirements and Setup](#requirements-and-setup)
- [Run Pac-Man with the Implemented Agents](#run-pac-man-with-the-implemented-agents)
- [Autograder Results](#autograder-results)
- [Performance Comparison](#performance-comparison)
- [Repository Structure](#repository-structure)
- [Version Control and Collaboration](#version-control-and-collaboration)
- [Assignment Submission and Evidence](#assignment-submission-and-evidence)
- [Attribution](#attribution)

## Implementation Status and Contributions

Each question was developed on a task-specific branch and integrated into `main` through GitHub pull requests.

| Question | Task | Main function or class | Edited file | Contributor ID | Status |
|---|---|---|---|---|---|
| Q1 | Depth First Search (DFS) | `depthFirstSearch()` | `search.py` | IT24100802 | Complete — PASS |
| Q2 | Breadth First Search (BFS) | `breadthFirstSearch()` | `search.py` | IT24101801 | Complete — PASS |
| Q3 | Uniform Cost Search (UCS) | `uniformCostSearch()` | `search.py` | IT24101861 | Complete — PASS |
| Q4 | A* Search | `aStarSearch()` | `search.py` | IT24102710 | Complete — PASS |
| Q5 | Finding All Corners | `CornersProblem` | `searchAgents.py` | IT24101801 | Complete — PASS |
| Q6 | Corners Heuristic | `cornersHeuristic()` | `searchAgents.py` | IT24100802 | Complete — PASS |
| Q7 | Food Heuristic | `foodHeuristic()` | `searchAgents.py` | IT24101861 | Complete — PASS |

Contributor IDs and task ownership reflect the repository's feature branches, commits, and pull requests. Refer to the group report for full names, additional shared contributions, and screenshots of Git history.

## Algorithms and Heuristics

### Q1 — Depth First Search (DFS)

`depthFirstSearch()` uses `util.Stack` (**last in, first out**) to explore the deepest available path first. It keeps a set of explored states, avoids expanding the same state repeatedly, and returns the sequence of actions when the goal is found. DFS does **not** guarantee a shortest path.

### Q2 — Breadth First Search (BFS)

`breadthFirstSearch()` uses `util.Queue` (**first in, first out**) to explore states in increasing depth order. An explored-state set prevents repeated expansion. For equal-cost movements, BFS finds a shortest path in number of actions.

### Q3 — Uniform Cost Search (UCS)

`uniformCostSearch()` uses `util.PriorityQueue` and prioritizes the **accumulated path cost**:

```text
g(n) = cost of the path from the starting state to n
```

The implementation stores the best discovered cost per state, skips outdated higher-cost queue entries, and updates a state when a cheaper route is found. UCS supports variable movement costs and finds minimum-cost solutions under the standard nonnegative-cost search assumptions.

### Q4 — A* Search

`aStarSearch()` combines the cost already incurred and a heuristic estimate of the remaining cost:

```text
f(n) = g(n) + h(n)
```

It uses `util.PriorityQueue`, maintains cumulative path costs, and checks for the goal when a state is removed from the priority queue. With an appropriate admissible/consistent heuristic, A* finds an optimal route.

### Q5 — Finding All Corners

`CornersProblem` represents a search state as:

```python
(position, (visited_corner_1, visited_corner_2,
            visited_corner_3, visited_corner_4))
```

The visited-corner flags are stored in a hashable tuple. `getStartState()` initializes them, `isGoalState()` checks whether every corner was visited, and `getSuccessors()` generates legal moves, updates the flags, assigns unit step costs, and maintains the expansion counter.

### Q6 — Corners Heuristic

`cornersHeuristic()` estimates the remaining path cost by adding:

1. The Manhattan distance to the nearest unvisited corner.
2. A minimum spanning tree (MST) cost connecting the unvisited corners, also using Manhattan distances.

It returns zero when all four corners have been visited. On the tested `mediumCorners` layout, the heuristic led A* to expand **774 nodes**, below the assignment's **1,200-node** threshold for the highest performance band.

### Q7 — Food Heuristic

`foodHeuristic()` estimates the remaining cost of collecting all food dots using:

```text
h(n) = maze distance to nearest remaining food
       + MST cost connecting all remaining food dots
```

Shortest-path maze distances are computed through BFS (accounting for walls) and cached in `problem.heuristicInfo`. The MST is constructed using Prim's algorithm, with its costs also cached for each remaining-food set. This provides a lower-bound estimate for the remaining route.

On the autograder's `trickySearch` test, the heuristic expanded **255 nodes**, comfortably below the assignment's **9,000-node** threshold for its highest performance band.

## Requirements and Setup

The assignment specifies **Python 3.9–3.11**. Python **3.11** is recommended. Git is needed for working with the repository. NumPy and Matplotlib are listed in the assignment's environment setup.

### 1. Clone the repository

```powershell
git clone https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms.git
cd IT3012-Pacman-Search-Algorithms
```

### 2. Create a virtual environment (Windows PowerShell)

```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation under your system's execution policy, use the virtual environment's Python executable directly instead of permanently changing security settings:

```powershell
.\venv\Scripts\python.exe -m pip install numpy matplotlib
.\venv\Scripts\python.exe pacman.py
```

### 3. Install the packages

```powershell
python -m pip install numpy matplotlib
python --version
```

The virtual environment is excluded from version control by `.gitignore`. **Do not commit or submit `venv/`.**

### 4. Verify Pac-Man launches

```powershell
python pacman.py
```

A Pac-Man game window should open.

## Run Pac-Man with the Implemented Agents

Run the following commands from the project's root directory after activating the Python environment. The `--frameTime 0.3` argument is optional and slows the animation for screenshots.

| Question | Demonstration command |
|---|---|
| Q1 — DFS | `python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs --frameTime 0.3` |
| Q2 — BFS | `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs --frameTime 0.3` |
| Q3 — UCS | `python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs --frameTime 0.3` |
| Q4 — A* | `python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --frameTime 0.3` |
| Q5 — Corners Problem | `python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem --frameTime 0.3` |
| Q6 — Corners Heuristic | `python pacman.py -l mediumCorners -p AStarCornersAgent --frameTime 0.3` |
| Q7 — Food Heuristic | `python pacman.py -l trickySearch -p AStarFoodSearchAgent --frameTime 0.3` |

These commands produce visual demonstrations of the agents. The **autograder outputs** remain the primary grading evidence.

## Autograder Results

The project was tested using the provided `autograder.py`. The results below reflect the completed Q1–Q7 implementation and the recorded integrated run on **11 October 2026**, reproduced from the supplied project files.

### Individual question commands

```powershell
python autograder.py -q q1
python autograder.py -q q2
python autograder.py -q q3
python autograder.py -q q4
python autograder.py -q q5
python autograder.py -q q6
python autograder.py -q q7
```

The Q7 test also triggers its Q4 dependency.

| Question | Local autograder score | Relevant observation |
|---|---:|---|
| Q1 — DFS | 3/3 | All 5 tests passed |
| Q2 — BFS | 3/3 | All 5 tests passed |
| Q3 — UCS | 3/3 | All 10 tests passed |
| Q4 — A* | 3/3 | All 6 tests passed |
| Q5 — Corners Problem | 3/3 | Tiny-corner problem test passed |
| Q6 — Corners Heuristic | 3/3 | 774 expanded nodes; 106-action path on `mediumCorners` |
| Q7 — Food Heuristic | **5/4*** | All 18 tests passed; 255 expanded nodes |

**All seven questions required by the lecturer's assignment passed the provided local tests.** The listed local scores are **not** the official course marks; the assignment uses its own 40-mark allocation for Q1–Q7.

### Why Q7 displays `5/4`*

The local Q7 autograder is configured with `max_points: 4`, but its `food_heuristic_grade_tricky.test` awards **one base point plus one point for each of four thresholds** met (15,000, 12,000, 9,000, and 7,000 nodes). With **255 expanded nodes**, all four thresholds were met, giving **5 points against a configured maximum of 4**. The extra displayed point is a **test configuration inconsistency**, not additional guaranteed course marks.

### Why a full run also shows Q8

Running the complete command:

```powershell
python autograder.py
```

also executes **Q8**, because the provided `test_cases/CONFIG` specifies `q1 q2 q3 q4 q5 q6 q7 q8`. **Q8 is not part of the lecturer's Q1–Q7 assignment requirements.** Its `findPathToClosestDot()` implementation remains a starter-code placeholder, so Q8 reports `0/3`. The full local output therefore shows **23/25**, including the unassigned Q8 and the extra Q7 point. **Do not treat that total as the assignment score.**

To run only the required questions in Windows PowerShell:

```powershell
1..7 | ForEach-Object { python autograder.py -q "q$_" }
```

## Performance Comparison

The following values come from the supplied project's test results and documented Pac-Man execution runs; each layout and evaluation type is indicated to avoid comparing different test scenarios as though they were identical.

| Search method | Layout / test | Path length or cost | Nodes expanded |
|---|---|---:|---:|
| DFS | `mediumMaze` | 130 | 146 |
| BFS | `mediumMaze` | 68 | 269 |
| UCS | `mediumMaze`, standard-cost test | 68 | 269 |
| A* with Manhattan heuristic | `mediumMaze` | 68 | 221 |
| Corners Problem with BFS | `mediumCorners` (project PR result) | 106 | 1,966 |
| Corners Heuristic with A* | `mediumCorners` | 106 | 774 |
| Food Heuristic with A* | `trickySearch` | — | **255** |

The **same-maze** comparison shows A* with the Manhattan heuristic expanding fewer nodes than BFS or standard-cost UCS on `mediumMaze`. The corner heuristic also substantially reduces node expansions compared with the recorded BFS corner search. The food-heuristic test uses a different layout and should be evaluated against its own thresholds.

## Repository Structure

```text
IT3012-Pacman-Search-Algorithms/
├── README.md              # Project overview, setup, results and collaboration
├── search.py              # Q1–Q4: DFS, BFS, UCS and A*
├── searchAgents.py        # Q5–Q7: CornersProblem and heuristics
├── util.py                # Provided Stack, Queue and PriorityQueue
├── pacman.py              # Provided Pac-Man game entry point
├── game.py                # Provided game logic and grid structures
├── autograder.py          # Provided local test runner
├── layouts/               # Maze layouts, including mediumCorners and trickySearch
├── test_cases/            # Provided tests, including an unassigned Q8
└── .gitignore             # Excludes venv/, caches and other local files
```

Additional files from the UC Berkeley starter project are retained in the repository.

## Version Control and Collaboration

Work was implemented on separate feature branches and reviewed/merged through pull requests.

| Question | Feature branch | Merged pull request |
|---|---|---|
| Q1 | `Question1_DFS_IT24100802` | [PR #1](https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms/pull/1) |
| Q2 | `Question2_BFS_IT24101801` | [PR #2](https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms/pull/2) |
| Q3 | `Question3_UCS_IT24101861` | [PR #5](https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms/pull/5) |
| Q4 | `Question4_AStarSearch_IT24102710` | [Q4 contribution history](https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms/commits/main/) |
| Q5 | `Question5_CornersProblem_IT24101801` | [PR #6](https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms/pull/6) |
| Q6 | `Question6_CornersHeuristic_IT24100802` | [PR #7](https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms/pull/7) |
| Q7 | `Question7_FoodHeuristic_IT24101861` | [PR #8](https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms/pull/8) |

The Q4 work was integrated through multiple pull requests, so the commits/history are the authoritative record of that contribution. The final group report contains the formal contribution table and Git screenshots.

## Attribution

This project builds upon the **UC Berkeley CS188 Pac-Man AI Search Project** and retains its original source-code copyright and attribution notices. The Pac-Man game engine, layouts, test utilities, and autograder were provided as starter material.

- [UC Berkeley Pac-Man AI Projects](https://ai.berkeley.edu/)
- [UC Berkeley CS188](https://inst.eecs.berkeley.edu/~cs188/)

**Academic integrity and redistribution:** The starter source notices specify conditions on distribution and publication of solutions. Group members should follow those notices and their lecturer's requirements when sharing the repository or final deliverables.

---

**Project status: Q1–Q7 implemented, integrated into `main`, and passing the provided local autograder tests.**
