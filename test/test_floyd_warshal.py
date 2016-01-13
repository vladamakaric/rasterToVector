from floyd_warshal import *

inf = float("inf")

def test_shortest_path_lengths():

	graph1 =  [
		[0, 3, 8, inf, -4], 
		[inf, 0, inf, 1, 7],
		[inf, 4, 0, inf, inf],
		[2, inf, -5, 0, inf],
		[inf, inf, inf, 6, 0]]

	fw1 = FloydWarshal(graph1)

	assert fw1.shortestPathLengths == [
			[0, 1, -3, 2, -4],
			[3, 0, -4, 1, -1],
			[7, 4, 0, 5, 3],
			[2, -1, -5, 0, -2],
			[8, 5, 1, 6, 0] ]

	assert fw1.predecessors == [
			[None, 2, 3, 4, 0],
			[3, None, 3, 1, 0],
			[3, 2, None, 1, 0],
			[3, 2, 3, None, 0],
			[3, 2, 3, 4, None]]

def test_shortest_cycles():
	graph2 = [ [inf, inf, 1, 1],
			   [1, inf, inf, 1],
			   [inf, 1, inf, inf],
			   [inf, inf, 1, inf]]

	fw2 = FloydWarshal(graph2)

	assert fw2.shortestPathLengths == [
			[3, 2, 1, 1],
			[1, 3, 2, 1],
			[2, 1, 3, 2],
			[3, 2, 1, 3]]

	assert fw2.getShortestPath(0,0) == [0, 2, 1, 0]

def test_all_shortst
