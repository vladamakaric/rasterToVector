from bezier_curve import _bern3

def test_bern3():
	assert _bern3(1,0) == _bern3(2,0) == _bern3(3,0) == 0
	assert _bern3(0,0) == 1
