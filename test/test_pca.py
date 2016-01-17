from pca import *
import math



def test_pca():

	assert getPrincipalComponentLine([Vec2(0,0), Vec2(2,0)]) == Line(Vec2(1,0), Vec2(1,0))
	isr2 = 1/math.sqrt(2)
	assert getPrincipalComponentLine([Vec2(0,0), Vec2(1,1), Vec2(2,2)]) == Line(Vec2(1,1), Vec2(isr2, isr2))

	assert getPrincipalComponentLine([Vec2(0,1), Vec2(1,1)]) == Line(Vec2(0.5,1), Vec2(1,0))
