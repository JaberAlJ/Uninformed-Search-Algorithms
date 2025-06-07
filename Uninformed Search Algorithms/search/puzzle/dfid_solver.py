# -----------------------------------------------------------------------
# JaberAlJ — https://github.com/JaberAlJ
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# This class find the solves the N-Puzzle Problem using the 
# Depth-First-Iterative-Deepening Search approach
# -----------------------------------------------------------------------

from stdlib import Stack
from search.puzzle import Board
from .dls_solver import DLSSolver

class DFIDSolver:

    def __init__(self, initial:Board) -> None:
        """
        Construct a DFIDSolver object based on the initial board
        """

        # the solution to the puzzle is based on a DLSSolver object
        self._solver:DLSSolver = None


        # the depth where the solution was found
        self._depth:int  = None

        self.__dfid(initial)
    

    def __dfid(self, initial:Board):
        """
        Run DFID on a the initial board
        """
        d = 0       # we start at depth 0
        while self._depth == None:      # loop indefinitely
            self._solver = DLSSolver(initial, limit = d)

            if not(self._solver.reached_limit) and not(self._solver.found):
                # if we did not reach the limit and goal is not found
                # this mean the goal is not in the graph so stop the search
                break
            elif self._solver.found:
                # if we found the goal at depth d
                self._depth = d
                break
            d += 1
            
    @property
    def found(self) -> bool:
        """
        Return true if the goal is reachable
        """
        return self._solver.found
    
    @property
    def moves(self) -> int:
        """
        Return the depth where the goal was found
        """
        return self._solver.moves
    
    def solution(self) -> Stack:
        """
        Return the solution of the underlying solver object
        """
        return self._solver.solution()
    

    def print_solution(self) -> None:
        """
        Print the solution (if found) to the standard output.
        """

        if not(self._solver.found):
            print("The board can not be solved.")
        else:
            print(f"Depth = {self._depth}")
            print(f"Number of moves = {self._solver.moves}")

            for board in self.solution():
                print(board)
