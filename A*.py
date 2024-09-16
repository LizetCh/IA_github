
from heapq import heappop, heappush

def heuristic(node, end):
  # Simple heuristics, in this case, Manhattan distance
	#
  return abs(node[0] - end[0]) + abs(node[1] - end[1])


def a_star(graph, start, end):
	open_list = [] #elements waiting to be explored
	#                   total estimated cost, actual cost, node, path to current node
	heappush(open_list, (0 + heuristic(start, end), 0, start, [start]))
	visited_list = set() #list of visited nodes

	while open_list:
		_, cost, node, path = heappop(open_list)
		if node in visited_list:
			continue
		if node == end:
			return path
		
		visited_list.add(node)
		
		for neighbor, neighbor_cost in graph[node].items():
			if neighbor not in visited_list:
				new_cost = cost + neighbor_cost
				heappush(open_list, (new_cost + heuristic(neighbor, end), new_cost, neighbor, path + [neighbor]))
				
	return None


graph = {
    (0, 0): {(0, 1): 2, (1, 0): 4},
    (0, 1): {(0, 0): 2, (0, 2): 1, (1, 1): 3},
    (0, 2): {(0, 1): 1, (1, 2): 5},
    (1, 0): {(0, 0): 4, (1, 1): 1},
    (1, 1): {(1, 0): 1, (0, 1): 3, (1, 2): 2},
    (1, 2): {(1, 1): 2, (0, 2): 5, (2, 2): 1},
    (2, 2): {(1, 2): 1, (2, 3): 3},
    (2, 3): {(2, 2): 3, (1, 3): 4},
    (1, 3): {(2, 3): 4, (0, 3): 2},
    (0, 3): {(1, 3): 2}
}

start_node = (0, 0)
end_node = (0, 3)

print(a_star(graph, start_node, end_node))
