# -----------------------------------------------------------------------
# JaberAlJ — https://github.com/JaberAlJ
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# This class find the path between two vertexes in a graph using the
# Depth-First Search algorithm.
# -----------------------------------------------------------------------

from stdlib import Graph
from stdlib import Stack
from .node import Node

class DFSPath:
    
    def __init__(self, graph:Graph, source:int, goal:int) -> None:
        """
        Construct a DFSPath object based on graph, source and goal vertices
        """
        self._found = False
        self._goal  = None

        # check if both source and goal are in the graph
        self._check(graph, source)
        self._check(graph, goal)

        self.__dfs(graph, source, goal)

    
    def _check(self, graph:Graph, vertex:int):
        """
        Ensure that the vertex is a valid vertex.
        """
        graph.degree(vertex)
    
    def __dfs(self, graph:Graph, source:int, goal:int):
        """
        Run DFS on a graph to find a path from source to goal
        """

        agenda  = Stack()
        visited = []    # was missing

        firstNode = Node(source, 0, 0, None)
        agenda.push(firstNode)

        # DFS Loop
        while not(agenda.isEmpty()):
            node = agenda.pop()

            if not(node.state in visited):      # was missing

                # add state to visited
                visited.append(node.state)      # was missing

                # if we found the goal
                if node.state == goal:
                    self._goal = node # remember the goal node
                    self._found = True
                    break # exist the loop
                
                # put the successor nodes in the stack.
                for successor in graph.adj(node.state):

                    # create a successor node (sN)
                    sN = Node(successor, node.depth + 1, node.cost + 1, node)
                    agenda.push(sN)
                    
    def solution(self) -> Stack:
        """
        Construct a solution by moving along the search tree and return 
        the path in a stack
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
    
    @property
    def found(self) -> bool:
        """
        Return true if the goal is reachable
        """
        return self._found
    

    def print_solution(self) -> None:
        """
        Print the solution (if found) to the standard output.
        """

        if not(self.found):
            print("No path found")
        else:
            output = ""
            for state in self.solution():
                output += f"{state} "
            

            print("Path:", output.strip().replace(" ", " -> "))