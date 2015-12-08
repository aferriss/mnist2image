import os, struct
from array import array as pyarray
from numpy import append, array, int8, uint8, zeros
from pylab import *
from numpy import *
from PIL import Image
import math
# data from  http://yann.lecun.com/exdb/mnist/
#sliced from here http://g.sweyla.com/blog/2012/mnist-numpy/

def load_mnist(dataset="training", digits=np.arange(10), path='.'):
	fname_img = os.path.join(path, 'train-images-idx3-ubyte')
	fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')

	flbl = open(fname_lbl, 'rb')
	magic_nr, size = struct.unpack(">II", flbl.read(8))
	lbl = pyarray("b", flbl.read())
	flbl.close()


	fimg = open(fname_img, 'rb')
	magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
	img = pyarray("B", fimg.read())
	fimg.close()

	#ind = [ k for k in range(size) ]
	ind = [ k for k in range(size) if lbl[k] in digits ]
	N = len(ind)


	images = zeros((N, rows, cols), dtype=uint8)
	labels = zeros((N, 1), dtype=int8)
	for i in range(len(ind)):
		images[i] = array(img[ind[i]*rows*cols : (ind[i]+1)*rows*cols ]).reshape((rows, cols))
		labels[i] = lbl[ind[i]]
	return images, labels


def load_mnist_unlabeled(dataset="training", path='.'):
	fname_img = os.path.join(path, 'train-images-idx3-ubyte')

	fimg = open(fname_img, 'rb')
	magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
	img = pyarray("B", fimg.read())
	fimg.close()

	ind = [ k for k in range(size) ]

	N = len(ind)


	images = zeros((N, rows, cols), dtype=uint8)
	for i in range(len(ind)):
		images[i] = array(img[ind[i]*rows*cols : (ind[i]+1)*rows*cols ]).reshape((rows, cols))

	return images, size

def saveIndividuals():
	images, size = load_mnist_unlabeled('training')
	print images.shape
	for i in range(size):
		im = Image.fromarray(images[i])
		im.save("numbers/img"+str(i)+".jpg")

def saveSheets():
	for num in range(10):
		images, labels = load_mnist('training', digits=[num])

		#for i in range(60000):
		#	im = Image.fromarray(images[i])
		#	im.save("sheets/img"+str(i)+".jpg")
		largeImage = Image.new("L", (2500,2500))
		y = 0
		print images.shape

		for i in range(len(images)):
			y = int(i/sqrt(len(images)))
			x = int(i%int(sqrt(len(images))))
			#print x
			im = Image.fromarray(images[i])
			largeImage.paste(im, (x*28, y*28))

		largeImage.show()
		largeImage.save("sheets/"+str(num)+".jpg")


saveIndividuals()



