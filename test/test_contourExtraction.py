from contourExtraction import *

def test_get_4_pixel_neighborhood():
	binimg = [[ 0, 0, 1, 1],
			  [ 0, 0, 1, 1],
			  [ 0, 1, 1, 1],
			  [ 0, 1, 1, 0]]

	assert get4PixelNeighborhood(binimg, Vec2(0,0)) == ((0,0), (0,0))
	assert get4PixelNeighborhood(binimg, Vec2(1,2)) == ((0,0), (0,1))
	assert get4PixelNeighborhood(binimg, Vec2(1,4)) == ((0,1), (0,0))
	assert get4PixelNeighborhood(binimg, Vec2(3,3)) == ((1,1), (1,0))
	assert get4PixelNeighborhood(binimg, Vec2(4,0)) == ((0,0), (1,0))

def test_normalize_4_pixel_neighborhood():
	neighborhood1 = ((0,0), (0,1))

	assert normalize4PixelNeighborhood(neighborhood1, Vec2(0,1)) == ((0,0), (0,1))
	assert normalize4PixelNeighborhood(neighborhood1, Vec2(1,0)) == ((0,1), (0,0))
	assert normalize4PixelNeighborhood(neighborhood1, Vec2(-1,0)) == ((0,0), (1,0))
	assert normalize4PixelNeighborhood(neighborhood1, Vec2(0,-1)) == ((1,0), (0,0))

	neighborhood2 = ((0,0), (1,1))

	assert normalize4PixelNeighborhood(neighborhood2, Vec2(-1,0)) == ((1,0), (1,0))
