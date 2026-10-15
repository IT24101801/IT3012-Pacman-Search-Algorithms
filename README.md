IT3012 — Pac-Man Search Algorithms
IT3012 — Intelligent Agent | SLIIT | Group 2026-AI-40 | 2026
Repository: IT24101801/IT3012-Pacman-Search-Algorithms
Project Overview
This project implements seven search-related tasks in the UC Berkeley CS188 Pac-Man environment. It explores uninformed search (Depth First Search, Breadth First Search, and Uniform Cost Search), informed search (A*), problem-state representation for visiting every maze corner, and admissible, consistent heuristics for visiting corners and collecting all remaining food dots.
All seven questions required by the group's assignment (Q1–Q7) are implemented in the integrated project. Their local autograder tests have passed. The project uses the provided Pac-Man engine and autograder; these are not original implementations by the group.
Team Members
Student ID	Student name	Assigned work
IT24100802	Ranawansha P. G. D. D.	Q1 DFS; Q6 Corners Heuristic
IT24101801	Vimukthi L. H. T. P.	Q2 BFS; Q5 Corners Problem; repository coordination
IT24101861	Gamage K. T. P.	Q3 UCS; Q7 Food Heuristic; testing and evidence
IT24102710	Sandul T. H. N. N.	Q4 A* Search; related test evidence
The team membership, question allocations, and contribution record are based on the final submission report.
Contents
Team Members
Implementation Status and Contributions
Algorithms and Heuristics
Requirements and Setup
Run Pac-Man with the Implemented Agents
Autograder Results
Performance Comparison
Repository Structure
Version Control and Collaboration
Assignment Submission and Evidence
Attribution
Implementation Status and Contributions
Each question was developed on a task-specific branch and integrated into `main` through GitHub pull requests.
Question	Task	Main function or class	Edited file	Contributor ID	Status
Q1	Depth First Search (DFS)	`depthFirstSearch()`	`search.py`	IT24100802	Complete — PASS
Q2	Breadth First Search (BFS)	`breadthFirstSearch()`	`search.py`	IT24101801	Complete — PASS
Q3	Uniform Cost Search (UCS)	`uniformCostSearch()`	`search.py`	IT24101861	Complete — PASS
Q4	A* Search	`aStarSearch()`	`search.py`	IT24102710	Complete — PASS
Q5	Finding All Corners	`CornersProblem`	`searchAgents.py`	IT24101801	Complete — PASS
Q6	Corners Heuristic	`cornersHeuristic()`	`searchAgents.py`	IT24100802	Complete — PASS
Q7	Food Heuristic	`foodHeuristic()`	`searchAgents.py`	IT24101861	Complete — PASS
Contributor IDs and task ownership reflect the repository's feature branches, commits, and pull requests. Refer to the group report for full names, additional shared contributions, and screenshots of Git history.
Algorithms and Heuristics
Q1 — Depth First Search (DFS)
`depthFirstSearch()` uses `util.Stack` (last in, first out) to explore the deepest available path first. It keeps a set of explored states, avoids expanding the same state repeatedly, and returns the sequence of actions when the goal is found. DFS does not guarantee a shortest path.
Q2 — Breadth First Search (BFS)
`breadthFirstSearch()` uses `util.Queue` (first in, first out) to explore states in increasing depth order. An explored-state set prevents repeated expansion. For equal-cost movements, BFS finds a shortest path in number of actions.
Q3 — Uniform Cost Search (UCS)
`uniformCostSearch()` uses `util.PriorityQueue` and prioritizes the accumulated path cost:
```text
g(n) = cost of the path from the starting state to n
```
The implementation stores the best discovered cost per state, skips outdated higher-cost queue entries, and updates a state when a cheaper route is found. UCS supports variable movement costs and finds minimum-cost solutions under the standard nonnegative-cost search assumptions.
Q4 — A* Search
`aStarSearch()` combines the cost already incurred and a heuristic estimate of the remaining cost:
```text
f(n) = g(n) + h(n)
```
It uses `util.PriorityQueue`, maintains cumulative path costs, and checks for the goal when a state is removed from the priority queue. With an appropriate admissible/consistent heuristic, A* finds an optimal route.
Q5 — Finding All Corners
`CornersProblem` represents a search state as:
```python
(position, (visited_corner_1, visited_corner_2,
            visited_corner_3, visited_corner_4))
```
The visited-corner flags are stored in a hashable tuple. `getStartState()` initializes them, `isGoalState()` checks whether every corner was visited, and `getSuccessors()` generates legal moves, updates the flags, assigns unit step costs, and maintains the expansion counter.
Q6 — Corners Heuristic
`cornersHeuristic()` estimates the remaining path cost by adding:
The Manhattan distance to the nearest unvisited corner.
A minimum spanning tree (MST) cost connecting the unvisited corners, also using Manhattan distances.
It returns zero when all four corners have been visited. On the tested `mediumCorners` layout, the heuristic led A* to expand 774 nodes, below the assignment's 1,200-node threshold for the highest performance band.
Q7 — Food Heuristic
`foodHeuristic()` estimates the remaining cost of collecting all food dots using:
```text
h(n) = maze distance to nearest remaining food
       + MST cost connecting all remaining food dots
```
Shortest-path maze distances are computed through BFS (accounting for walls) and cached in `problem.heuristicInfo`. The MST is constructed using Prim's algorithm, with its costs also cached for each remaining-food set. This provides a lower-bound estimate for the remaining route.
On the autograder's `trickySearch` test, the heuristic expanded 255 nodes, comfortably below the assignment's 9,000-node threshold for its highest performance band.
Requirements and Setup
The assignment specifies Python 3.9–3.11. Python 3.11 is recommended. Git is needed for working with the repository. NumPy and Matplotlib are listed in the assignment's environment setup.
1. Clone the repository
```powershell
git clone https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms.git
cd IT3012-Pacman-Search-Algorithms
```
2. Create a virtual environment (Windows PowerShell)
```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```
If PowerShell blocks activation under your system's execution policy, use the virtual environment's Python executable directly instead of permanently changing security settings:
```powershell
.\venv\Scripts\python.exe -m pip install numpy matplotlib
.\venv\Scripts\python.exe pacman.py
```
3. Install the packages
```powershell
python -m pip install numpy matplotlib
python --version
```
The virtual environment is excluded from version control by `.gitignore`. Do not commit or submit `venv/`.
4. Verify Pac-Man launches
```powershell
python pacman.py
```
A Pac-Man game window should open. On a headless machine or when graphics are unavailable, use the autograder commands in the testing section.
macOS / Linux alternative
```bash
python3.11 -m venv venv
source venv/bin/activate
python -m pip install numpy matplotlib
python pacman.py
```
If the `python3.11` command is unavailable, install Python 3.11 or use the version approved for the assignment. The supplied Pac-Man GUI uses Tkinter, which may need to be installed separately on some systems.
Run Pac-Man with the Implemented Agents
Run the following commands from the project's root directory after activating the Python environment. The `--frameTime 0.3` argument is optional and slows the animation for screenshots.
Question	Demonstration command
Q1 — DFS	`python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs --frameTime 0.3`
Q2 — BFS	`python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs --frameTime 0.3`
Q3 — UCS	`python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs --frameTime 0.3`
Q4 — A*	`python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --frameTime 0.3`
Q5 — Corners Problem	`python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem --frameTime 0.3`
Q6 — Corners Heuristic	`python pacman.py -l mediumCorners -p AStarCornersAgent --frameTime 0.3`
Q7 — Food Heuristic	`python pacman.py -l trickySearch -p AStarFoodSearchAgent --frameTime 0.3`
These commands produce visual demonstrations of the agents. The autograder outputs remain the primary grading evidence.
Autograder Results
The project was tested using the provided `autograder.py`. The Q1–Q7 outcomes in the submitted report were checked against the contents of the finalized ZIP. A full local autograder run was also performed while preparing this README. These are local test results, not university-issued grades.
Individual question commands
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
Question	Local autograder score	Relevant observation
Q1 — DFS	3/3	All 5 tests passed
Q2 — BFS	3/3	All 5 tests passed
Q3 — UCS	3/3	All 10 tests passed
Q4 — A*	3/3	All 6 tests passed
Q5 — Corners Problem	3/3	Tiny-corner problem test passed
Q6 — Corners Heuristic	3/3	774 expanded nodes; 106-action path on `mediumCorners`
Q7 — Food Heuristic	5/4*	All 18 tests passed; 255 expanded nodes
All seven questions identified in the submitted report passed the provided local tests. The listed local scores are not the official course marks; the assignment uses its own 40-mark allocation for Q1–Q7.
Why Q7 displays `5/4`*
The local Q7 autograder is configured with `max_points: 4`, but its `food_heuristic_grade_tricky.test` awards one base point plus one point for each of four thresholds met (15,000, 12,000, 9,000, and 7,000 nodes). With 255 expanded nodes, all four thresholds were met, giving 5 points against a configured maximum of 4. The extra displayed point is a test configuration inconsistency, not additional guaranteed course marks.
Why a full run also shows Q8
Running the complete command:
```powershell
python autograder.py
```
also executes Q8, because the provided `test_cases/CONFIG` specifies `q1 q2 q3 q4 q5 q6 q7 q8`. Q8 is not part of the lecturer's Q1–Q7 assignment requirements. Its `findPathToClosestDot()` implementation remains a starter-code placeholder, so Q8 reports `0/3`. The full local output therefore shows 23/25, including the unassigned Q8 and the extra Q7 point. Do not treat that total as the assignment score.
To run only the required questions in Windows PowerShell:
```powershell
1..7 | ForEach-Object { python autograder.py -q "q$_" }
```
Performance Comparison
The following values come from the supplied project's test results and documented Pac-Man execution runs; each layout and evaluation type is indicated to avoid comparing different test scenarios as though they were identical.
Search method	Layout / test	Path length or cost	Nodes expanded
DFS	`mediumMaze`	130	146
BFS	`mediumMaze`	68	269
UCS	`mediumMaze`, standard-cost test	68	269
A* with Manhattan heuristic	`mediumMaze`	68	221
Corners Problem with BFS	`mediumCorners` (project PR result)	106	1,966
Corners Heuristic with A*	`mediumCorners`	106	774
Food Heuristic with A*	`trickySearch`	—	255
The same-maze comparison shows A* with the Manhattan heuristic expanding fewer nodes than BFS or standard-cost UCS on `mediumMaze`. The corner heuristic also substantially reduces node expansions compared with the recorded BFS corner search. The food-heuristic test uses a different layout and should be evaluated against its own thresholds.
Repository Structure
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
Version Control and Collaboration
Work was implemented on separate feature branches and reviewed/merged through pull requests.
Question	Feature branch	Merged pull request
Q1	`Question1_DFS_IT24100802`	PR #1
Q2	`Question2_BFS_IT24101801`	PR #2
Q3	`Question3_UCS_IT24101861`	PR #5
Q4	`Question4_AStarSearch_IT24102710`	PR #4
Q5	`Question5_CornersProblem_IT24101801`	PR #6
Q6	`Question6_CornersHeuristic_IT24100802`	PR #7
Q7	`Question7_FoodHeuristic_IT24101861`	PR #8
All seven listed question contributions are recorded as merged in the final group report (PRs #1, #2, #5, #4, #6, #7 and #8). GitHub commit history and report screenshots provide additional evidence of team collaboration.
Report and Submission Notes
The final report is titled IT3012: Intelligent Agent — Final Submission (2026-AI-40). It includes question explanations, code screenshots, local autograder evidence, pull-request evidence, and the group’s AI usage declarations. The report was supplied separately for README preparation; it is not present in the finalized project ZIP.
The report’s Q4 section contains a table entry referring to `breadthFirstSearch()` and the Q2 test command. Those entries appear to be copying mistakes: the actual Q4 implementation is `aStarSearch()` and the appropriate test command is `python autograder.py -q q4`. This README follows the source code and the Q4 test evidence.
Submission checklist
Keep the implemented `search.py` and `searchAgents.py` in the repository.
Include the supplied `test_cases/`, `layouts/`, Pac-Man framework, and `autograder.py` when a full runnable project is required.
Include the required final report separately if the lecturer requests it.
Do not include a virtual environment, temporary caches, or personal local paths.
Check the assignment’s source-publication and academic-integrity rules before making solutions publicly accessible.
Attribution
This project builds upon the UC Berkeley CS188 Pac-Man AI Search Project and retains its original source-code copyright and attribution notices. The Pac-Man game engine, layouts, test utilities, and autograder were provided as starter material.
UC Berkeley Pac-Man AI Projects
UC Berkeley CS188
Academic integrity and redistribution: The starter source notices specify conditions on distribution and publication of solutions. Group members should follow those notices and their lecturer's requirements when sharing the repository or final deliverables.
---
Project status: Q1–Q7 implemented, integrated into `main`, and passing the provided local autograder tests.
