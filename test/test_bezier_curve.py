from bezier_curve import bern3

def test_bern3():
	assert bern3(1,0) == bern3(2,0) == bern3(3,0) == 0
	assert bern3(0,0) == 1
