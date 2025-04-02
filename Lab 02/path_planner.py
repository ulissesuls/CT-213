from grid import Node, NodeGrid
from math import inf
import heapq

class PathPlanner(object):
    """
    Represents a path planner, which may use Dijkstra, Greedy Search or A* to plan a path.
    """
    def __init__(self, cost_map):
        """
        Creates a new path planner for a given cost map.

        :param cost_map: cost used in this path planner.
        :type cost_map: CostMap.
        """
        self.cost_map = cost_map
        self.node_grid = NodeGrid(cost_map)

    @staticmethod
    def construct_path(goal_node):
        """
        Extracts the path after a planning was executed.

        :param goal_node: node of the grid where the goal was found.
        :type goal_node: Node.
        :return: the path as a sequence of (x, y) positions: [(x1,y1),(x2,y2),(x3,y3),...,(xn,yn)].
        :rtype: list of tuples.
        """
        node = goal_node
        # Since we are going from the goal node to the start node following the parents, we
        # are transversing the path in reverse
        reversed_path = []
        while node is not None:
            reversed_path.append(node.get_position())
            node = node.parent
        return reversed_path[::-1]  # This syntax creates the reverse list

    def dijkstra(self, start_position, goal_position):
        """
        Plans a path using the Dijkstra algorithm.

        :param start_position: position where the planning stars as a tuple (x, y).
        :type start_position: tuple.
        :param goal_position: goal position of the planning as a tuple (x, y).
        :type goal_position: tuple.
        :return: the path as a sequence of positions and the path cost.
        :rtype: list of tuples and float.
        """
		# Todo: implement the Dijkstra algorithm
		# The first return is the path as sequence of tuples (as returned by the method construct_path())
		# The second return is the cost of the path
        # Dijkistra do not use the "f" atribute, because is a uniform cost search
        
        # Reset the grid before
        self.node_grid.reset()
        
        # Initial variables
        start_i, start_j = start_position
        finish_i, finish_j = goal_position
        
        # Defining the start and goal nodes
        start_node = self.node_grid.get_node(start_i, start_j)
        finish_node = self.node_grid.get_node(finish_i, finish_j)
        
        # Creating a priority queue
        pq = []
        
        # Defining initial cost of the first node
        start_node.g = 0
        
        # Inserting the first element in the heap (start)
        heapq.heappush(pq, (start_node.g, start_node))
        
        # While the list is not empty:
        while pq:            
            current_gcost, current_node = heapq.heappop(pq)
            
            # Verifying if the node is already explored
            if current_node.closed is True:
                continue
            # Mark the current_node as a closed node
            current_node.closed = True
            
            # Verifying if the search can be finished
            if current_node == finish_node:
                return self.construct_path(finish_node), finish_node.g
            
            i, j = current_node.get_position()
            
            for successor in self.node_grid.get_successors(i, j):
                
                # Getting the next node
                i_next, j_next = successor
                exploring_node = self.node_grid.get_node(i_next, j_next)
                
                # Calculate the edge cost for the g parameter
                current_distance = self.cost_map.get_edge_cost((i,j), (i_next, j_next))
                
                if exploring_node.g > current_gcost + current_distance:
                    
                    exploring_node.g = current_gcost + current_distance
                    exploring_node.parent = current_node
                    heapq.heappush(pq, (exploring_node.g, exploring_node))
        
        # if no path to the goal was found
        return [], inf

    def greedy(self, start_position, goal_position):
        """
        Plans a path using greedy search.

        :param start_position: position where the planning stars as a tuple (x, y).
        :type start_position: tuple.
        :param goal_position: goal position of the planning as a tuple (x, y).
        :type goal_position: tuple.
        :return: the path as a sequence of positions and the path cost.
        :rtype: list of tuples and float.
        """
		# Todo: implement the Greedy Search algorithm
		# The first return is the path as sequence of tuples (as returned by the method construct_path())
		# The second return is the cost of the path
        # Greedy does not matter about the better path, but the fastest path. Uses only h(n), i.e. euclidian distance.
        
        # Reset the grid before
        self.node_grid.reset()
        
        # Initial variables
        start_i, start_j = start_position
        finish_i, finish_j = goal_position
        
        # Defining the start and goal nodes
        start_node = self.node_grid.get_node(start_i, start_j)
        finish_node = self.node_grid.get_node(finish_i, finish_j)
        
        # Creating a priority queue
        pq = []
        
        # Defining initial costs of the first node (g and h)
        start_node.g = 0
        start_node.f = start_node.distance_to(finish_i, finish_j)
        
        # Inserting the first element in the heap (start)
        heapq.heappush(pq, (start_node.f, start_node))
        
        # While the list is not empty:
        while pq:            
            current_fcost, current_node = heapq.heappop(pq)
            
            # Verifying if the node is already explored
            if current_node.closed is True:
                continue
            
            # Mark the current_node as a closed node
            current_node.closed = True
            
            # Verifying if the search can be finished
            if current_node == finish_node:
                final_path = self.construct_path(finish_node)
                
                return final_path, finish_node.g
            
            i, j = current_node.get_position()
            
            for successor in self.node_grid.get_successors(i, j):
                
                # Getting the next node
                i_next, j_next = successor
                exploring_node = self.node_grid.get_node(i_next, j_next)
                
                # Calculate the edge cost for the g parameter
                current_distance = self.cost_map.get_edge_cost((i,j), (i_next, j_next))
                
                if exploring_node.g > current_node.g + current_distance:
                    
                    exploring_node.g = current_node.g + current_distance
                    exploring_node.f = exploring_node.distance_to(finish_i, finish_j)
                    exploring_node.parent = current_node
                    heapq.heappush(pq, (exploring_node.f, exploring_node))
        
        # if no path to the goal was found
        return [], inf

    def a_star(self, start_position, goal_position):
        """
        Plans a path using A*.

        :param start_position: position where the planning stars as a tuple (x, y).
        :type start_position: tuple.
        :param goal_position: goal position of the planning as a tuple (x, y).
        :type goal_position: tuple.
        :return: the path as a sequence of positions and the path cost.
        :rtype: list of tuples and float.
        """
		# Todo: implement the A* algorithm
		# The first return is the path as sequence of tuples (as returned by the method construct_path())
		# The second return is the cost of the path
        # A* combines the heuristic function h(n) with the minor cost g
        
        # Reset the grid before
        self.node_grid.reset()
        
        # Initial variables
        start_i, start_j = start_position
        finish_i, finish_j = goal_position
        
        # Defining the start and goal nodes
        start_node = self.node_grid.get_node(start_i, start_j)
        finish_node = self.node_grid.get_node(finish_i, finish_j)
        
        # Creating a priority queue
        pq = []
        
        # Defining initial costs of the first node (g and h)
        start_node.g = 0
        start_node.f = start_node.g + start_node.distance_to(finish_i, finish_j) # f(n) = g(n) + h(n)
        
        # Inserting the first element in the heap (start)
        heapq.heappush(pq, (start_node.f, start_node))
        
        # While the list is not empty:
        while pq:            
            current_fcost, current_node = heapq.heappop(pq)
            
            # Verifying if the node is already explored
            if current_node.closed is True:
                continue
            
            # Mark the current_node as a closed node
            current_node.closed = True
            
            # Verifying if the search can be finished
            if current_node == finish_node:
                return self.construct_path(finish_node), finish_node.g
            
            i, j = current_node.get_position()
            
            for successor in self.node_grid.get_successors(i, j):
                
                # Getting the next node
                i_next, j_next = successor
                exploring_node = self.node_grid.get_node(i_next, j_next)
                
                # Calculate the edge cost for the g parameter
                current_distance = self.cost_map.get_edge_cost((i,j), (i_next, j_next))
                
                if exploring_node.g > current_node.g + current_distance:
                    
                    exploring_node.g = current_node.g + current_distance
                    exploring_node.f = exploring_node.g + exploring_node.distance_to(finish_i, finish_j)
                    exploring_node.parent = current_node
                    heapq.heappush(pq, (exploring_node.f, exploring_node))
        
        # if no path to the goal was found
        return [], inf