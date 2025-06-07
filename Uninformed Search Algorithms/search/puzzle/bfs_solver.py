# -----------------------------------------------------------------------
# JaberAlJ — https://github.com/JaberAlJ
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# This class find the solves the N-Puzzle Problem using the 
# Breadth-First-Search approach
# -----------------------------------------------------------------------


from stdlib import Queue
from stdlib import Stack
from search.puzzle import Board
from .node import Node


class BFSSolver:

    def __init__(self, initial:Board) -> None:
        """
        Initialize the solver object
        """
        self._found:bool = False
        self._goal:Node  = None

        self.__bfs(initial)

    def __bfs(self, initial:Board):
        """
        Run Breadth-First Search on the initial board
        """
        agenda = Queue()
        visited = []

        # create a new node and add it to the agenda
        firstNode = Node(initial, 0, 0, None)
        agenda.enqueue(firstNode)

        # BFS loop
        while not(agenda.isEmpty()):
            node:Node = agenda.dequeue()

            # if the board is not visited 
            if not(node.state in visited):

                # add the state to visited
                visited.append(node.state)

                if node.state.is_goal():
                    # found the goal
                    self._goal = node
                    self._found = True
                    break

                # put the successor nodes in the agenda
                for successor in node.state.neighbors():

                    # create a successor node and add it to agenda
                    # for time being the cost to a node from a parent is 1
                    neighborN = Node(successor, node.depth + 1, node.cost + 1, node)

                    agenda.enqueue(neighborN)
    
    @property
    def moves(self) -> int:
        """
        Minimum number of moves to solve initial board; -1 if unsolvable
        """
        if self._goal is None:
            return -1
        else:
            return self._goal.depth
    
    @property
    def found(self) -> bool:
        """
        Return true if the goal is reachable
        """
        return self._found
    

    def solution(self) -> Stack:
        """
        Construct a solution by moving along the search tree and return 
        the result in a stack
        """

        if self._goal is None:
            return None
        
        stack = Stack()

        # start goal node
        node = self._goal
        stack.push(node.state)

        while node.parent is not None:
            stack.push(node.parent.state)
            node = node.parent
        
        return stack
    
    def print_solution(self) -> None:
        """
        Print the solution (if found) to the standard output.
        """

        if not(self.found):
            print("The board can not be solved.")
        else:
            print(f"Number of moves = {self.moves}")

            for board in self.solution():
                print(board)