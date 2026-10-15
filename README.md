# IT3012 – Pac-Man Search Algorithms

## Project Overview

This project was developed for the **IT3012 – Intelligent Agents** module at the Sri Lanka Institute of Information Technology (SLIIT).

**Group:** 2026-AI-40

The project implements seven search-related tasks using the Berkeley Pac-Man framework. The main objective is to help Pac-Man find paths, visit all four corners, and collect food efficiently using search algorithms and heuristics.

## Implemented Questions

| Question | Algorithm / Task | File |
|---|---|---|
| Q1 | Depth First Search (DFS) | `search.py` |
| Q2 | Breadth First Search (BFS) | `search.py` |
| Q3 | Uniform Cost Search (UCS) | `search.py` |
| Q4 | A* Search | `search.py` |
| Q5 | Corners Problem | `searchAgents.py` |
| Q6 | Corners Heuristic | `searchAgents.py` |
| Q7 | Food Heuristic | `searchAgents.py` |

## Technologies Used

- Python 3.9–3.11
- Berkeley Pac-Man Search Framework
- Git and GitHub
- Visual Studio Code
- Python autograder

## Installation and Setup

**Step 1: Clone the repository**

```bash
git clone https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms.git
```

**Step 2: Navigate to the project folder**

```bash
cd IT3012-Pacman-Search-Algorithms
```

**Step 3: Install dependencies**

```bash
pip install numpy matplotlib
```

**Step 4: Run Pac-Man**

```bash
python pacman.py
```

## Run Search Algorithms

**Q1 – Depth First Search**

```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
```

**Q2 – Breadth First Search**

```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

**Q3 – Uniform Cost Search**

```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```

**Q4 – A* Search**

```bash
python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

**Q5 – Corners Problem**

```bash
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

**Q6 – Corners Heuristic**

```bash
python pacman.py -l mediumCorners -p AStarCornersAgent
```

**Q7 – Food Heuristic**

```bash
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```

## Testing

The project uses the provided autograder to verify the implementations.

Run individual tests:

```bash
python autograder.py -q q1
python autograder.py -q q2
python autograder.py -q q3
python autograder.py -q q4
python autograder.py -q q5
python autograder.py -q q6
python autograder.py -q q7
```

Run the full autograder:

```bash
python autograder.py
```

## Testing Results

| Question | Local Autograder Result |
|---|---|
| Q1 – DFS | 3/3 |
| Q2 – BFS | 3/3 |
| Q3 – UCS | 3/3 |
| Q4 – A* | 3/3 |
| Q5 – Corners Problem | 3/3 |
| Q6 – Corners Heuristic | 3/3 |
| Q7 – Food Heuristic | 5/4* |

**Performance Results**

- Q6 Corners Heuristic: 774 nodes expanded.
- Q7 Food Heuristic: 255 nodes expanded.
- All 18 Q7 local test cases passed.

*The provided local Q7 autograder reports 5/4 because of its scoring configuration. These are local test results, not confirmed final university marks.*

The bundled autograder also includes Q8, which is outside the seven questions covered in this assignment report.

## Group Members and Contributions

| Student ID | Student Name | Contribution |
|---|---|---|
| IT24100802 | Ranawansha P G D D | Q1 DFS, Q6 Corners Heuristic |
| IT24101801 | Vimukthi L.H.T.P. | Q2 BFS, Q5 Corners Problem, Repository Coordination |
| IT24101861 | Gamage K.T.P. | Q3 UCS, Q7 Food Heuristic |
| IT24102710 | Sandul T.H.N.N. | Q4 A* Search |

## GitHub Collaboration

The team used GitHub branches and pull requests to manage development.

| Question | Pull Request | Status |
|---|---|---|
| Q1 – DFS | #1 | Merged |
| Q2 – BFS | #2 | Merged |
| Q3 – UCS | #5 | Merged |
| Q4 – A* | #4 | Merged |
| Q5 – Corners Problem | #6 | Merged |
| Q6 – Corners Heuristic | #7 | Merged |
| Q7 – Food Heuristic | #8 | Merged |

All seven question implementations were merged into the `main` branch.

## Project Files

- `search.py` – DFS, BFS, UCS, and A* implementations.
- `searchAgents.py` – Search agents, Corners Problem, and heuristics.
- `pacman.py` – Main Pac-Man game.
- `util.py` – Stack, Queue, and Priority Queue utilities.
- `autograder.py` – Automated testing.
- `test_cases/` – Autograder test cases.

## Conclusion

This project successfully implements the seven assigned Pac-Man search tasks.

Through this assignment, our team gained practical experience with uninformed search, informed search, heuristic design, graph search, automated testing, and GitHub collaboration.

## Repository

https://github.com/IT24101801/IT3012-Pacman-Search-Algorithms

## Acknowledgement

This project is based on the UC Berkeley CS188 Pac-Man Search Project framework and was completed for educational purposes as part of the SLIIT IT3012 – Intelligent Agents module.
