'''
Algorithm to find the shortest path between two nodes
'''


from collections import deque

def bfs_shortest_path(graph, start, end):
		
	#check if start and end nodes are actually in the graphx
	if start not in graph:
		return f"{start} not in graph"
	if end not in graph:
		return f"{end} not in graph"


	if start == end:
		return [start]

	toVisit_queue = deque([(start, [start])]) #creates a double ended queue
	while toVisit_queue: #while there's nodes to visit
		(node, path) = toVisit_queue.popleft() #(node,path to node), FIFO 
		for neighbor in graph[node]:
			if neighbor not in path: #if not visited
				if neighbor == end: #check if we've arrived
					return path + [neighbor]
				else:
					toVisit_queue.append((neighbor, path + [neighbor]))
	return "No path found"

graph = {
		'Mérida': ['Hunucmá', 'Progreso', 'Motul','Kanasín', 'Umán'],
		'Hunucmá': ['Umán'],
		'Progreso': [],
		'Motul': ['Cansahcab'],
		'Kanasín': ['Knatunil','Acancéh'],
		'Umán': ['Maxcanú','Muna'],
		'Cansahcab': ['Izamal'],
		'Knatunil': ['Pisté','Sotuta','Yaxcaba'],
		'Acancéh': ['Tecoh'],
		'Maxcanú': ['Muna'],
		'Muna': ['Oxkutzcab'],
		'Izamal': ['Knatunil'],
		'Pisté': [],
		'Sotuta': ['Oxkutzcab','Tahdziú'],
		'Yaxcaba': ['Peto'],
		'Tecoh': ['Tekit'],
		'Oxkutzcab': ['Tekax'],
		'Tahdziú': ['Peto'],
		'Peto': [],
		'Tekit': ['Oxkutzcab'],
		'Tekax': ['Tzucacab'],
		'Tzucacab': ['Peto'],
}

start_node = 'Pisté'
end_node = 'Tzucacab'

print(bfs_shortest_path(graph, start_node, end_node))