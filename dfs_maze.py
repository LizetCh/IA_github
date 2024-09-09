'''
	graph: includes a dictionary of all nodes. 
		- key is the node, values are the adjacent nodes
	start: starting node
	path: list of visited nodes
	end: end node of the path
''' 

graph = { #dictionary with all nodes
		'1': ['6'],
		'2': ['1', '3'],
		'3': ['8'],
		'4': [],
		'5': ['4'],
		'6': ['11'],
		'7': [], #dead end
		'8': ['7','13'],
		'9': ['10'],
		'10': ['5','15'],
		'11': ['12'],
		'12': ['17'],
		'13': ['14'],
		'14': ['9'],
		'15': ['20'],
		'16': [],
		'17': ['16','18'],
		'18': ['19'],
		'19': ['14'],
		'20': []
}

def dfs_all_paths(graph, start, end, path=[]):
		#if entrance value is not in graph we stop
		if start not in graph:
			print("Start value not in graph")
			return[]
		
    #if end value is not in graph we stop
		if end not in graph:
			print("End value not in graph")
			return[]
    
    #path is empty we add the first node (start node)
		path = path + [start]

		#if we have reached the end node we stop
		if start == end:
				return [path] #return the path with the nodes visited
		if not graph[start]: #check for dead end
			print(f"Dead end at: {start}")
			return[]
		

		possible_paths = [] #list for all lists path[]
		
		for node in graph[start]: #for all nodes in the specified key(start)
				if node not in path: #if we haven't visited the node
						new_paths = dfs_all_paths(graph, node, end, path) #we move to that node and continue our path searching alg until we find the end node
						for p in new_paths: #after we have the path to the end 
								possible_paths.append(p)
								
		return possible_paths



entrance = '2'
exit = '5'

print(dfs_all_paths(graph, entrance, exit))