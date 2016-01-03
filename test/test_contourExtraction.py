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

def test_get_normalized_neighborhood_next_dir():
	neighborhood1 = ((0,0), (1,0))

	assert getNormalizedNeighborhoodNextDir(neighborhood1) == Vec2(-1,0)



def test_denormalize_next_direction():
	assert denormalizeNextDirection(Vec2(1,0), Vec2(0,1)) == Vec2(1,0)


def test_next_path_dir():
	binimg = [[ 0, 0, 1, 1],
			  [ 0, 0, 1, 1],
			  [ 0, 1, 1, 1],
			  [ 0, 1, 1, 0]]

	assert getNextPathDir(binimg, Vec2(2,1), Vec2(2,0)) == Vec2(0,1)
	assert getNextPathDir(binimg, Vec2(2,2), Vec2(2,1)) == Vec2(-1,0)
	assert getNextPathDir(binimg, Vec2(3,3), Vec2(3,4)) == Vec2(1,0)
	assert getNextPathDir(binimg, Vec2(3,4), Vec2(2,4)) == Vec2(0,-1)

def test_extract_shape_contour_from_binimg():
	binimg1 = [[ 1, 0],
			   [ 0, 0]]

	binimg2 = [[ 0, 0, 0, 0],
			   [ 0, 0, 0, 0],
			   [ 0, 1, 1, 1],
			   [ 0, 1, 1, 0]]

	assert extractShapeContourPathFromBinImg(binimg1) == [Vec2(0,0), Vec2(0,1), Vec2(1,1), Vec2(1,0)]

	assert extractShapeContourPathFromBinImg(binimg2) == [Vec2(1,2), Vec2(1,3), Vec2(1,4), Vec2(2,4),
		Vec2(3,4), Vec2(3,3), Vec2(4,3), Vec2(4,2), Vec2(3,2), Vec2(2,2)]
