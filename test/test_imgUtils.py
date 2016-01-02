from imgUtils import *

def test_bin_image_loading():
	assert getBinImg("img/3.png") == [[ 0, 0, 0, 0],
									  [ 0, 1, 0, 0],
									  [ 0, 0, 0, 1],
									  [ 0, 0, 1, 1]]



