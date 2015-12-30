from PIL import Image

def pixelFilled(pix):
	return pix[0]<250 or pix[1]<250 or pix[2]<250

def getBinImg(path):
	im = Image.open(path) 
	pix = im.load()

	binImg = []

	for i in xrange(0, im.size[0]):
		binRow = []
		for j in xrange(0, im.size[1]):
			binRow.append(1*pixelFilled(pix[i,j]))
		binImg.append(binRow)

	return binImg

def printBinImg(bi):
	for br in bi:
		strRow = ""
		for pix in br:
			strRow += str(pix) + " "
		print strRow


# ib = getBinImg("img/1.png")
# printBinImg(ib)

		
