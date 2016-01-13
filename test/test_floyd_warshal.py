from floyd_warshal import *

def test_shortest_path_lengths():
	inf = float("inf")

	fw = FloydWarshal( [
		[0, 3, 8, inf, -4], 
		[inf, 0, inf, 1, 7],
		[inf, 4, 0, inf, inf],
		[2, inf, -5, 0, inf],
		[inf, inf, inf, 6, 0]])

	assert fw.shortestPathLengths == [
			[0, 1, -3, 2, -4],
			[3, 0, -4, 1, -1],
			[7, 4, 0, 5, 3],
			[2, -1, -5, 0, -2],
			[8, 5, 1, 6, 0] ]

	assert fw.predecessors == [
			[None, 2, 3, 4, 0],
			[3, None, 3, 1, 0],
			[3, 2, None, 1, 0],
			[3, 2, 3, None, 0],
			[3, 2, 3, 4, None]]
