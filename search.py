# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    
def depthFirstSearch(problem: SearchProblem):
    
    #Search the deepest nodes in the search tree first.
    
    frontier = util.Stack()
    start_state = problem.getStartState()

    # Store each state with the path used to reach it.
    frontier.push((start_state, []))

    explored = set()

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        # Ignore states that have already been explored.
        if state in explored:
            continue

        explored.add(state)

        # Return the action sequence when the goal is reached.
        if problem.isGoalState(state):
            return actions

        # Add successors to the LIFO stack.
        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in explored:
                frontier.push((successor, actions + [action]))

    # No solution exists.
    return []

    
    util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""

    # Step 1: Create a FIFO Queue
    fringe = util.Queue()

    # Step 2: Get the start state
    start_state = problem.getStartState()

    # Step 3: Add start state and empty path
    fringe.push((start_state, []))

    # Step 4: Track expanded states
    expanded = set()

    # Step 5: Continue until queue is empty
    while not fringe.isEmpty():

        # Remove the oldest node
        current_state, path = fringe.pop()

        # Avoid expanding the same state twice
        if current_state in expanded:
            continue

        # Check if the goal is reached
        if problem.isGoalState(current_state):
            return path

        # Mark the current state as expanded
        expanded.add(current_state)

        # Explore neighbouring states
        for successor, action, stepCost in problem.getSuccessors(current_state):

            if successor not in expanded:

                # Add the action to the current path
                new_path = path + [action]

                # Add successor to the queue
                fringe.push((successor, new_path))

    # No solution exists
    return []



def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""

    # Create a priority queue
    frontier = util.PriorityQueue()

    # Get the starting state
    start_state = problem.getStartState()

    # Push (state, path, cost) with priority 0
    frontier.push((start_state, [], 0), 0)

    # Track the lowest known cost to each state
    best_cost = {start_state: 0}

    while not frontier.isEmpty():

        # Remove the node with the lowest total cost
        current_state, path, current_cost = frontier.pop()

        # Skip outdated, more expensive paths
        if current_cost > best_cost[current_state]:
            continue

        # Check whether the goal has been reached
        if problem.isGoalState(current_state):
            return path

        # Explore neighboring states
        for next_state, action, step_cost in problem.getSuccessors(current_state):

            new_cost = current_cost + step_cost

            # Keep the path only if its cost is lower
            if next_state not in best_cost or new_cost < best_cost[next_state]:

                best_cost[next_state] = new_cost
                new_path = path + [action]

                frontier.push(
                    (next_state, new_path, new_cost),
                    new_cost
                )

    # No solution found
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
