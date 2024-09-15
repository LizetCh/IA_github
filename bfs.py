'''
Algorithm to find the shortest path between two nodes
'''


from collections import deque

def bfs_shortest_path(graph, start, end):
		toVisit = deque([(start, [start])]) #creates a double ended queue
		while toVisit: #while there's nodes to visit
				(node, path) = toVisit.popleft() #(node,path to node), FIFO 
				for neighbor in graph[node]:
						if neighbor not in path: #if not visited
								if neighbor == end: #check if we've arrived
										return path + [neighbor]
								else:
										toVisit.append((neighbor, path + [neighbor]))
		return None

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

start_node = 'Mérida'
end_node = 'Peto'

print(bfs_shortest_path(graph, start_node, end_node))