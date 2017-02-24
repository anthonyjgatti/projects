
from collections import defaultdict, deque
from pprint import pprint

class AGraph(object):
	'''An advanced graph analytics class.'''


	def __init__(self, connections, directed = False):
		'''Instantiate graph as defaultdict. Pass list of tuples. Graph undirected by default.'''

		self._directed = directed
		self._graph = defaultdict(set)
		for node1, node2 in connections:
			self.add_edge(node1, node2)


	def add_edge(self, from_node, to_node = None):
		'''Add edge to graph, taking from_node and to_node, if to_node is non-empty'''

		self._graph[from_node].add(to_node)
		if not self._directed and to_node:
			self._graph[to_node].add(from_node)


	def add_node(self, node):
		'''API helper function to add node - calls add_edge internally.'''

		self.add_edge(node)


	def remove_node(self, node):
		'''Remove the node after removing its associated connections.'''
		
		for v, cnxs in self._graph.iteritems():
			try:
				cnxs.remove(node)
			except KeyError:
				pass	
		try:
		 	del self._graph[node]
		except KeyError:
			pass


	def find_path(self, start, end, path = []):
		'''Using BFS, find a path from start node to end node, if there is one.'''

		visited = set(start)
		parents = {start: None}
		q = deque(start)

		while q:
			current = q.popleft()
			if current == end:
				break
			for node in list(self._graph[current]):
				if node not in visited:
					visited.add(node)
					parents[node] = current
					q.append(node)

		if end in parents:
			current = end
			while current:
				path.append(current)
				current = parents[current]
			path = ' -> '.join(node for node in reversed(path))
			print path
		else:
			print 'No path found!'


	def __str__(self, print_direction = '<->'):
		'''Print out vertices and edges nicely.'''

		if self._directed:
			print_direction = '-->'

		# return pprint(self._graph.iteritems())

		for key, value in self._graph.iteritems():
			print key, print_direction, ', '.join(node if node else '' for node in value)
		return ''



my_connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'A'), ('E', 'F'), ('F', 'C'), ('H', None)]

the_graph = AGraph(my_connections, directed = True)
print the_graph

the_graph.find_path('A','F')




